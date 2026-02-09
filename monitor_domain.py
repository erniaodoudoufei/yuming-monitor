import whois
import requests
import os
from datetime import datetime

# 从系统环境变量中读取配置，提高安全性
TG_TOKEN = os.getenv("TG_TOKEN", "您的默认Token")
TG_CHAT_ID = os.getenv("TG_CHAT_ID", "您的默认ID")
# 多个域名用逗号分隔，例如: "google.com,baidu.com"
DOMAINS_STR = os.getenv("DOMAINS", "67856.xyz,magao.com")
ALERT_DAYS = int(os.getenv("ALERT_DAYS", "30"))

def send_tg_msg(message):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload, timeout=15)
    except Exception as e:
        print(f"发送失败: {e}")

def get_days(domain):
    try:
        w = whois.whois(domain.strip())
        expiry = w.expiration_date
        if isinstance(expiry, list): expiry = expiry[0]
        if not expiry: return None
        # 统一时区修复
        remaining = (expiry.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)).days
        return remaining
    except: return None

if __name__ == "__main__":
    domains = DOMAINS_STR.split(",")
    report = "📊 域名到期提醒:\n"
    need_alert = False
    
    for d in domains:
        days = get_days(d)
        if days is not None:
            status = f"⚠️ {d}: 仅剩 {days} 天" if days < ALERT_DAYS else f"✅ {d}: 剩余 {days} 天"
            report += status + "\n"
            if days < ALERT_DAYS: need_alert = True
    
    if need_alert:
        send_tg_msg(report)
    print(report)
