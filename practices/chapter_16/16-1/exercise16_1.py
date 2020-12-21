import csv
from datetime import datetime
from matplotlib import pyplot as plt


class GetData(object):
    def __init__(self, filename):
        self.filename = filename
        self.dates, self.highs, self.lows = [], [], []

    def form_file(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    date = datetime.strptime(row[0], '%Y-%m-%d')
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    self.dates.append(date)
                    self.highs.append(pre_high)
                    self.lows.append(pre_low)
                    print(date, 'missing data')
                else:
                    self.dates.append(date)
                    self.highs.append(high)
                    self.lows.append(low)
                    pre_high = high
                    pre_low = low


filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'

gt1 = GetData(filename_1)
gt2 = GetData(filename_2)
gt1.form_file()
gt2.form_file()
dates = gt1.dates

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, gt1.highs, c='red', alpha=0.5)
plt.plot(dates, gt1.lows, c='blue', alpha=0.5)
plt.plot(gt2.dates, gt2.highs, c='pink', alpha=0.5)
plt.plot(gt2.dates, gt2.lows, c='cyan', alpha=0.5)
plt.title("Temperature-high and low-2014", fontsize=24)
plt.xlabel("Date", fontsize=14)
fig.autofmt_xdate()  # 自动调整日期标签格式,倾斜避免重叠
plt.ylabel("temperature", fontsize=14)
# plt.axis(['', '', 0, 150])
plt.tick_params(axis='both', which='major', labelsize=16)

# 添加填充
plt.fill_between(dates, gt1.highs, gt1.lows, facecolor='blue', alpha=0.1)
plt.fill_between(gt2.dates, gt2.highs, gt2.lows, facecolor='yellow', alpha=0.1)
plt.show()






