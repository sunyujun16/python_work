from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen
import json

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件d
with open('btc_close_2017.json', 'wb') as f:
    f.write(req)

file_urllib = json.load(req)
print(file_urllib)





