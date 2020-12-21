import csv
from datetime import datetime
from matplotlib import pyplot as plt

# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header.strip())

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    # print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.title("Temperature-high and low-2014", fontsize=24)
plt.xlabel("Date", fontsize=14)
fig.autofmt_xdate()  # 自动调整日期标签格式,倾斜避免重叠
plt.ylabel("temperature", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

# 添加填充
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.show()


