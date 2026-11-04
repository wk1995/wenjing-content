---
status: draft
updated: 2026-11-04
level: practical
---

# 04 连接别名与文件传输

学会登录后，最常见的两个需求是：少输入一长串连接参数，以及在两端之间传文件。本篇沿用家里 Mac 的自连接环境；完成[密钥练习](03-key-authentication.md)后再做。

本篇命令默认在**本机 Mac 终端**执行。若刚才仍登录在 SSH 会话里，先用 `exit` 回到本机；文件传输命令也从本机发起。

## 连接设置放在哪个文件

| 文件或入口 | 谁使用 | 修改后影响什么 |
| --- | --- | --- |
| Mac/Linux 客户端 `~/.ssh/config` | 发起连接的 ssh、scp、sftp 等客户端 | 这台客户端之后发起的新连接 |
| Windows 客户端 `$HOME\.ssh\config` | Windows OpenSSH 客户端 | Windows 之后发起的新连接，文件不带 .txt 后缀 |
| Unix 风格服务端的 `/etc/ssh/sshd_config` 及其包含文件 | 接收连接的 SSH 服务 | 服务端监听、认证和转发等策略，生效方式依系统而定 |
| Mac 的“远程登录”设置 | macOS 管理接收登录的入口 | 是否开启远程登录、允许哪些账号 |

本篇只编辑客户端的 `config`。保存后重新发起连接即可读取新设置，不需要因此重启服务端，也不会改变已经建立的会话。

## 给连接起一个名字

客户端可以从 `~/.ssh/config` 读取连接设置。这个文件影响发起连接的客户端，不会替你开启服务端，也不会授予新权限。

先用文本编辑器查看是否已有文件。若已存在，在保留原内容的前提下添加下面这个配置块，放在宽泛的 `Host *` 默认配置之前；如果已经有同名 `Host ssh-lab`，先检查并修改原块，避免重复。

如果还不熟悉编辑隐藏文件，可以在本机 Mac 终端执行：

```bash
nano ~/.ssh/config
```

这会打开终端内的文字编辑器；文件不存在时，可以在里面创建内容。下面的配置填好后，按 `Control + O` 保存，回车确认文件名，再按 `Control + X` 退出。这里是 Control 键，不是 Command 键。若 `nano` 不可用，换用支持纯文本的编辑器，并确认文件没有被保存成富文本或 `config.txt`。

```sshconfig
Host ssh-lab
    HostName 127.0.0.1
    User alice
    Port 22
    IdentityFile ~/.ssh/id_ed25519_ssh_learning
    IdentitiesOnly yes
```

**将 `User alice` 中的 `alice` 替换为本机 `whoami` 显示的短账号名。** 这段配置内容应写入文件，不是在 Shell 中逐行执行的命令。

| 配置项 | 含义 |
| --- | --- |
| `Host ssh-lab` | 你在命令行使用的别名 |
| `HostName` | 真正连接的地址 |
| `User` | 目标账号 |
| `Port` | 服务端端口 |
| `IdentityFile` | 使用的用户私钥文件 |
| `IdentitiesOnly` | 限制使用的认证身份 |

在 Mac 本机终端设置文件权限并检查最终配置：

```bash
chmod 600 ~/.ssh/config
ssh -G ssh-lab
```

`ssh -G` 会输出解析后的配置，本命令不发起登录。重点查看 `hostname`、`user`、`port` 和 `identityfile`；输出里还有很多默认项，不必全部理解。

确认后登录：

```bash
ssh ssh-lab
```

退出后还可以执行一条远程命令：

```bash
ssh ssh-lab hostname
```

这里登录后只执行 `hostname`，完成后结束会话，通常不会进入持续等待输入的交互式 Shell。

## 把别名用于另一台机器

如果将来从其他电脑连接家里的 Mac，需要在**那台客户端**建立配置，将 `HostName` 改成目标 Mac 实际可达的地址，并使用那台客户端自己的密钥。

在 Windows OpenSSH 客户端中，个人配置通常位于 `$HOME\.ssh\config`。这个文件名没有 `.txt` 后缀。不要将上面绑定 `127.0.0.1` 的练习配置原样搬过去，就期待它连接家里的 Mac。

若要在 Windows 编辑个人配置，可在本机 PowerShell 执行 `notepad "$HOME\.ssh\config"`，按需新建并保存为纯文本。先检查目录是否已按第三篇创建，保存后确认实际文件名确实是 `config`。登录目标 Mac 时，`User` 填 Mac 账号，`IdentityFile` 使用第三篇在 Windows 生成的私钥路径。

