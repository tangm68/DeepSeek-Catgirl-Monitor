# DeepSeek-Catgirl-Monitor
# 🐟 DeepSeek API Balance Monitor (赛博猫娘看门狗)

这是一个轻量级的 Python 脚本，用于定时监控你的 DeepSeek API 余额。当余额消耗过快时，它会通过 Server酱 向你的微信发送警报；正常消耗时，它也会进行打卡，甚至支持“二次元随机台词”。

本项目专为低配设备（如旧手机 Termux、老款笔记本、树莓派）优化，包含防断网容错机制。

## ✨ 特性
- **极低占用**：纯 Python 脚本，无重型依赖。
- **断网容错**：遇到网络波动或 API 超时，会自动跳过，拒绝误报。
- **双重版本**：
  - `boss_simple.py`：极简纯净版，只看数据。
  - `boss_catgirl.py`：二次元整活版，每次打卡随机从 `lines.txt` 抽取一句台词（自带 Ciallo～(∠・ω< )⌒☆）。
- **微信推送**：接入 Server酱（Turbo版），消息秒达。 https://sct.ftqq.com/

## 🚀 快速开始
1. 安装 Python 环境。
2. 安装依赖：`pip install requests`
3. 获取你的 `API_KEY`（DeepSeek 后台）和 `SERVERCHAN_KEY`（Server酱后台）。
4. 将 Key 填入代码中，运行 `python boss.py`。

## 📁 目录结构
- `boss_simple.py` (极简版)
- `boss_catgirl.py` (猫娘版)
- `lines.txt` (猫娘台词库)
  电脑版暂未上传
  ### 📱 手机版 (Termux-Boss.py)

请在 Termux 中运行以下命令安装依赖：
`pip install requests`

然后新建文件 `nano Boss.py`，将以下代码粘贴进去：

```python

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
```
### 📄 台词库 (lines.txt)

```python

主人，本喵今天绝对没有偷吃，只掉了一点点渣渣喵～
Ciallo～(∠・ω< )⌒☆ 钱包很安全，猫娘要睡觉了喵！
报告主人，余额平稳下降中，本喵的猫粮还够吃喵。
```
CTRL+c 暂停

## ⚠️ 免责声明
本脚本仅供学习交流，请勿将含有真实 API Key 的代码上传至公开仓库。
