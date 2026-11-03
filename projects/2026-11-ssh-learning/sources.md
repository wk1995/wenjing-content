---
template: project/sources
template_version: 2026-07-16
status: draft
updated: 2026-11-03
---

# SSH 学习资料来源与分篇结构

## 资料原则

- 优先依据 OpenSSH、操作系统厂商、Ubuntu 与 IETF 的一手资料；稳定概念用原创解释、案例和自测组织。
- 以下核验日期统一为 2026-11-03，指网页资料核对日期，不代表在用户设备上完成实验。
- OpenBSD 手册读取的是当日在线默认版本 OpenBSD-current，不等于用户 Mac、Windows 或 Linux 上实际安装的 OpenSSH 版本。
- 用户系统版本、客户端版本、权限和网络尚未确认。涉及菜单与安装入口时保留系统范围，不推定设备默认状态。
- 单篇结构、候选标题、可引用事实和示意图规划集中保留在本文件；正文放 `doc/`，当前没有平台成稿。

## 分篇内容结构

所有正文状态为 `draft`，目标读者为用户本人。以下为选定标题及备用标题，后者供后续修订使用。

| 编号 | 输出文件 | 深度 | 目标与核心观点 | 大纲 | 备用标题与素材 |
| --- | --- | --- | --- | --- | --- |
| 01 | [从零认识 SSH](doc/01-foundations.md) | 入门 | 分清窗口、协议、软件与两端角色 | 场景、术语、命令、身份、执行位置、只读练习、自测 | 备用：SSH 到底连接了什么；素材：客户端与服务端文字图 |
| 02 | [第一次连接](doc/02-first-connection.md) | 入门 | 没有云服务器也能开始，先自连接再跨设备 | Mac 服务入口、主机指纹、自连接、退出、Windows 连 Mac、恢复、自测 | 备用：用家里的电脑练 SSH；素材：步骤表，无用户设备截图 |
| 03 | [密码 公钥与私钥](doc/03-key-authentication.md) | 实用 | 区分主机身份、用户认证和私钥口令 | 两类身份、文件职责、独立密钥、追加授权、强制公钥测试、代理、撤销、自测 | 备用：SSH 的两种身份验证；素材：密钥文件职责表 |
| 04 | [连接别名与文件传输](doc/04-config-and-files.md) | 实用 | 客户端配置减少输入，传文件先看方向 | config、解析检查、执行命令、scp 上传下载、SFTP、自测 | 备用：登录以后怎么传文件；素材：参数大小写与传输方向表 |
| 05 | [网络与隧道](doc/05-network-and-tunnels.md) | 进阶 | 分清地址监听、SSH 跳板与系统路由，认证材料不能代替网络路径 | 回环与私有地址、A/B/C 双网卡拓扑、ListenAddress、系统转发边界、客户端源地址、NAT、公网路径、-L、-J/ProxyJump、自测 | 备用：多网卡的 B 怎样提供 SSH；素材：双网卡拓扑、任务区别表、NAT 与转发路径文字图 |
| 06 | [安全与运维](doc/06-security-and-operations.md) | 进阶 | 权限、授权和配置变更需要分别管理 | 账号权限、开放范围、密钥管理、主机变更、配置检查、长任务、代理转发、自测 | 备用：SSH 长期使用时要管好什么；素材：配置变更顺序 |
| 07 | [连接原理](doc/07-how-ssh-works.md) | 进阶 | 网络、主机认证、用户认证、通道各有分工 | 六步简化流程、文件对应、加密范围、免密表述、自测 | 备用：输入 ssh 后发生了什么；素材：协议流程与加密范围文字图 |
| 08 | [排错与命令速查](doc/08-troubleshooting.md) | 查阅 | 按失败阶段找原因，避免盲目改密码和清空信任记录 | 阶段图、报错表、双网卡一侧不通、跳板分阶段排错、Linux 监听与路由查询、日志、配置、公钥测试、主机记录、权限、提问模板 | 备用：SSH 连接失败从哪里查；素材：症状与检查表 |

