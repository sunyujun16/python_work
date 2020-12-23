from __future__ import (absolute_import, division, print_function, unicode_literals)

from itertools import groupby
from urllib.request import urlopen
import json
import requests
import pygal
import math


def download_file():
    json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"

    response = urlopen(json_url)
    # 读取数据
    req = response.read()
    # 将数据写入文件d
    with open('btc_close_2017.json', 'wb') as f:
        f.write(req)
    file_urllib = json.loads(req)
    print(file_urllib)

    # 用requests模块
    req = requests.get(json_url)
    with open('btc_close_2017_requests.json', 'w') as f:
        f.write(req.text)
    file_requests = req.json()
    print(file_requests)


filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, closes = [], [], [], [], []
# 每天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    dates.append(date)
    month = btc_dict['month']
    month = int(month)
    months.append(month)
    week = btc_dict['week']
    week = int(week)
    weeks.append(week)
    weekday = btc_dict['weekday']
    weekdays.append(weekday)
    close = float(btc_dict['close'])
    close = int(close)
    closes.append(close)
    # print("{} is month {} week {}, {}, the close price is {} RMB".format(
    #     date, month, week, weekday, close))


def draw_line(x_data, y_data, title, y_legend):
    xy_datas = []
    for x_num, data_tup in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_values = [i for _, i in data_tup]
        avr_x_value = sum(y_values) / len(y_values)
        xy_data = [x_num, avr_x_value]
        xy_datas.append(xy_data)

    x_labels, y_labels = [*zip(*xy_datas)]

    # print(x_labels, y_labels)
    # line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_labels
    # N = 20  # x轴坐标每隔20天显示一次
    # line_chart.x_labels_major = dates[::N]
    # closes_log = [math.log10(i) for i in closes]
    line_chart.add(y_legend, y_labels)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_month = dates.index('2017-12-01')
draw_line(months[:idx_month], closes[:idx_month], '收盘月日均值(￥)', '月日均值')

idx_week = dates.index('2017-12-11')
draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘周日均值(￥)', '周日均值')

week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_int = [week_list.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekday_int, closes[1:idx_week], '收盘星期日均值', '星期日均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘星期日均值.svg')

with open('收盘价_Dashboard.html', 'w', encoding='utf-8') as html_file:
    html_file.write('<!DOCTYPE html>\n<html><head><title>收盘价Dashboard</title>'
                    '<meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图.svg', '收盘价折线图_log10.svg', '收盘月日均值(¥).svg',
        '收盘周日均值(¥).svg', '收盘星期日均值.svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}"'
                        ' height=500></object>\n'.format(svg))

    html_file.write('</body></html>')

