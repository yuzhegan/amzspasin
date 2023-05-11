# encoding='utf-8

# @Time: 2023-05-11
# @File: %
#!/usr/bin/env
from icecream import ic
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
#change cwd to current file dir

import requests

import re

def GenIp():
    r = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall(r'\d+\.\d+\.\d+\.\d+', r.text)[0]
    return ip
    # print(ip)

def SetWhiteList():
    # get current ip
    ip = GenIp()
    # print(ip)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = (
        ('neek', '76123'),
        ('appkey', '7c1ce13b901faee46d1081f8f84bd86f'),
        ('white', ip),
    )

    response = requests.get('https://pycn.yapi.3866866.com/index/index/save_white', headers=headers, params=params)
    print(response.json())




def GenProxy():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    params = (
        ('count', '500'),
        ('neek', '76123'),
        ('type', '1'),
        ('yys', '0'),
        ('port', '1'),
        ('sb', ''),
        ('mr', '1'),
        ('sep', '1'),
    )


    response = requests.get('http://zltiqu.pyhttp.taolop.com/getip', headers=headers, params=params, verify=False)
    # print(response.text)
    return response.text

def GetIPs(text):
    ips = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', text)
    return ips


def GenProxyIPs():
    # SetWhiteList()
    ips = GetIPs(GenProxy())
    # print(ips)
    return ips
# ips = GenProxyIPs()
# with open('proxies.txt', 'w') as f:
#     for ip in ips:
#         f.write(ip+'\n')
#     f.close()
#
