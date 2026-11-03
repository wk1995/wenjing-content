---
status: draft
updated: 2026-11-03
level: reference
---

# 08 排错与命令速查

遇到失败时先看报错属于哪个阶段，再做最小范围的检查。前面的 `ssh-lab` 是你在[第四篇](04-config-and-files.md)建立的客户端别名，未建立前不要直接照抄使用。

## 先按这条顺序判断

```text
本机找不到命令？ → 检查客户端
       ↓
地址无法解析？   → 检查地址或 DNS
       ↓
连不到端口？     → 检查开机、服务、路由和防火墙
       ↓
主机身份不一致？ → 独立核对目标身份
       ↓
认证不通过？     → 检查账号、密码、公钥和权限
       ↓
登录后功能失败？ → 检查目标程序、路径和服务端策略
```

## 按报错查问题

| 提示或现象 | 通常发生在哪 | 优先检查 |
| --- | --- | --- |
| `command not found: ssh` / 无法识别 `ssh` | 客户端 | 是否安装客户端，命令路径是否正常 |
| `Could not resolve hostname` | 地址解析 | 地址拼写、别名配置、DNS；是否忘记把示例替换 |
| `Connection timed out` | 网络连接 | 目标是否开机、地址是否可达、端口及防火墙；不是先改密码 |
| `Connection refused` | 连接目标端口 | 该地址和端口是否运行 SSH 服务；也可能是网络设备主动拒绝 |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` | 主机身份检查 | 地址是否变化、是否重装或更换密钥；先核对指纹 |
| `Permission denied` | 用户认证 | 目标账号是否正确、是否允许登录、认证材料是否匹配 |
| `Permission denied (publickey)` | 用户公钥认证 | 是否提供正确私钥，目标是否授权对应公钥，权限和策略是否符合要求 |
| `Too many authentication failures` | 用户认证 | 客户端或代理是否尝试过多身份；指定对应密钥并限制身份 |
| `UNPROTECTED PRIVATE KEY FILE` | 本地私钥权限 | 私钥是否允许其他用户读取；Mac/Linux 检查权限和归属 |
| `no matching ... found` | 算法协商 | 两端版本及策略是否兼容；优先了解升级路径，不随意开启旧算法 |
| 登录后文件操作 `Permission denied` | 目标文件权限 | 这时可能已登录成功，检查文件和目录权限，不要误判为认证失败 |

“通常”不等于唯一原因。网络设备的过滤、系统策略和具体版本可能改变表现。

## 打开详细日志

在发起连接的本机终端执行：

```bash
ssh -vvv ssh-lab
```

详细程度随 `-v` 数量增加，最多三个。先从日志中确认四件事：

1. 实际连接的是哪个地址和端口。
2. 是否已经建立 TCP 连接。
3. 客户端尝试的是哪个账号、哪些认证方法和身份文件。
4. 是否出现认证成功，随后才发生其他错误。

日志可能包含账号、地址、目录、主机指纹和环境信息。分享前遮盖不愿公开的部分；不需要提供私钥或密码。

## 检查自己到底用了什么配置

```bash
ssh -G ssh-lab
```

核对 `hostname`、`user`、`port`、`identityfile` 和 `identitiesonly`。如果原以为登录远程，却配置到了 `127.0.0.1`，先改正配置。

## 只测试公钥认证

先完成第三篇的密钥生成和授权，再在本机 Mac 执行：

```bash
ssh -o IdentitiesOnly=yes -o PreferredAuthentications=publickey -i ~/.ssh/id_ed25519_ssh_learning "$(whoami)"@127.0.0.1
```

这次测试不回退到账号密码。输入私钥口令不算回退密码认证。若使用了额外客户端配置，仍应通过日志确认实际提供的身份。

## 发现主机身份改变怎么办

先通过目标设备本地终端、可信管理员或控制台，查到新指纹并确认变化原因。[第二篇](02-first-connection.md)有本机查看主机公钥指纹的方法。

**只有完成独立核验以后**，才处理对应旧记录。例如已确认自连接练习的主机密钥变化，可以在本机运行：

```bash
ssh-keygen -R 127.0.0.1
```

如果是非默认端口，主机记录常用 `[地址]:端口` 表示，例如：

```bash
ssh-keygen -R '[127.0.0.1]:2222'
```

这些命令会修改主机记录，不是只读查询。替换或删除记录后，重新连接仍需核对新指纹。域名和 IP 可能有各自记录，要对应实际连接方式处理，不要清空整个文件。

## Mac 密钥权限检查

在本机 Mac 终端查看：

```bash
ls -ld ~/.ssh
ls -l ~/.ssh/id_ed25519_ssh_learning ~/.ssh/id_ed25519_ssh_learning.pub ~/.ssh/authorized_keys
```

只对本教程的对应文件修正权限：

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519_ssh_learning
chmod 600 ~/.ssh/authorized_keys
```

如果目标是另一台机器，目标 `authorized_keys` 的检查应在目标账号下做，修本机同名文件不会替目标授权。Windows ACL 与 Mac/Linux 权限模型不同，不要在 PowerShell 中直接套用这些 `chmod` 命令。

## 几个一眼能查的命令

| 目的 | 命令 | 执行位置 |
| --- | --- | --- |
| 看客户端版本 | `ssh -V` | 本机终端或 PowerShell |
| 看当前账号 | `whoami` | 当前系统，注意是否已登录远程 |
| 看主机名 | `hostname` | 当前系统 |
| 发起别名连接 | `ssh ssh-lab` | 配置别名的客户端 |
| 看配置，不登录 | `ssh -G ssh-lab` | 客户端 |
| 看详细连接日志 | `ssh -vvv ssh-lab` | 客户端 |
| 看代理中身份的指纹 | `ssh-add -l` | 客户端，需代理可连接 |
| 看用户公钥指纹 | `ssh-keygen -lf ~/.ssh/id_ed25519_ssh_learning.pub` | 存放该公钥的 Mac 终端 |
| 退出当前远程 Shell | `exit` | 已登录的远程 Shell |

## 提问时记录这五项

1. 哪台机器连接哪台机器，分别是什么系统。
2. 同一局域网、跨家庭网络，还是云服务器。
3. 执行的命令，隐藏敏感地址但保留参数结构。
4. 完整报错，以及是否曾经成功。
5. 最近改过什么，例如密码、密钥、IP、系统、网络或配置。

示例：“Windows PowerShell 连接同一家庭网络的 Mac。Mac 自连接成功，Windows 连接 Mac 局域网 IP 超时，最近换过路由器。”这比只说“SSH 用不了”更容易定位。

## 参考资料

- [ssh 手册](https://man.openbsd.org/ssh)：日志级别和配置输出。
- [ssh-keygen 手册](https://man.openbsd.org/ssh-keygen)：指纹和主机记录管理。
- [sshd 手册](https://man.openbsd.org/sshd)：认证与文件权限条件。

返回[学习导航](../README.md)。
