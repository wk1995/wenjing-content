---
status: draft
updated: 2026-11-04
level: practical
---

# 03 密码 公钥与私钥

完成第一次密码登录后，你会遇到“生成 SSH key”“把公钥放到服务器”“用私钥登录”等说法。这一篇解释它们，并用家里的 Mac 自连接环境完成一次公钥认证。

## 先区分三个秘密和两个身份

| 名称 | 用于什么 | 放在哪里 |
| --- | --- | --- |
| 账号密码 | 向服务端证明你能登录该账号 | 你记住它；密码认证发生在加密连接中 |
| 用户私钥 | 客户端用它完成签名，证明自己持有相应私钥 | 你的客户端，不能上传给别人 |
| 私钥口令 passphrase | 加密保护磁盘上的私钥文件 | 你记住它；不是服务端账号密码 |
| 用户公钥 | 服务端验证客户端的签名 | 配置到允许登录的目标账号下 |
| 主机公钥 | 客户端识别目标主机 | 客户端核对后通常记入 `known_hosts` |

服务端还有自己的主机私钥，由服务端保存。不要把“主机用的密钥”和“用户登录用的密钥”混为一谈。

## 公钥认证怎样证明你是你

可以先用“钥匙和登记名册”帮助理解：服务端保存允许登录的公钥，客户端持有相应私钥。实际工作时，客户端对认证相关数据做数字签名，服务端用公钥检查签名。

私钥不会在登录时发送给服务器。公钥认证也不是把登录密码自动填进去。

两者都在 SSH 加密连接中进行。使用公钥认证以后，最终能访问哪些文件，仍受目标账号权限控制。

## 认识 `.ssh` 中的文件

在 Mac/Linux 上，`~` 表示当前账号的主目录，例如 `/Users/alice`。`.ssh` 前面的点表示它通常在文件管理器中隐藏。

| 文件 | 谁读取 | 用途 |
| --- | --- | --- |
| `~/.ssh/id_ed25519_ssh_learning` | 客户端 | 本教程新建的用户私钥 |
| `~/.ssh/id_ed25519_ssh_learning.pub` | 可复制到服务端 | 对应的用户公钥 |
| `~/.ssh/authorized_keys` | 服务端 | 允许登录本账号的公钥列表 |
| `~/.ssh/known_hosts` | 客户端 | 记录已接受的主机身份 |
| `~/.ssh/config` | 客户端 | 保存连接别名和选项 |

在两台机器的场景中，私钥放客户端，`authorized_keys` 放目标账号下。本章连接的是自己，所以两端文件恰好位于同一台 Mac 的同一账号中。

## 实操前提

