import requests
import time

API_KEY = "sk-你的API_KEY"
SERVERCHAN_KEY = "SCTxxxxxx"

WARN_DROP = 5.0       
CHECK_INTERVAL = 3600

def get_balance():
    url = "https://api.deepseek.com/user/balance"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            data = res.json()
            if data.get("balance_infos"):
                return float(data["balance_infos"][0]["total_balance"])
    except Exception:
        pass
    return None

def send_wechat(title, content):
    push_url = f"https://sctapi.ftqq.com/{SERVERCHAN_KEY}.send"
    try:
        requests.post(push_url, data={"title": title, "desp": content}, timeout=15)
    except Exception:
        pass

print("已启动，正在后台默默守护你的钱包...")

last_balance = get_balance()

while True:
    time.sleep(CHECK_INTERVAL)
    current_balance = get_balance()

    if current_balance is None:
        print("网络异常，本次跳过查询。")
        continue

    if last_balance is not None:
        drop = last_balance - current_balance
        print(f"[{time.strftime('%H:%M:%S')}] 当前余额: {current_balance} 元")

        if drop >= WARN_DROP:
            title = "🚨 警告：余额掉得太快了！"
            content = f"过去一段时间余额掉了 {drop:.2f} 元，当前余额仅剩 {current_balance:.2f} 元，请检查是否有异常调用。"
            send_wechat(title, content)
            print("⚠️ 掉太快了！已发送微信警报！")

        # 正常消耗打卡（如果你不想看打卡，可以把下面这三行删掉）
        elif drop >= 0.03:
            title = "📊 余额消耗打卡"
            content = f"过去一段时间消耗了 {drop:.2f} 元。当前余额：{current_balance:.2f} 元。"
            send_wechat(title, content)
            print("✅ 已发送正常打卡通知。")

    last_balance = current_balance
