import requests, json
from CrawlerUtility import ChromeHeaders2Dict

url = 'https://api.bilibili.com/x/web-interface/newlist'

params = {
    # 'callback': 'jqueryCallback_bili_6750545833325885',
    'rid': 33,
    'type': 0,
    'pn': 1,
    'ps': 20,
}

header = """
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: LIVE_BUVID=AUTO1315434149103291; sid=6cahd4ai; stardustvideo=1; CURRENT_FNVAL=16; buvid3=8AE54823-BE7D-49FA-9E0D-B733CBA0CA69189497infoc; rpdid=wdospsokxxqw; finger=edc6ecda; im_notify_type_383705819=0; im_local_unread_383705819=0; bp_t_offset_383705819=205004810585961689; DedeUserID=383705819; DedeUserID__ckMd5=45c134f6bb1e019a; SESSDATA=afd62b14%2C1549162506%2C6422e911; bili_jct=a89fba107f60c67cf3d0452b43cd97e1; _dfcaptcha=726bc99ba83e36f576c5c105ddc55872
Host: api.bilibili.com
Pragma: no-cache
Referer: https://www.bilibili.com/v/anime/serial/?spm_id_from=333.334.b_7072696d6172795f6d656e75.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
"""
headers = ChromeHeaders2Dict(header)
resp = requests.get(url=url, params=params, headers=headers)
# print(resp.text)
str = resp.text

# dict = json.loads(str)
# print(dict)
# dict = json.load('bilibili.json')
# comments = dict['archives']
# print(comments)