---
template: project/research/post-reinstall-check
template_version: 2026-10-24
status: done
---

# 重装后的复查记录（2026-10-24）

2026-10-17 那次排查结束时，注入和对外连接还在。10 月 18 日做过一轮清理，但记录显示清理后又被重建。10 月 23 日这台机器全新安装 Windows，10 月 24 日晚按当时锁定的 IOC 做了一次复查。

## 复查对象

- 机器：同一台 Windows 台式机（不是新设备）
- 系统：2026-10-23 全新安装 Windows 10 22H2，UBR 3803
- 复查时间：2026-10-24 23:13–23:20（GMT+8）
- 复查方式：只读枚举 + 一次剪贴板行为复现；没有执行任何清理动作

## 复查指标与结果

指标取自 10 月 17–18 日对话中已经确认的结论，不新增假设。

| 指标 | 来源 | 本次结果 |
| --- | --- | --- |
| `\Microsoft\Windows\Application Experience\Diagnostics` / `Diagnostics2` | 伪装计划任务，2026-05-10 创建 | 不存在。该目录只剩 5 个正常任务：MareBackup、Microsoft Compatibility Appraiser、PcaPatchDbTask、ProgramDataUpdater、StartupAppTask |
| `AppData\Roaming\comain_ev2c34` / `comain_ev2f79` | 随机名载荷目录 | 不存在。Roaming 下也没有随机名目录；近 30 天新建的目录为 NVIDIA、Tencent、Atlassian、Adobe、GitHub CLI、Oray、AweSun、SNDA、clash_win、Microsoft |
| `UserAccountBroker.exe` 被注入 | 内存注入宿主 | 该进程当前未运行；全系统没有进程加载 `AppData` / `ProgramData` / `Temp` 下的可疑 DLL，命中的都是 OneDrive、PowerToys、微信插件、Clash 一类正常注入 |
| Defender 排除项 | 当时排除了 `C:\`、`C:\Users\wk\AppData\Local`、`D:\`、`F:\`，是它能存活的前提 | 排除列表为空。实时防护开启，特征库 1.461.171.0（2026-10-24 更新），当天 22:46 完成快速扫描 |
| C2 `47.84.66.208:8852` | 注入进程的外联 | 无任何连接 |
| 安装来源 `i4Tools_yyytt_510633.msi` | 2026-04-20 的第三方安装包 | 卸载登记无 i4Tools／爱思／助手类条目；`Downloads` 无该安装包；C 盘用户目录搜 `ev2c34`、`ev2f79`、`i4Tools` 无匹配 |
| 其他持久化 | 自启动与服务的横向检查 | Run 键、启动文件夹、指向用户目录的服务均无可疑项 |

## 行为复现

静态检查只能证明文件不在，所以补了一次和当时同形状的复制测试。

- 方法：生成 `hlg_` + 48 位十六进制随机 token，写入剪贴板，等待 1200 ms 后读回，与写入值逐字节比对，重复三轮
- 结果：3/3 完全一致，长度与内容均未变化
- 副作用处理：测试前备份原剪贴板文本，结束后已还原

当时的现象是复制后几百毫秒内被替换成另一串，这个延迟窗口被完整覆盖。

## 一条需要单独说明的检测

复查期间 Defender 有 2 条 `Trojan:Win32/ClickFix.HHI!MTB` 记录（2026-10-24 15:03:54、14:57:49，ThreatID 2147950086，严重级别 5，处置成功）。

它的资源字段是命令行，内容是 WorkBuddy 自身 safe-delete 包装器的 powershell 调用；两条记录的 `DidThreatExecute` 均为 `False`，威胁状态为非活跃。判断为启发式误报：ClickFix 规则匹配的是长命令行加剪贴板操作，恰好撞上工具自身的实现。这项不作为感染证据，也不写进成稿。

## 结论与表述边界

可以写的：重装后按原 IOC 复查，未发现残留，复制改写也未复现。

不能写的：清理成功、已经修复、原清理步骤有效。理由是复查对象是 10 月 23 日新装的系统，原失陷环境已经不在这台机器上；这次复查没有验证 10 月 18 日那轮清理动作的效果，也没有回答「不重装能不能治好」。

未覆盖的部分：

- 其他机器是否中招（对话当时就没有回答，现在依然没有）
- 内核层／bootkit 级持久化（本次只做用户态枚举，没做离线取证）
- 浏览器下载记录的回查（没有重新打开 `6x.org` 那条短链）

## 对成稿的影响

`README.md` 复盘里原来写的是「若用户补上清理后的复测结果，再把修复从建议改成已验证结果」。这个条件现在满足了一半：可以补一句「重装后复查未复现」，但不能把整篇的「修复建议」升级成「已验证修复」。公众号、抖音、视频号的既有表述不需要改。
