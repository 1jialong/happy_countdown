# Happy Countdown

## 项目描述
这是一个用于计算节假日倒计时和工资发放倒计时的 Python 脚本，并将结果通过企业微信机器人发送通知。

## 安装步骤
1. 确保已安装 Python 3.x。
2. 安装依赖库：
   ```bash
   pip3 install chinese_calendar requests
   ```

## 使用方法
1. 修改 `happy_countdown.py` 文件中的 `xx` 为实际的工资发放日（例如 `5` 表示每月 5 日）。
2. 运行脚本：
   ```bash
   python3 happy_countdown.py
   ```

## 配置说明
1. 替换 `happy_countdown.py` 文件中的 `YOUR_WECHAT_BOT_KEY` 为企业微信机器人的 Webhook 地址。
2. 确保企业微信机器人已启用并配置正确。

## 示例输出
脚本运行后会发送类似以下的通知内容：
```
今天是 2025年5月9日 (星期五)

距离【😄 周    末】只有 2 天

距离【🐲 端午节】只有 10 天

距离【💰 薪水日】只有 20 天

为了美好的假期，撸起袖子加油干！！！
```