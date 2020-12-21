from collections import OrderedDict

msg_sun = OrderedDict()

msg_sun["name"] = 'SunYujun'
msg_sun["wife"] = "LiuYihan"
msg_sun["lover"] = "MengFanlin"

for k, v in msg_sun.items():
    print(k.title()+' is '+v)
