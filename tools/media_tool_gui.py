#!/usr/bin/env python3
"""
Desktop GUI for the local media tools in this repository.

It wraps:
  - tools/furina_pv_downloader.py
  - tools/local_srt_from_media.py

Run:
  python tools/media_tool_gui.py

Optional drag-and-drop support:
  python -m pip install -U tkinterdnd2
"""

from __future__ import annotations

import os
import queue
import subprocess
import sys
import threading
from pathlib import Path
from tkinter import (
    BooleanVar,
    END,
    LEFT,
    RIGHT,
    BOTH,
    X,
    Y,
    filedialog,
    messagebox,
    StringVar,
    Text,
    Tk,
)
from tkinter import ttk

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
except ImportError:
    DND_FILES = None
    TkinterDnD = None


REPO_ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = Path(__file__).resolve().parent
DOWNLOAD_SCRIPT = TOOLS_DIR / "furina_pv_downloader.py"
SRT_SCRIPT = TOOLS_DIR / "local_srt_from_media.py"
DEFAULT_DOWNLOAD_DIR = REPO_ROOT / "_downloads" / "furina-pv"
MEDIA_FILETYPES = [
    ("Media files", "*.mp4 *.mov *.mkv *.avi *.webm *.mp3 *.wav *.m4a *.flac *.aac *.ogg *.wma"),
    ("All files", "*.*"),
]