## 来源列表

表中“未标注”表示未将页面发布日期作为事实使用，不将抓取时间当成发布时间。RFC 的发布日期来自文档头部。所有链接都指向官方主体。

| 编号 | 主体及标题 | 链接 | 发布时间 | 核验日期 | 适用平台或版本 | 支持结论 |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | OpenBSD ssh 手册 | [ssh(1)](https://man.openbsd.org/ssh) | 动态手册，未固定发布日期 | 2026-11-03 | OpenBSD-current 在线上游手册；基础选项需结合本机版本 | 远程执行、-V/-G/-v/-i/-p、-L/-N/-J、主机指纹与代理转发 |
| S2 | OpenBSD ssh-keygen 手册 | [ssh-keygen(1)](https://man.openbsd.org/ssh-keygen) | 动态手册，未固定发布日期 | 2026-11-03 | OpenBSD-current；教程使用常见 Ed25519、指纹与记录管理选项 | -t/-f/-C、私钥口令、-l、-R |
| S3 | OpenBSD 客户端配置手册 | [ssh_config(5)](https://man.openbsd.org/ssh_config) | 动态手册，未固定发布日期 | 2026-11-03 | OpenBSD-current；客户端配置 | Host、HostName、User、IdentityFile、IdentitiesOnly、配置匹配、ExitOnForwardFailure |
| S4 | OpenBSD 服务端手册 | [sshd(8)](https://man.openbsd.org/sshd) | 动态手册，未固定发布日期 | 2026-11-03 | OpenBSD-current；Unix 风格授权文件，其他系统有差异 | authorized_keys 的角色、文件安全条件、用户认证与会话 |
| S5 | OpenBSD 文件复制手册 | [scp(1)](https://man.openbsd.org/scp) | 动态手册，未固定发布日期 | 2026-11-03 | 当前上游 scp；旧版本协议行为可能不同 | 来源与目标语法、大写 -P、当前上游默认使用 SFTP |
| S6 | OpenBSD SFTP 手册 | [sftp(1)](https://man.openbsd.org/sftp) | 动态手册，未固定发布日期 | 2026-11-03 | 当前上游 sftp；基础交互命令 | put/get、pwd/lpwd、ls/lls、cd/lcd、bye、-P |
| S7 | 苹果 允许远程电脑访问 Mac | [Remote Login](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac) | 未标注 | 2026-11-03 | 当日 macOS 在线指南；用户系统版本未知 | 通用→共享→远程登录、限定用户、SSH/SFTP、账号地址登录方式 |
| S8 | 微软 OpenSSH for Windows overview | [OpenSSH 概览](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview) | 页面显示 2025-02-20 | 2026-11-03 | Windows 10 build 1809 起及文档列出的 Windows/Server；不推定用户安装状态 | 客户端/服务端架构、组件用途、可选功能 |
| S9 | 微软 Get started with OpenSSH | [OpenSSH 入门](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) | 未作为发布日期结论使用 | 2026-11-03 | Windows 内置 Feature on Demand；当前页面涵盖 Windows 10/11 与 Server | 通过可选功能或 PowerShell 安装客户端；客户端与服务端分开 |
| S10 | Ubuntu OpenSSH server 指南 | [OpenSSH server](https://documentation.ubuntu.com/server/how-to/security/openssh-server/) | 滚动维护，未固定发布日期 | 2026-11-03 | Ubuntu 官方文档；不泛化到 macOS 或 Windows | sshd -t、配置片段、变更后服务管理与验证 |
| S11 | OpenBSD 认证代理手册 | [ssh-agent(1)](https://man.openbsd.org/ssh-agent) | 动态手册，未固定发布日期 | 2026-11-03 | 当前上游代理语义；系统集成因平台而异 | 代理保存加载的认证身份并提供签名，私钥及其口令不经网络发给目标 |
| S12 | OpenBSD 代理密钥管理手册 | [ssh-add(1)](https://man.openbsd.org/ssh-add) | 动态手册，未固定发布日期 | 2026-11-03 | 当前上游 ssh-add；需能访问代理 | 加载身份、-l 查看指纹、-d 移除指定身份 |
| S13 | IETF RFC 1918 Address Allocation for Private Internets | [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) | 1996-02 | 2026-11-03 | IPv4 私有地址分配 | 三个私有 IPv4 地址块及其非全球唯一性质 |
| S14 | IETF RFC 3022 Traditional IP Network Address Translator | [RFC 3022](https://www.rfc-editor.org/rfc/rfc3022) | 2001-01 | 2026-11-03 | 传统 IPv4 NAT 模型 | NAT 地址转换及常见出入站路径区别；不据此推定用户运营商状态 |
| S15 | IETF RFC 4251 SSH Protocol Architecture | [RFC 4251](https://www.rfc-editor.org/rfc/rfc4251) | 2006-01 | 2026-11-03 | SSH 协议架构说明 | 传输层、用户认证、连接协议分工 |
| S16 | IETF RFC 4253 SSH Transport Layer Protocol | [RFC 4253](https://www.rfc-editor.org/rfc/rfc4253) | 2006-01 | 2026-11-03 | 历史基础规范；算法细节有后续更新 | 版本交换、算法协商、密钥交换、加密与完整性保护 |
| S17 | IETF RFC 4252 SSH Authentication Protocol | [RFC 4252](https://www.rfc-editor.org/rfc/rfc4252) | 2006-01 | 2026-11-03 | 用户认证协议基础；实际方法受实现与策略控制 | 公钥认证签名、密码认证及用户认证阶段 |
| S18 | IETF RFC 4254 SSH Connection Protocol | [RFC 4254](https://www.rfc-editor.org/rfc/rfc4254) | 2006-01 | 2026-11-03 | 连接协议基础 | 多通道、Shell、子系统及 TCP 转发 |
| S19 | 微软 OpenSSH Server configuration for Windows | [Windows OpenSSH 配置](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-server-configuration) | 未作为发布日期结论使用 | 2026-11-03 | Windows OpenSSH；须区分客户端和服务端路径 | 客户端个人配置在用户主目录 .ssh/config，服务端配置位置不同 |
| S20 | OpenBSD 服务端配置手册 | [sshd_config(5)](https://man.openbsd.org/sshd_config) | 动态手册，未固定发布日期 | 2026-11-03 | 当日 OpenBSD-current；实际服务启动、监听和策略随系统而异 | ListenAddress 本地地址与多项累加、AddressFamily、AllowTcpForwarding、DisableForwarding、PermitOpen、Match |
| S21 | Linux 内核 IP Sysctl 文档 | [IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html) | 滚动维护，未固定发布日期 | 2026-11-03 | Linux IPv4 内核配置；不套用到 macOS/Windows | ip_forward 控制接口间 IPv4 转发，不等于 SSH 用户态 TCP 转发 |
| S22 | IETF RFC 1812 Requirements for IP Version 4 Routers | [RFC 1812](https://www.rfc-editor.org/rfc/rfc1812) | 1995-06 | 2026-11-03 | IPv4 路由器基础模型；不用于推定具体设备配置 | 转发与路由表、下一跳、主机本地接收和转发的区别 |
| S23 | iproute2 ss 手册 | [ss(8)](https://man7.org/linux/man-pages/man8/ss.8.html) | man7 承载的原始手册，未固定发布日期 | 2026-11-03 | Linux 安装 iproute2 的环境；不套用到 Mac/PowerShell | -l 查看监听、-n 数字形式、-t 限定 TCP |
| S24 | iproute2 ip-route 手册 | [ip-route(8)](https://man7.org/linux/man-pages/man8/ip-route.8.html) | man7 承载的原始手册，未固定发布日期 | 2026-11-03 | Linux iproute2；查询结果受实际路由策略影响 | ip route get 及 from 参数，只查询内核选路，不添加路由 |

## 可引用事实与使用边界

| 事实 | 来源 | 可用于本文哪些位置 | 不应扩大的结论 |
| --- | --- | --- | --- |
| Mac 可以开启远程登录接收 SSH/SFTP | S7 | 02 实验入口 | 不表示公司设备允许开启，也不表示公网可达 |
| 客户端与服务端角色可由普通电脑承担 | S1、S8 | 01、02 | 不表示目标默认已安装且启动服务 |
| 客户端通过主机密钥确认目标身份 | S1、S2 | 02、03、06、08 | 不能将首次出现的未知指纹直接写成可信 |
| 用户公钥认证不发送用户私钥 | S1、S17 | 03、07 | 不表示客户端失陷时仍能保护全部秘密 |
| 当前上游 scp 默认使用 SFTP | S5 | 04 | 不泛化到所有历史客户端 |
| -L 的目标连接由 SSH 服务端发起 | S1、S18 | 05、07 | 不表示 SSH 出口到最终目标也自动加密 |
| ExitOnForwardFailure 不验证最终目标服务可用 | S3 | 05 | 不能把隧道监听成功写成端到端服务成功 |
| sshd -t 属于配置语法检查 | S4、S10 | 06 | 不能替代新会话与网络验证 |
| 私有地址不作为全球唯一主机地址使用 | S13、S14 | 05 | 不据此断言用户没有公网 IPv4/IPv6 或 VPN |
| 同一 SSH 服务可监听多个本地地址，监听与来源访问控制不同 | S20 | 05、08 | 不表示实际系统已监听所有网卡，也不表示追加地址能覆盖已有通配监听 |
| ProxyJump 由跳板发起目标 TCP 连接，目标 SSH 认证仍在客户端完成 | S1、S3、S18、S20 | 05、08 | 不要求复制私钥到 B，也不能把 B 的 TCP 转发许可视为当然成立 |
| 仅登录双网卡 B 或使用 SSH 跳板通常无需系统 IP 转发 | S1、S18、S21、S22 | 05、08 | 仅限本文普通主机网络模型，不代表 A、C 已获得通用跨网段路由 |
| Linux ss 和 ip route get 可查询监听与选路 | S23、S24 | 08 | 语法示例不是实际输出，查询成功不证明对端服务可达 |

## 示例与素材规划

- 文本、步骤、自测和文字图为本项目创作，未引入外部图片或视频。
- 账号 alice、IP 192.168.1.50 是说明用虚构值，不是发现的设备信息。
- 多网卡场景按用户的 AB、BC 描述组织为 A/B 共用网段一、B/C 共用网段二；具体地址 192.168.10.10、B 的 192.168.10.1/192.168.20.1、C 的 192.168.20.30，以及 buser/cuser 均为新增虚构示例，两段均假设 /24。未确认用户有该实际拓扑。
- ListenAddress 片段为服务端概念示例；ProxyJump 块是 A 的客户端配置示例。未修改任何实际 SSH 服务、网卡、路由、防火墙或内核开关。
- 127.0.0.1 自连接路线用于降低练习门槛，不代表用户已验收任何状态。
- 端口转发示例只描述已有服务的访问路径，目标 3000 端口服务为假设前提，未安装、启动或访问。
- 无 AI 生成媒体资产、第三方运行时包、密钥、账号凭据或接口调用记录需要纳入本项目。

## 不确定信息与后续补充

- 用户实际系统版本、OpenSSH 版本、是否有管理员权限与公司策略。
- Mac 远程登录、密码/公钥策略、主机密钥实际算法与文件状态。
- Windows 客户端安装状态、家庭网络设备隔离与防火墙策略。
- 所有设备实操结果：待用户练习，不能写成已测试。
- 资料访问情况：苹果网页在 web 工具返回 429 后，通过直接 HTTPS 抓取官方正文完成核对；微软入门旧连字符路径返回 404，已从官网入口解析并改用实际下划线路径。
