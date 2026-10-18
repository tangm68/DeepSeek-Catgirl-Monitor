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
- **微信推送**：接入 Server酱（Turbo版），消息秒达。

## 🚀 快速开始
1. 安装 Python 环境。
2. 安装依赖：`pip install requests`
3. 获取你的 `API_KEY`（DeepSeek 后台）和 `SERVERCHAN_KEY`（Server酱后台）。
4. 将 Key 填入代码中，运行 `python boss.py`。

## 📁 目录结构
- `boss_simple.py` (极简版)
- `boss_catgirl.py` (猫娘版)
- `lines.txt` (猫娘台词库，请保存为 UTF-8 编码)

## ⚠️ 免责声明
本脚本仅供学习交流，请勿将含有真实 API Key 的代码上传至公开仓库。
