# encoding='utf-8

# @Time: 2023-05-11
# @File: %
#!/usr/bin/env
import requests
from icecream import ic
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))


import requests

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'session-id=142-3054330-1694839; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=134-4415301-3228921; skin=noskin; session-token="8bKHNn2FAR1AH+uD0c55SUE7XoJ+DQPDzEvbq63xLAVv6wcXr4pSsYkAOmtH8fGxcKhipn5gwbab8dIYc0y6L1psinRyRThPkOu83zA+tlfMLZGpsxXHO51P9q1hOP5/cwP6ZfFxiVLm6x6zvMOobOjpP81L62a6YXGNyoavUqwk1Xo+2RBnA1/M2MMvKxVBTUT6tLcxNU/qo29DBDEZZLVxKt6Pbja5LLusyGkFiw8="; csm-hit=tb:s-EF1Q2KRGCDQSCNZE7F4Q|1683771117031&t:1683771119397&adb:adblk_no',
    'device-memory': '8',
    'downlink': '7.65',
    'dpr': '0.8',
    'ect': '4g',
    'pragma': 'no-cache',
    'rtt': '250',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '0.8',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-viewport-width': '1294',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'viewport-width': '1294',
}

params = (
    ('k', 'timer'),
)

response = requests.get('https://www.amazon.com/s', headers=headers, params=params)
print(response.status_code)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.amazon.com/s?k=timer', headers=headers)
