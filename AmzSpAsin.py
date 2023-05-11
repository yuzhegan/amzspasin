# encoding='utf-8

# @Time: 2023-05-11
# @File: %
#!/usr/bin/env
#%%
from requests import session
import requests
from icecream import ic
import os
import time
# os.chdir(os.path.abspath(os.path.dirname(__file__)))
# change cwd to current file dir
from pycnapi import GenProxyIPs  #获取代理IP
import random


#%%
def AddZipCode(zipcode, proxies):
    params = (
        ('actionSource', 'glow'),
    )
    # data = '{"locationType":"LOCATION_INPUT","zipCode":%s,"storeContext":"generic","deviceType":"web","pageType":"Search","actionSource":"glow"}'.format(zipcode)
    data = '{{"locationType":"LOCATION_INPUT","zipCode":{},"storeContext":"generic","deviceType":"web","pageType":"Search","actionSource":"glow"}}'.format(zipcode)
    # print(type(data))
    # add headers to session
    proxies = proxies

    response = session.post('https://www.amazon.com/portal-migration/hz/glow/address-change',
                            params=params, data=data, proxies=proxies)
    if response.status_code == 200:
        print('AddZipCode Success')
    else:
        for i in range(5):
            ip = random.choice(ips)
            proxip = 'http://' + ip
            proxies = {
                'http': proxip,
                'https': proxip,}
            response = session.post('https://www.amazon.com/portal-migration/hz/glow/address-change',
                                params=params, data=data, proxies=proxies)
            if response.status_code == 200:
                print(i)
                print('AddZipCode Success')
                break
    print(response.status_code)
    return proxies


#%%
def GenPorductList(kw, proxies):
    # 随机休眠1-5秒
    unuseips = [] # 无法使用的IP
    sleeptime = random.randint(10, 20)
    time.sleep(sleeptime)
    params = (
        ('k', kw),
    )
    response = session.get('https://www.amazon.com/s',
                           params=params, proxies=proxies)
    if response.status_code == 200:
        print('GenPorductList Success')
    else:
        try:
            ip = proxies['http'].split('//')[1]
            unuseips.append(ip)
            for i in range(50):
                sleeptime = random.randint(5, 10)
                time.sleep(sleeptime)
                ip = random.choice(ips)
                if ip in unuseips:
                    continue # 如果IP已经使用过，则跳过
                proxip = 'http://' + ip
                proxies = {
                    'http': proxip,
                    'https': proxip,
                }
                response = session.get('https://www.amazon.com/s',
                                    params=params, proxies=proxies)
                if response.status_code == 200:
                    print(i)
                    print('GenPorductList Success')
                    # with open('kw_response.html', 'w', encoding='utf-8') as f:
                    #     f.write(response.text)
                    break
            print(response.status_code)
        except:
            print('GenPorductList Failed')
            return ""
    return response.text






# %%
# parse html
from lxml import etree
def parse_link(contents):
    html = etree.HTML(contents)
    divs = html.xpath('//*[@id="search"]/div[1]/div[1]/div[1]/span[1]/div[1]/div')
    # print(len(divs))
    links = []
    for div in divs:
        link = div.xpath('.//span[1]//@href')
        if link:
            links.append(link[0])
    return links

def GenSpLink(links):
    sp_links = []
    for link in links:
        if "_sp_" in link and (link not in sp_links):
            sp_links.append(link)
    return sp_links

#%%
import re
def get_asin(url):
    # 使用正则表达式匹配asin码
    pattern = re.compile(r"dp%2F([A-Z0-9]{10})")
    match = pattern.search(url)
    # print(match)
    if match:
        return match.group(1)
    else:
        try:
            pattern = re.compile(r"dp/([A-Z0-9]{10})")
            match = pattern.search(url)
            return match.group(1)
        except:
            return None
#%%

session = session()

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'anti-csrftoken-a2z': 'gFiAblc4ivxYYuQWArCzzAHvjII0+9KFqNh9v1gAAAAMAAAAAGRcLtxyYXcAAAAA;hL0Jgj6/BaKETsCqnOwbDfZKG8zrVYSlV8RAvbTPOLShAAAAAGRcLtwAAAAB',
    'content-type': 'application/json',
    'cookie': 'session-id=142-8976350-2422860; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=131-4884580-0753829; ext_pgvwcount=1; session-token=yL4100sdiW+ieAogYimq9XsInB1Fwd/1inBccLx2Pkylt4GUeLEOuiyjQOSNbjM2E0HY1U4IJcBzlrUZo/1elvHCo/ssL8ZIbwgh2UNXwE3YByE+cXRndYEav5txgKbbPFv6vMcnQc7sIFIXj25ww2PLiiYUnb9rLoeJ0IgtVKAzUl4XbWnzFqmCAC9kQZmF1XfxEmym7h1B1lynnaVuddOC8Ak2f3K9V7GayNXJ5Jk=; csm-hit=tb:6VJQGSQD7MVZ8XKKH4Q1+s-6VJQGSQD7MVZ8XKKH4Q1|1683762899462&t:1683762899463&adb:adblk_no',
    'device-memory': '4',
    'downlink': '1.55',
    'dpr': '1',
    'ect': '3g',
    'origin': 'https://www.amazon.com',
    'referer': 'https://www.amazon.com',
    'rtt': '350',
    'sec-ch-device-memory': '4',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-viewport-width': '837',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
    'viewport-width': '837',
    'x-requested-with': 'XMLHttpRequest',
}

session.headers.update(headers)


#%%
ips = GenProxyIPs()
# ips = ['121.61.195.140:64256','113.241.136.83:64256','182.204.178.107:64256','121.206.45.233:64256','122.188.193.145:64256','123.189.91.16:64256','106.110.215.81:64256','42.56.2.238:64256','113.237.187.161:64256','125.78.217.60:64256','115.152.234.26:64256','110.85.29.110:64256']
# print(len(ips))
# print(ips[:5])
ip = random.choice(ips)
proxip = 'http://' + str(ip)
proxies = {
  'http': proxip,
  'https': proxip,
}

import polars as pl
kws = pl.read_csv('L213_keywords.csv',ignore_errors=True,skip_rows=0,
)

# write kw_response to html file
proxy = AddZipCode('10001', proxies)
print(proxy)


sp_asins = []
for kw in kws['keywords']:
    print(kw)
    contents = GenPorductList('gymnastcis leotards for girls', proxy)
    #%%
    links = parse_link(contents)
    sp_links = GenSpLink(links)
    asins = []
    for link in sp_links:
        asin = get_asin(link)
        if asin:
            asins.append(asin)
    sp_asins += asins
print(len(sp_asins))
import csv
# with open('asins.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for asin in sp_asins:
#         writer.writerow([asin])

#%%

# 定义一个列表，包含要写入的数据
def Duplicateasins(asins):
    asins = list(set(asins))
    return asins

def First_three_page():
    pass

# 打开一个csv文件，指定写入模式和编码
with open('asins.csv', 'w', encoding='utf-8') as f:
    # 创建一个csv写入对象，指定分隔符为逗号
    writer = csv.writer(f, delimiter=',')
    # 写入一行列名
    writer.writerow(['asins'])
    # 将列表转换为二维列表，每个元素作为一个子列表
    data = [[item] for item in sp_asins]
    # 一次性写入多行数据
    writer.writerows(data)
print('写入完毕！')
