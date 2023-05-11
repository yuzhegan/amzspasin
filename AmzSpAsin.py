# encoding='utf-8

# @Time: 2023-05-11
# @File: %
#!/usr/bin/env
from requests import session
import requests
from icecream import ic
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
# change cwd to current file dir

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

params = (
    ('actionSource', 'glow'),
)

data = '{"locationType":"LOCATION_INPUT","zipCode":"10001","storeContext":"generic","deviceType":"web","pageType":"Search","actionSource":"glow"}'

session.headers.update(headers)
response = session.post('https://www.amazon.com/portal-migration/hz/glow/address-change',
                        params=params, data=data)
print(response.status_code)


kw_params = (
    ('k', 'timer'),
)

kw_response = session.get('https://www.amazon.com/s',
                          params=kw_params)
print(kw_response.status_code)
# write kw_response to html file
with open('kw_response.html', 'w') as f:
    f.write(kw_response.text)
