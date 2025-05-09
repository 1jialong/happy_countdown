# coding:utf-8
import chinese_calendar
import datetime
import requests


def get_paydays(year=None):
    """
    获取工资发放日
    :type year: int
    :param year: 指定年份
    :rtype: list[datetime.date]
    """
    year = datetime.datetime.now().year if not year else year
    money_days = []
    for month in range(1, 13):
        # xx填写工资发放日 eg 5
        fifth = datetime.datetime(year, month, xx)
        while not chinese_calendar.is_workday(fifth):
            fifth = fifth + datetime.timedelta(days=-1)

        money_days.append(fifth.date())
    return money_days


def get_holidays(include_weekends=True, year=None):
    """
    获取节假日
    :type year: int
    :param year: 指定年份
    :type include_weekends: bool
    :param include_weekends: 是否包含周末
    :rtype: list[datetime.date]
    """
    year = datetime.datetime.now().year if not year else year
    holidays = chinese_calendar.get_holidays(
        start=datetime.date(year, 1, 1),
        end=datetime.date(year, 12, 31),
        include_weekends=include_weekends
    )
    return holidays


# 动态获取节假日信息并填充HOLIDAYS字典
HOLIDAYS = {}
holiday_names = {
    "Mid-autumn Festival": "🎑 中秋节",
    "National Day": "🇨🇳 国庆节",
    "New Year's Day": "🏮 元旦节",
    "Spring Festival": "🐰 春    节",
    "Tomb-sweeping Day": "🍃 清明节",
    "Labour Day": "🧹 劳动节",
    "Dragon Boat Festival": "🐲 端午节",
    "National Day": "🎃 七    夕",
}

for holiday in get_holidays(include_weekends=False):
    holiday_detail = chinese_calendar.get_holiday_detail(holiday)
    holiday_name = holiday_detail[1] if holiday_detail else None
    if holiday_name in holiday_names:
        HOLIDAYS[holiday] = holiday_names[holiday_name]


def trs(num):
    mappings = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "日"}
    return mappings.get(num)


def main():
    _today = datetime.datetime.strptime(str(datetime.datetime.now().date()), '%Y-%m-%d')
    format_today = f'{_today.year}年{_today.month}月{_today.day}日 (星期{trs(_today.weekday()+1)})'

    msg = f"今天是 {format_today}\n\n"

    today = datetime.date.today()
    # 追加周末
    weekends = get_holidays()
    for weekend in weekends:
        if weekend == today:
            msg += "🌟 今天是节假日！享受愉快时光！\n\n"
            break
        if weekend > today:
            msg += f" 距离【😄 周    末】只有 {(weekend-today).days} 天\n\n"
            break

    # 添加节假日倒计时（仅显示最近的节假日）
    closest_holiday = None
    closest_days = float('inf')

    for holiday, name in HOLIDAYS.items():
        if holiday > today:
            days_diff = (holiday - today).days
            if days_diff < closest_days:
                closest_days = days_diff
                closest_holiday = (holiday, name)

    if closest_holiday:
        msg += f" 距离【{closest_holiday[1]}】只有 {closest_days} 天\n\n"

    # 追加工资倒计时
    money_days = get_paydays()
    for money_day in money_days:
        if money_day == today:
            msg += "🌟 今天发薪水了！钱包即将续命！\n\n"
            break
        if money_day > today:
            msg += f" 距离【💰 薪水日】只有 {(money_day - today).days} 天\n\n"
            break

    msg += "为了美好的假期，撸起袖子加油干！！！"

    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }

    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_WECHAT_BOT_KEY"

    requests.post(url, headers={'Content-type': 'markdown'}, json=data)


if __name__ == '__main__':
    main()