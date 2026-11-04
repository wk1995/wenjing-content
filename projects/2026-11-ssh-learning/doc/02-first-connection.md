---
status: draft
updated: 2026-11-04
level: beginner
---

# 02 不买服务器完成第一次连接

目标是在家里的 Mac 上完成一次“开启服务 → 核对身份 → 登录 → 执行命令 → 退出”的过程。先用 Mac 连接自己；之后再用同一家庭网络里的 Windows 连接这台 Mac。

下面涉及设置的操作由你手动完成。公司 Mac 先用于阅读和客户端练习，需要修改公司设备设置时遵循公司的管理要求。

第一次完成路线 A 就可以继续读第三篇。路线 B 是有两台设备时的选做练习；若上一回练习后关闭了“远程登录”，下一次连接前先重新开启。

## 路线 A 用一台 Mac 连接自己

### 1 确认你在自己的 Mac 终端

打开终端，执行：

```bash
sw_vers
ssh -V
whoami
```

`sw_vers` 显示 macOS 版本，`whoami` 显示当前账号短名称。它可能和登录界面上的中文姓名不同。

### 2 开启接收连接的服务

在较新 macOS 中，进入：

```text
系统设置 → 通用 → 共享 → 远程登录
```

打开“远程登录”，访问范围选择“仅这些用户”，添加你要用于练习的当前账号。这一步可能需要管理员权限。

本练习只访问自己的主目录，不需要额外打开“允许远程用户完全访问磁盘”。系统版本不同，入口文字和布局可能不同，可在系统设置里搜索“远程登录”。

打开后，这台 Mac 会开始接收符合系统与网络策略的 SSH 连接，包括可能来自局域网其他设备的连接；访问范围中的账号限制仍然生效。

### 3 在本机查看主机公钥指纹

在原来的本机终端执行：

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

这读取的是主机**公钥**文件，显示结果通常包含算法、位数和 `SHA256:...` 指纹。记下指纹，下一步核对。

