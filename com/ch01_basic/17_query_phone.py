# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 16:46
# @Author : qingwei.han


import requests
import json


def main():
    """
    查询联调手机的话费余额
    :return:
    """
    requests_url = "https://weixin.10010js.com/app/charge/qryRealFee"
    headers = {
        "Host": "weixin.10010js.com",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        # "Content-Length": "23",
        "Accept": "*/*",
        "Referer": "https://weixin.10010js.com/actPage/activity/index28.html?",
        "Accept-Language": "zh-cn",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
    }
    data = {
        "phone": phone
    }
    response = requests.post(requests_url, headers=headers, data=json.dumps(data)).text
    query = int(response) / 100
    print("\33[32m剩余余额：\33[0m%s" % query)


if __name__ == "__main__":
    print('#' * 20)
    phone = str(input("\33[33m请输入待查询手机号：\33[0m"))
    main()
