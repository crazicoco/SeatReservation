import urllib.parse
import urllib.request
import json
import requests

# configuration
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'X-Requested-With': 'XMLHttpRequest'
    }
login_website = 'http://lib-room.chu.edu.cn/ClientWeb/pro/ajax/login.aspx/'
seat_website = 'http://lib-room.chu.edu.cn/ClientWeb/pro/ajax/util.aspx'
room_1 = "http://lib-room.chu.edu.cn/ClientWeb/xcus/a/dftdetail.aspx"
room_2 = "http://lib-room.chu.edu.cn/ClientWeb/pro/ajax/device.aspx"
time_1 = "http://lib-room.chu.edu.cn/ClientWeb/pro/ajax/util.aspx"

login_para = {
    'id': '11111111',
    'pwd': '111111',
    'act': 'login'
}
seat_para = {
    'act': 'get_code',
    'type': '9',
    'sn': '',
    '_': '1599386292694'
}
room1_para = {
    "classKind": "1",
    "id": "100456113",
    "name": "609%e5%ae%a4%e4%b8%aa%e4%ba%ba%e7%a0%94%e4%bf%ae%e9%97%b4"
}

room2_para = {
    "dev_order": '',
    "kind_order": '',
    "classkind": '1',
    "display": 'cld',
    "md": 'd',
    "class_id": '100456113',
    "purpose": '',
    "selectOpenAty": '',
    "cld_name": 'default',
    "date": '20200907',  # 后面注意用变量代替实际时间
    "act": 'get_rsv_sta',
    "_": '1599389266454'
}

time1_para = {
    "act": 'get_code',
    "type": '9',
    "_": '1599394043255'    # 1599393707525  #1599394043255
}
# 登录请求
result = requests.get(login_website, params=login_para)
# 选择房间请求
room_r = requests.get(room_1, params=room1_para, headers=header)  # 确定房间，建立连接
room_r = requests.get(room_2, params=room2_para, headers=header)  # 返回关于所选房间的情况

time = requests.get(time_1, params=time1_para, headers=header)
result_1 = requests.get(seat_website, params=seat_para)
print(result_1.request.headers)