若文件不存在，先检查远程登录是否已开启；如果连接提示使用的是其他主机密钥算法，应核对相应的 `.pub` 公钥文件。例如提示 ECDSA 或 RSA 时，分别查看：

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ecdsa_key.pub
ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub
```

只有系统实际存在对应文件时才能读取。指纹是公钥的摘要，比较时要核对提示的算法以及完整的 `SHA256:...` 字符串。不要把自己的用户公钥指纹拿来与主机指纹比较，也不要为了读私钥而加 `sudo`。

### 4 发起连接

仍然在本机终端执行：

```bash
ssh "$(whoami)"@127.0.0.1
```

这里有两个新写法：

- `$(whoami)`：先执行 `whoami`，把输出的账号名填进命令。
- `127.0.0.1`：回环地址，表示“正在执行命令的这台电脑自己”。

初次连接可能提示无法确认主机身份，并显示指纹。把它与上一步结果核对；算法与指纹一致后，输入 `yes` 并回车。若已存有匹配的可信主机记录，可能不会再次询问。

随后如果提示输入账号密码，输入**这台 Mac 上该账号的登录密码**。密码输入时终端通常不显示字符或星号，这是正常现象；输入完直接回车。这里不是让你输入 Apple 账号密码。

如果出现 `Permission denied`，到[排错手册](08-troubleshooting.md)查看，不要反复猜密码。

### 5 执行三个只读命令

登录成功后执行：

```bash
whoami
hostname
pwd
```

因为你连接的就是自己，账号名、主机名可能和登录前相同。这不是连接失败。重点是经历了 SSH 的身份核对和登录过程，并且没有出现连接失败信息。

想更直观地确认当前 SSH 会话，可以在**登录后**运行：

```bash
printenv SSH_CONNECTION
```

通常会输出四项：客户端地址、客户端临时端口、服务端地址、服务端端口。示意输出如下，不能把它当成命令执行：

```text
127.0.0.1 54321 127.0.0.1 22
```

`54321` 只是虚构的客户端临时端口，不要求和你的相同。这个环境变量由 SSH 会话设置；新开的未登录 SSH 的本机终端通常没有这项值。它帮助你确认会话环境，不替代前面的主机身份核对。

以后连接另一台电脑时，`hostname` 会帮助你区分两端。提示符的样式由 Shell 配置决定，不能只靠颜色判断。

### 6 退出

```bash
exit
```

正常情况下会看到连接关闭，回到原来的本机终端。不要把关闭终端窗口当成退出所有远程任务的通用方法，长任务的处理见[安全与运维](06-security-and-operations.md)。

## 路线 B 用家里的 Windows 连接 Mac

先完成路线 A，再让 Mac 和 Windows 连到同一个家庭局域网。这里不需要改路由器端口映射。

### 1 在目标 Mac 查清账号与地址

账号用 Mac 终端里的 `whoami` 结果。IP 地址可在系统设置中查看当前 Wi-Fi 或以太网的网络详情；也可以查看“远程登录”页面提供的登录命令。

若要在网络详情中找地址，选择实际正在使用的 Wi-Fi 或以太网接口，查看其 TCP/IP 或 IP 地址信息。多网卡时先选与 Windows 所在网络对应的接口，不需要猜固定的网卡名。

假设查到账号为 `alice`，当前地址为 `192.168.1.50`。这两个值只是示例，你必须换成实际值。Mac 换网络或路由器重新分配地址后，IP 可能改变。

### 2 在 Windows 检查客户端

打开 PowerShell，执行：

```powershell
ssh -V
```

如果找不到 `ssh`，在支持的 Windows 10/11 系统“可选功能”中查找并安装 **OpenSSH 客户端**。界面入口随版本有所不同，可以在设置中搜索“可选功能”。仅发起连接不需要安装 OpenSSH 服务端。

具体安装方法见[微软入门文档](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)。

### 3 发起登录并核对指纹

在 Windows PowerShell 执行，先替换账号与 IP：

```powershell
ssh alice@192.168.1.50
```

首次登录时，与目标 Mac 上查到的主机公钥指纹核对；一致后再接受，随后按提示完成认证。

这里填的是目标 Mac 的短账号名；Windows 本地 `whoami` 可能显示成 `电脑名\账号`，不要把它直接当成 Mac 的登录账号。密码提示要求的也是目标 Mac 账号密码。

**在 Windows 输入 `127.0.0.1`，目标会是 Windows 自己。** 它不会自动指向家里的 Mac。

### 4 确认命令现在运行在哪里

登录成功后输入：

```bash
sw_vers
pwd
```

你是在 Windows 的窗口里输入，但运行的是目标 Mac 的命令，因此可以得到 macOS 信息。执行 `exit` 后，才回到本机 PowerShell。

如果超时：先看 Mac 是否开机且未睡眠、地址是否正确，两台设备是否在访客网络或被无线隔离。连接同一个 Wi-Fi 名称不保证设备间一定可通信。

## 练习后怎样恢复

如果暂时不继续练习，在 Mac 的“系统设置 → 通用 → 共享”中关闭“远程登录”。这会停止后续 SSH 登录入口；以后继续练习时再开启。

本章不要求修改服务端配置文件、安装第三方客户端或将家里的 SSH 服务暴露到公网。

## 自测

1. Windows 连接 Mac，需要知道的是 Windows 账号还是 Mac 账号？
2. 在两台不同电脑上执行 `ssh alice@127.0.0.1`，目标会一样吗？
3. 登录成功后，在 Windows 窗口里输入 `sw_vers`，由谁执行？

答案：1. Mac 上允许登录的账号。2. 不同，分别指向执行命令的那台电脑。3. 目标 Mac。

完成标准：路线 A 能核对主机身份、完成登录、查看 SSH_CONNECTION 并用 exit 返回本机。跨设备练习还应确认 Windows 登录后能读取目标 Mac 的 macOS 信息。

## 参考资料

- [苹果远程登录指南](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)。
- [OpenSSH ssh-keygen 手册](https://man.openbsd.org/ssh-keygen)：读取公钥指纹。
- [OpenSSH ssh 手册](https://man.openbsd.org/ssh)：SSH_CONNECTION 的四个字段。
- [微软 OpenSSH 入门](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)。

上一篇：[01 从零认识 SSH](01-foundations.md)。下一篇：[03 密码 公钥与私钥](03-key-authentication.md)。返回[学习导航](../README.md)。