- 已完成[第二篇的路线 A](02-first-connection.md#路线-a-用一台-mac-连接自己)，家里 Mac 的远程登录已开启，并允许当前账号；不要求先完成 Windows 练习。
- 从已有 SSH 会话 `exit` 退出，回到原来的**本机 Mac 终端**。
- 本章的命令使用 Mac Shell 语法，不要直接复制到 PowerShell。

### 1 检查是否已存在同名学习密钥

```bash
ls -la ~/.ssh
```

在列表里查找 `id_ed25519_ssh_learning` 和对应的 `.pub` 文件。如果提示 `.ssh` 目录不存在，可以在下一步创建；若提示没有访问权限，则先查权限，不要当成“文件不存在”。

如果已经存在，先确认是否就是之前生成的学习密钥；不要覆盖。需要重新练习时换一个新名字，并同步调整后续路径。

### 2 创建独立的学习密钥

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_ssh_learning -C "ssh-learning-mac"
```

- `-t ed25519`：选择密钥算法。本教程以支持该算法的常见 OpenSSH 环境为前提。
- `-f`：指定保存位置，避免与已有工作密钥重名。
- `-C`：添加备注，只用于辨认，不赋予登录权限。

按提示设置私钥口令，并再次输入确认。终端通常不显示输入内容。如果意外出现覆盖已有文件的询问，选择不覆盖并先检查。

生成后会得到私钥文件及对应的 `.pub` 公钥文件。

### 3 仅把公钥加入当前账号的授权列表

仍在本机 Mac 终端执行：

```bash
cat ~/.ssh/id_ed25519_ssh_learning.pub
```

确认查看的是以 `.pub` 结尾的文件。公钥通常是一整行，包含算法、编码内容和备注。

下面的命令将它**追加**到当前账号的授权列表，执行一次即可：

```bash
printf '\n' >> ~/.ssh/authorized_keys
cat ~/.ssh/id_ed25519_ssh_learning.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_ed25519_ssh_learning
```

`>>` 表示追加；`>` 表示覆盖。这里不要换成单个 `>`，否则可能抹掉已有授权列表。重复追加会产生重复记录，通常没有必要。

第一行先追加换行，避免原文件最后一行没有换行时，把新公钥粘到旧公钥后面。授权列表允许空行；一把公钥仍应完整占一行。

`700` 在这里表示目录仅自己可读、写和进入；`600` 表示文件仅自己可读写。这些是本练习采用的保守权限设置。账号归属和上层目录权限也可能影响服务端是否接受公钥。

### 4 强制用这把密钥测试

```bash
ssh -o IdentitiesOnly=yes -o PreferredAuthentications=publickey -i ~/.ssh/id_ed25519_ssh_learning "$(whoami)"@127.0.0.1
```

- `-i` 指定用户私钥。
- `IdentitiesOnly=yes` 限制尝试的身份，减少代理中其他密钥的干扰；已有配置仍可能指定其他身份文件。
- `PreferredAuthentications=publickey` 让这次测试只尝试公钥认证，避免失败后悄悄回退到账号密码。

首次使用时，可能询问：

```text
Enter passphrase for key ...
```

这时输入的是**刚才给私钥设置的口令**。如果密钥已被代理加载，也可能无需再次输入。

能登录则说明公钥认证成功；如果提示 `Permission denied (publickey)`，先检查目标账号、授权文件和权限，见[排错手册](08-troubleshooting.md)。登录后用 `exit` 返回本机。

## 为什么用了密钥还可能要输入口令

因为私钥口令保护的是本地私钥。它和服务端账号密码的作用不同。

`ssh-agent` 是在本机为客户端代做签名的代理。它可以在加载密钥后减少重复输入私钥口令的次数。先检查当前代理：

```bash
ssh-add -l
```

若能连接代理，再按需加载本章密钥：

```bash
ssh-add ~/.ssh/id_ed25519_ssh_learning
```

`The agent has no identities` 表示代理可连接，但当前没有加载身份；`Could not open a connection to your authentication agent` 表示当前环境无法连接代理。遇到后者可以先继续使用 `ssh -i`，不必为了完成练习立即配置代理。

代理生命周期和系统钥匙串集成随系统及配置而变化。这里不承诺重启后永久免输口令。

## 将来换成两台电脑时怎样做

每台客户端分别生成自己的密钥，把各自公钥添加到目标账号的授权列表。这样可以单独撤销某台设备的登录资格。

不要为了让 Windows 也能登录，就随意把 Mac 的私钥通过聊天工具发过去。Windows 上的路径与代理配置也需要按 Windows 环境处理。

### 选学 Windows 用自己的公钥登录家里 Mac

前提：已完成第二篇路线 B，Windows 可以用密码登录目标 Mac。本节按“Windows 保存私钥，Mac 保存授权公钥”操作，不需要 Windows 开启 SSH 服务端。

**第一步，在 Windows 本机 PowerShell 创建独立密钥。** 先退出已有 SSH 会话，确保当前是 PowerShell；创建 `.ssh` 目录后检查同名文件：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.ssh" | Out-Null
Get-ChildItem -Force "$HOME\.ssh"
```

若已有 `id_ed25519_ssh_learning_windows` 或同名 `.pub`，先检查是否可以复用，不要覆盖。确认没有同名学习密钥后运行：

```powershell
ssh-keygen -t ed25519 -f "$HOME\.ssh\id_ed25519_ssh_learning_windows" -C "ssh-learning-windows"
Get-Content "$HOME\.ssh\id_ed25519_ssh_learning_windows.pub"
```

按提示设置并确认私钥口令。复制 `Get-Content` 显示的完整公钥行：从 `ssh-ed25519` 开始，到末尾备注结束。窗口自动折行不代表公钥应分成多行。不要复制不带 `.pub` 的私钥文件。

**第二步，把这行公钥加到目标 Mac 账号下。** 在 Windows PowerShell 发起密码登录，先替换示例账号与地址：

```powershell
ssh alice@192.168.1.50
```

登录后窗口已进入 **Mac 的 Shell**。接下来输入的是 Mac 命令：

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

如果文件已有授权内容，先保留副本并保持原有行不变。用方向键移到末尾，必要时先回车另起一行，再粘贴刚才的完整公钥行，末尾再回车。按 `Control + O`、回车、`Control + X` 保存退出；这是 Control 键，不是 Command 键。若没有 nano，使用目标系统可用的纯文本编辑器完成同样的追加操作。

仍在目标 Mac 执行：

```bash
chmod 600 ~/.ssh/authorized_keys
exit
```

**第三步，回到 Windows 本机 PowerShell 验证。** 替换同一个目标账号和地址：

```powershell
ssh -o IdentitiesOnly=yes -o PreferredAuthentications=publickey -i "$HOME\.ssh\id_ed25519_ssh_learning_windows" alice@192.168.1.50
```

若询问 `Enter passphrase for key ...`，输入第一步设置的 Windows 私钥口令。成功后，可在目标 Mac 运行 `printenv SSH_CONNECTION`，看到客户端地址为 Windows 的地址；然后用 `exit` 退出。

这里目标是 Mac，因此授权文件在 Mac 账号主目录下。不要把 Windows **服务端**的管理员授权文件规则套到这个场景。[来源：微软 OpenSSH 密钥管理](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement)

## 怎样撤销本章授权

在目标账号的 `authorized_keys` 中，找到与本章 `.pub` 文件内容一致的那一行，备份后只删除该行；如果误追加了多次，要删除全部对应重复项。不要删除整份文件。

若密钥已加载到代理，可在本机执行：

```bash
ssh-add -d ~/.ssh/id_ed25519_ssh_learning.pub
```

从代理移除和从服务端撤销授权是两件事。私钥泄露后，重点是撤销各目标上的对应公钥授权，并创建新密钥；只修改旧私钥文件口令无法让已泄露的副本失效。

如果只是忘记了私钥口令，也不能用目标账号密码替它解锁。无法取回口令时，需要生成新密钥，通过仍可用的登录方式或本机入口重新授权，并撤销旧授权；不要覆盖唯一可用的密钥后再寻找退路。

## 自测

1. `known_hosts` 和 `authorized_keys` 各解决哪个方向的信任问题？
2. 把 `.pub` 文件放到自己任意一个文件夹里，就能登录别人的服务器吗？
3. 公钥认证时，私钥会发送给服务器吗？
4. 用了公钥后还要输入 passphrase，是公钥认证失败吗？

答案：1. 前者帮助客户端识别主机，后者允许指定用户公钥登录目标账号。2. 不能，需要在目标服务的正确账号和配置下授权。3. 不会。4. 不一定，它可能是在解锁本地私钥。

完成标准：明确说出私钥在哪台设备、授权公钥在哪个目标账号，并通过只尝试公钥的命令登录成功。自连接完成即可进入第四篇；Windows 部分按需选做。

## 参考资料

- [ssh-keygen 手册](https://man.openbsd.org/ssh-keygen)：密钥生成与私钥口令。
- [sshd 手册](https://man.openbsd.org/sshd)：公钥授权列表及权限要求。
- [ssh-agent 手册](https://man.openbsd.org/ssh-agent)与 [ssh-add 手册](https://man.openbsd.org/ssh-add)：代理和身份管理。
- [微软 OpenSSH 密钥管理](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement)：Windows 客户端生成用户密钥。

上一篇：[02 第一次连接](02-first-connection.md)。下一篇：[04 连接别名与文件传输](04-config-and-files.md)。返回[学习导航](../README.md)。
