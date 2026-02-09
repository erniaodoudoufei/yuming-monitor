# 🌐 Light Domain Monitor (轻量级域名到期监控)

这是一个极其轻量的域名到期监控工具，基于 Python 编写，支持通过 Docker 一键部署。它能自动查询域名的剩余天数，并在接近到期时通过 Telegram 机器人为您发送提醒。

## ✨ 特性
- **零依赖部署**：采用 Docker 封装，无需配置 Python 环境。
- **灵活配置**：通过环境变量自定义机器人 Token、Chat ID 以及监控域名。
- **精准提醒**：自动处理时区差异，确保剩余天数计算准确。
- **阅后即焚**：支持容器运行完即销毁，不占用服务器常驻内存。

## 🚀 快速开始

只需一行命令，即可开启您的域名哨兵：

```bash
docker run --rm \
  -e TG_TOKEN="您的机器人Token" \
  -e TG_CHAT_ID="您的ChatID" \
  -e DOMAINS="example.com,yourdomain.xyz" \
  -e ALERT_DAYS="30" \
  hdyus-monitor:1.0
