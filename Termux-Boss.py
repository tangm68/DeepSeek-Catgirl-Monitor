import requests
import time

# ⚠️ 请务必替换为你自己的 Key
API_KEY = "sk-你的API_KEY" 
SERVERCHAN_KEY = "SCT你的KEY" 

WARN_DROP = 5.0
CHECK_INTERVAL = 600

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

print("已启动喵，本喵正在后台默默守护你的钱包喵...")

last_balance = get_balance()

while True:
    time.sleep(CHECK_INTERVAL)
    current_balance = get_balance()

    if current_balance is None:
        print("喵？网络不好，没查到，本喵先休息一下。")
        continue

    if last_balance is not None:
        drop = last_balance - current_balance
        print(f"[{time.strftime('%H:%M:%S')}] 当前余额: {current_balance} 元喵")

        if drop >= WARN_DROP:
            title = "🚨 主人！钱包大漏气喵！"
            content = f"主人！刚才这一小时漏气了 {drop:.2f} 元！现在只剩 {current_balance:.2f} 了喵！"
            send_wechat(title, content)
            print("⚠️ 掉太快了！已发送警报！")

        elif drop >= 0.03:
            title = "📊 余额消耗打卡喵"
            content = f"主人，过去一小时消耗了 {drop:.2f} 元。当前余额：{current_balance:.2f} 元。本喵绝对没偷吃喵~ Ciallo～(∠・ω< )⌒☆"
            send_wechat(title, content)
            print("✅ 已发送正常打卡。")

    last_balance = current_balance