class MediaToolApp:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("本地媒体工具")
        self.root.geometry("980x720")
        self.root.minsize(860, 620)

        self.log_queue: queue.Queue[tuple[str, str | None]] = queue.Queue()
        self.process: subprocess.Popen[str] | None = None
        self.worker: threading.Thread | None = None

        self.download_url_file = StringVar()
        self.download_out_dir = StringVar(value=str(DEFAULT_DOWNLOAD_DIR))
        self.download_format = StringVar(value="bv*+ba/b")
        self.download_container = StringVar(value="mp4")
        self.download_cookies = StringVar()
        self.download_browser = StringVar()
        self.download_proxy = StringVar()
        self.download_limit_rate = StringVar()
        self.download_filter_furina = BooleanVar(value=False)
        self.download_write_subs = BooleanVar(value=False)

        self.srt_out_dir = StringVar()
        self.srt_model = StringVar(value="small")
        self.srt_language = StringVar(value="zh")
        self.srt_device = StringVar(value="cpu")
        self.srt_compute_type = StringVar(value="auto")
        self.srt_beam_size = StringVar(value="5")
        self.srt_recursive = BooleanVar(value=False)
        self.srt_overwrite = BooleanVar(value=False)
        self.srt_no_vad = BooleanVar(value=True)
        self.srt_allow_duplicate_openmp = BooleanVar(value=True)
        self.srt_initial_prompt = StringVar()
        self.srt_drop_status = StringVar(value=self._initial_drop_status())

        self._build_ui()
        self._poll_log_queue()

    def _initial_drop_status(self) -> str:
        if DND_FILES is not None and hasattr(self.root, "drop_target_register"):
            return "可拖动文件/目录到左侧区域"
        return "拖动添加需安装：python -m pip install tkinterdnd2"

    def _build_ui(self) -> None:
        root_frame = ttk.Frame(self.root, padding=10)
        root_frame.pack(fill=BOTH, expand=True)

        notebook = ttk.Notebook(root_frame)
        notebook.pack(fill=BOTH, expand=True)

        self.download_tab = ttk.Frame(notebook, padding=10)
        self.srt_tab = ttk.Frame(notebook, padding=10)
        notebook.add(self.download_tab, text="PV 下载")
        notebook.add(self.srt_tab, text="生成 SRT")

        self._build_download_tab(self.download_tab)
        self._build_srt_tab(self.srt_tab)

        log_frame = ttk.LabelFrame(root_frame, text="运行日志", padding=8)
        log_frame.pack(fill=BOTH, expand=False, pady=(10, 0))
        self.log_text = Text(log_frame, height=11, wrap="word")
        self.log_text.pack(side=LEFT, fill=BOTH, expand=True)
        log_scroll = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        log_scroll.pack(side=RIGHT, fill=Y)
        self.log_text.configure(yscrollcommand=log_scroll.set)

        actions = ttk.Frame(root_frame)
        actions.pack(fill=X, pady=(8, 0))
        ttk.Button(actions, text="清空日志", command=self.clear_log).pack(side=LEFT)
        ttk.Button(actions, text="停止任务", command=self.stop_process).pack(side=RIGHT)

    def _build_download_tab(self, tab: ttk.Frame) -> None:
        url_frame = ttk.LabelFrame(tab, text="视频/帖子 URL", padding=8)
        url_frame.pack(fill=BOTH, expand=True)
        self.urls_text = Text(url_frame, height=9, wrap="word")
        self.urls_text.pack(side=LEFT, fill=BOTH, expand=True)
        url_scroll = ttk.Scrollbar(url_frame, command=self.urls_text.yview)
        url_scroll.pack(side=RIGHT, fill=Y)
        self.urls_text.configure(yscrollcommand=url_scroll.set)

        file_row = ttk.Frame(tab)
        file_row.pack(fill=X, pady=(8, 0))
        ttk.Label(file_row, text="URL 文件").pack(side=LEFT)
        ttk.Entry(file_row, textvariable=self.download_url_file).pack(side=LEFT, fill=X, expand=True, padx=8)
        ttk.Button(file_row, text="选择文件", command=self.choose_download_url_file).pack(side=LEFT)

        out_row = ttk.Frame(tab)
        out_row.pack(fill=X, pady=(8, 0))
        ttk.Label(out_row, text="下载目录").pack(side=LEFT)
        ttk.Entry(out_row, textvariable=self.download_out_dir).pack(side=LEFT, fill=X, expand=True, padx=8)
        ttk.Button(out_row, text="选择目录", command=self.choose_download_out_dir).pack(side=LEFT)
        ttk.Button(out_row, text="打开目录", command=lambda: self.open_directory(self.download_out_dir.get())).pack(side=LEFT, padx=(6, 0))

        options = ttk.LabelFrame(tab, text="下载参数", padding=8)
        options.pack(fill=X, pady=(8, 0))
        self._grid_labeled_entry(options, "格式", self.download_format, 0, 0)
        self._grid_combo(options, "容器", self.download_container, ["mp4", "mkv", "webm"], 0, 2)
        self._grid_labeled_entry(options, "Cookie 文件", self.download_cookies, 1, 0, button=("选择文件", self.choose_download_cookies))
        self._grid_combo(options, "浏览器 Cookie", self.download_browser, ["", "chrome", "edge", "firefox"], 1, 3)
        self._grid_labeled_entry(options, "代理", self.download_proxy, 2, 0)
        self._grid_labeled_entry(options, "限速", self.download_limit_rate, 2, 2)
        ttk.Checkbutton(options, text="按芙宁娜关键词过滤", variable=self.download_filter_furina).grid(row=3, column=0, sticky="w", pady=(8, 0))
        ttk.Checkbutton(options, text="下载字幕", variable=self.download_write_subs).grid(row=3, column=1, sticky="w", pady=(8, 0))

        buttons = ttk.Frame(tab)
        buttons.pack(fill=X, pady=(10, 0))
        ttk.Button(buttons, text="检查命令", command=lambda: self.run_download(dry_run=True)).pack(side=LEFT)
        ttk.Button(buttons, text="开始下载", command=lambda: self.run_download(dry_run=False)).pack(side=RIGHT)

    def _build_srt_tab(self, tab: ttk.Frame) -> None:
        input_frame = ttk.LabelFrame(tab, text="音频/视频输入", padding=8)
        input_frame.pack(fill=BOTH, expand=True)

        list_frame = ttk.Frame(input_frame)
        list_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.srt_inputs = Text(list_frame, height=9, wrap="none")
        self.srt_inputs.pack(side=LEFT, fill=BOTH, expand=True)
        input_scroll = ttk.Scrollbar(list_frame, command=self.srt_inputs.yview)
        input_scroll.pack(side=RIGHT, fill=Y)
        self.srt_inputs.configure(yscrollcommand=input_scroll.set)
        self._setup_srt_drop_target(self.srt_inputs)

        input_buttons = ttk.Frame(input_frame)
        input_buttons.pack(side=RIGHT, fill=Y, padx=(8, 0))
        ttk.Button(input_buttons, text="添加文件", command=self.choose_srt_files).pack(fill=X)
        ttk.Button(input_buttons, text="添加目录", command=self.choose_srt_directory).pack(fill=X, pady=(6, 0))
        ttk.Button(input_buttons, text="清空", command=lambda: self.srt_inputs.delete("1.0", END)).pack(fill=X, pady=(6, 0))
        ttk.Label(input_buttons, textvariable=self.srt_drop_status, wraplength=110).pack(fill=X, pady=(12, 0))

        out_row = ttk.Frame(tab)
        out_row.pack(fill=X, pady=(8, 0))
        ttk.Label(out_row, text="输出目录").pack(side=LEFT)
        ttk.Entry(out_row, textvariable=self.srt_out_dir).pack(side=LEFT, fill=X, expand=True, padx=8)
        ttk.Button(out_row, text="选择目录", command=self.choose_srt_out_dir).pack(side=LEFT)
        ttk.Button(out_row, text="打开目录", command=self.open_srt_output_directory).pack(side=LEFT, padx=(6, 0))

        options = ttk.LabelFrame(tab, text="识别参数", padding=8)
        options.pack(fill=X, pady=(8, 0))
        self._grid_combo(options, "模型", self.srt_model, ["tiny", "base", "small", "medium", "large-v3"], 0, 0)
        self._grid_combo(options, "语言", self.srt_language, ["zh", "en", "auto"], 0, 2)
        self._grid_combo(options, "设备", self.srt_device, ["auto", "cpu", "cuda"], 1, 0)
        self._grid_combo(options, "计算类型", self.srt_compute_type, ["auto", "int8", "float16", "int8_float16"], 1, 2)
        self._grid_labeled_entry(options, "Beam", self.srt_beam_size, 2, 0)
        self._grid_labeled_entry(options, "提示词", self.srt_initial_prompt, 2, 2)
        ttk.Checkbutton(options, text="递归扫描目录", variable=self.srt_recursive).grid(row=3, column=0, sticky="w", pady=(8, 0))
        ttk.Checkbutton(options, text="覆盖已有 SRT", variable=self.srt_overwrite).grid(row=3, column=1, sticky="w", pady=(8, 0))
        ttk.Checkbutton(options, text="关闭静音过滤", variable=self.srt_no_vad).grid(row=3, column=2, sticky="w", pady=(8, 0))
        ttk.Checkbutton(options, text="OpenMP 兼容模式", variable=self.srt_allow_duplicate_openmp).grid(row=3, column=3, sticky="w", pady=(8, 0))

        buttons = ttk.Frame(tab)
        buttons.pack(fill=X, pady=(10, 0))
        ttk.Button(buttons, text="生成 SRT", command=self.run_srt).pack(side=RIGHT)

    def _grid_labeled_entry(
        self,
        parent: ttk.Frame,
        label: str,
        variable: StringVar,
        row: int,
        column: int,
        button: tuple[str, object] | None = None,
    ) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=column, sticky="w", padx=(0, 6), pady=4)
        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=column + 1, sticky="ew", padx=(0, 12), pady=4)
        parent.columnconfigure(column + 1, weight=1)
        if button:
            text, command = button
            ttk.Button(parent, text=text, command=command).grid(row=row, column=column + 2, sticky="e", pady=4)

    def _grid_combo(self, parent: ttk.Frame, label: str, variable: StringVar, values: list[str], row: int, column: int) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=column, sticky="w", padx=(0, 6), pady=4)
        combo = ttk.Combobox(parent, textvariable=variable, values=values, width=18)
        combo.grid(row=row, column=column + 1, sticky="ew", padx=(0, 12), pady=4)
        parent.columnconfigure(column + 1, weight=1)

    def choose_download_url_file(self) -> None:
        path = filedialog.askopenfilename(title="选择 URL 文件", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            self.download_url_file.set(path)

    def choose_download_out_dir(self) -> None:
        path = filedialog.askdirectory(title="选择下载目录")
        if path:
            self.download_out_dir.set(path)

    def choose_download_cookies(self) -> None:
        path = filedialog.askopenfilename(title="选择 cookies.txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            self.download_cookies.set(path)

    def choose_srt_files(self) -> None:
        paths = filedialog.askopenfilenames(title="选择音频/视频文件", filetypes=MEDIA_FILETYPES)
        self._append_srt_inputs(paths)

    def choose_srt_directory(self) -> None:
        path = filedialog.askdirectory(title="选择音频/视频目录")
        if path:
            self._append_srt_inputs([path])

    def choose_srt_out_dir(self) -> None:
        path = filedialog.askdirectory(title="选择 SRT 输出目录")
        if path:
            self.srt_out_dir.set(path)

    def _append_srt_inputs(self, paths: Iterable[str]) -> None:
        existing = set(self._read_text_lines(self.srt_inputs))
        for path in paths:
            if path and path not in existing:
                self.srt_inputs.insert(END, f"{path}\n")
                existing.add(path)

    def _setup_srt_drop_target(self, widget: Text) -> None:
        if DND_FILES is None or not hasattr(widget, "drop_target_register"):
            return

        widget.drop_target_register(DND_FILES)
        widget.dnd_bind("<<Drop>>", self._handle_srt_drop)

    def _handle_srt_drop(self, event: object) -> str:
        data = getattr(event, "data", "")
        if not data:
            return "break"

        paths = [path for path in self.root.tk.splitlist(data) if path]
        self._append_srt_inputs(paths)
        self.log(f"已拖动添加 {len(paths)} 个输入。\n")
        return "break"

    def run_download(self, dry_run: bool) -> None:
        urls = self._read_text_lines(self.urls_text)
        url_file = self.download_url_file.get().strip()
        if not urls and not url_file:
            messagebox.showwarning("缺少输入", "请粘贴 URL，或选择一个 URL 文件。")
            return

        command = [sys.executable, str(DOWNLOAD_SCRIPT)]
        if url_file:
            command.extend(["--url-file", url_file])
        out_dir = self.download_out_dir.get().strip()
        if out_dir:
            command.extend(["--out-dir", out_dir])
        if self.download_format.get().strip():
            command.extend(["--format", self.download_format.get().strip()])
        command.extend(["--merge-output-format", self.download_container.get().strip() or "mp4"])
        if self.download_cookies.get().strip():
            command.extend(["--cookies", self.download_cookies.get().strip()])
        if self.download_browser.get().strip():
            command.extend(["--cookies-from-browser", self.download_browser.get().strip()])
        if self.download_proxy.get().strip():
            command.extend(["--proxy", self.download_proxy.get().strip()])
        if self.download_limit_rate.get().strip():
            command.extend(["--limit-rate", self.download_limit_rate.get().strip()])
        if self.download_filter_furina.get():
            command.append("--filter-furina")
        if self.download_write_subs.get():
            command.append("--write-subs")
        if dry_run:
            command.append("--dry-run")
        command.extend(urls)

        self.run_command(command)

    def run_srt(self) -> None:
        inputs = self._read_text_lines(self.srt_inputs)
        if not inputs:
            messagebox.showwarning("缺少输入", "请添加音频/视频文件，或添加目录。")
            return

        command = [
            sys.executable,
            str(SRT_SCRIPT),
            *inputs,
            "--model",
            self.srt_model.get().strip() or "small",
            "--language",
            self.srt_language.get().strip() or "zh",
            "--device",
            self.srt_device.get().strip() or "auto",
        ]
        if self.srt_compute_type.get().strip() and self.srt_compute_type.get().strip() != "auto":
            command.extend(["--compute-type", self.srt_compute_type.get().strip()])
        if self.srt_beam_size.get().strip():
            command.extend(["--beam-size", self.srt_beam_size.get().strip()])
        if self.srt_out_dir.get().strip():
            command.extend(["--out-dir", self.srt_out_dir.get().strip()])
        if self.srt_recursive.get():
            command.append("--recursive")
        if self.srt_overwrite.get():
            command.append("--overwrite")
        if self.srt_no_vad.get():
            command.append("--no-vad")
        if self.srt_allow_duplicate_openmp.get():
            command.append("--allow-duplicate-openmp")
        if self.srt_initial_prompt.get().strip():
            command.extend(["--initial-prompt", self.srt_initial_prompt.get().strip()])

        self.run_command(command)

    def run_command(self, command: list[str]) -> None:
        if self.process and self.process.poll() is None:
            messagebox.showwarning("任务运行中", "当前已有任务在运行，请先停止或等待完成。")
            return

        self.log(f"> {subprocess.list2cmdline(command)}\n")
        self.worker = threading.Thread(target=self._run_process_worker, args=(command,), daemon=True)
        self.worker.start()

    def _run_process_worker(self, command: list[str]) -> None:
        try:
            self.process = subprocess.Popen(
                command,
                cwd=str(REPO_ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                bufsize=1,
            )
        except OSError as exc:
            self.log_queue.put((f"启动失败：{exc}\n", None))
            return

        assert self.process.stdout is not None
        for line in self.process.stdout:
            self.log_queue.put((line, None))

        return_code = self.process.wait()
        self.log_queue.put((f"\n任务结束，退出码：{return_code}\n", None))
        self.process = None

    def stop_process(self) -> None:
        if not self.process or self.process.poll() is not None:
            self.log("没有正在运行的任务。\n")
            return
        self.process.terminate()
        self.log("已请求停止当前任务。\n")

    def open_srt_output_directory(self) -> None:
        out_dir = self.srt_out_dir.get().strip()
        if out_dir:
            self.open_directory(out_dir)
            return

        inputs = self._read_text_lines(self.srt_inputs)
        if inputs:
            first = Path(inputs[0])
            directory = first if first.is_dir() else first.parent
            self.open_directory(str(directory))
            return

        messagebox.showwarning("缺少目录", "请先选择输出目录，或添加一个输入文件。")

    def open_directory(self, path: str) -> None:
        directory = Path(path.strip() or ".").expanduser()
        if not directory.exists():
            create = messagebox.askyesno("目录不存在", f"目录不存在，是否创建？\n{directory}")
            if not create:
                return
            directory.mkdir(parents=True, exist_ok=True)

        try:
            os.startfile(str(directory))  # type: ignore[attr-defined]
        except OSError as exc:
            messagebox.showerror("打开失败", str(exc))

    def log(self, text: str) -> None:
        self.log_text.insert(END, text)
        self.log_text.see(END)

    def clear_log(self) -> None:
        self.log_text.delete("1.0", END)

    def _poll_log_queue(self) -> None:
        while True:
            try:
                text, _ = self.log_queue.get_nowait()
            except queue.Empty:
                break
            self.log(text)
        self.root.after(100, self._poll_log_queue)

    @staticmethod
    def _read_text_lines(widget: Text) -> list[str]:
        return [line.strip() for line in widget.get("1.0", END).splitlines() if line.strip()]


def main() -> int:
    root = TkinterDnD.Tk() if TkinterDnD is not None else Tk()
    app = MediaToolApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