例如配置项可写成 `IdentityFile ~/.ssh/id_ed25519_ssh_learning_windows`，这里的 `~` 由 OpenSSH 按 Windows 当前用户的主目录解析。PowerShell 命令中的 `$HOME` 是另一种语法，不要把整条 PowerShell 命令当成配置项写入文件。

## 文件传输先分清方向

`scp` 常见格式：

```text
scp 来源 目的地
```

路径中含 `主机别名:`，表示这一端是通过 SSH 访问的远程端。上传是本地到远程，下载是远程到本地。

### 1 创建独立练习目录

在本机 Mac 终端执行：

```bash
mkdir -p ~/ssh-learning-files
cd ~/ssh-learning-files
```

用文本编辑器在该目录新建 `hello.txt`，写入一行 `Hello SSH`。如果目录或文件已存在，先检查内容，再决定是否复用。

也可以沿用刚才的编辑器：

```bash
nano hello.txt
```

输入内容后，同样按 `Control + O`、回车、`Control + X` 保存并退出。

### 2 上传

仍在本机终端、上述目录内执行：

```bash
scp hello.txt ssh-lab:ssh-learning-upload.txt
```

这把本地 `hello.txt` 传到远程账号主目录下的 `ssh-learning-upload.txt`。目标文件若同名会被覆盖，练习前确认没有要保留的同名文件。

因为本章连接的是自己，目标实际上还是这台 Mac，只是路径不同。以后连其他机器时，文件才真正跨机器传输。

### 3 下载

```bash
scp ssh-lab:ssh-learning-upload.txt ./downloaded-hello.txt
```

这将远程文件下载到本地当前目录，并换名为 `downloaded-hello.txt`。用文本编辑器打开，检查是否是你写入的那一行。

这里 `ssh-lab:文件名` 的远程相对路径按目标账号主目录理解，`./文件名` 按本机当前目录理解。上传后不会因为你之前在另一场 SSH 会话里执行过 `cd`，就自动传到那个会话的目录。

有空格的本地文件名要整体加引号。例如已在当前目录准备好 `hello world.txt` 后，可以这样上传：

```bash
scp "./hello world.txt" ssh-lab:ssh-learning-space-upload.txt
```

这只是可选示例，先确认目标没有要保留的同名文件。下载时本地目标若已存在，同样可能被覆盖。

### 4 端口参数大小写

| 工具 | 指定端口的参数 |
| --- | --- |
| `ssh` | 小写 `-p` |
| `scp` | 大写 `-P` |
| `sftp` | 大写 `-P` |

连接别名已经配置 `Port` 后，这些工具通常可以直接复用，不需要再写端口。

当前上游 OpenSSH 的 `scp` 默认通过 SFTP 协议传输；较老客户端行为可能不同。不要为了模仿旧教程就随意加 `-O` 切回旧 SCP 协议，遇到兼容性问题再按版本排查。

## 文件多时可以使用 SFTP

在本机 Mac 终端执行：

```bash
sftp ssh-lab
```

连接后进入的是 SFTP 命令环境，下面的命令不是通用 Shell 命令：

```text
pwd
lpwd
ls
lls
bye
```

| 命令 | 含义 |
| --- | --- |
| `pwd` / `ls` | 查看远程目录 / 文件 |
| `lpwd` / `lls` | 查看本地目录 / 文件，l 表示 local |
| `cd` / `lcd` | 切换远程 / 本地目录 |
| `put 本地文件` | 上传文件 |
| `get 远程文件` | 下载文件 |
| `bye` | 退出 SFTP |

带空格的路径需要按所用工具的规则加引号。先用本篇的英文无空格文件名练熟方向，再处理复杂路径。

## 自测

1. 配置 `Host home-mac` 会自动让家里的电脑可以从公网访问吗？
2. `scp report.txt ssh-lab:report.txt` 是上传还是下载？
3. `sftp` 里的 `lpwd` 查看哪一端？

答案：1. 不会，它只是客户端配置。2. 上传。3. 本地端。

完成标准：`ssh ssh-lab` 可以登录；上传和下载后，下载文件包含原先写下的文字。只完成了登录还不算验证文件传输。

## 参考资料

- [ssh_config 手册](https://man.openbsd.org/ssh_config)：连接别名、配置匹配与选项。
- [scp 手册](https://man.openbsd.org/scp)和 [sftp 手册](https://man.openbsd.org/sftp)：传输方向、参数和交互命令。
- [微软 Windows OpenSSH 配置](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-server-configuration)：Windows 用户配置位置。

上一篇：[03 密码 公钥与私钥](03-key-authentication.md)。下一篇：[05 网络与 SSH 隧道](05-network-and-tunnels.md)。返回[学习导航](../README.md)。
