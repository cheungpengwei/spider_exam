import requests
import lxml.html
from CrawlerUtility import ChromeHeaders2Dict

url = 'https://www.zcool.com.cn/work/ZMzI2MTMwNDQ=.html'
#请求头
header = """
:authority: www.zcool.com.cn
:method: GET
:path: /work/ZMzI2MTMwNDQ=.html
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: _uab_collina=154682896067764725900635; JSESSIONID=aaaEw8KSW2zqThp0iaoGw; up_location_prompt=1; isnv=1; gr_user_id=f9167224-0f0f-4eff-99b7-279298789096; gr_session_id_acec0eb2dafeaf05=c2ce5512-8128-49c5-bca2-f457d4abadf5; gr_cs1_c2ce5512-8128-49c5-bca2-f457d4abadf5=uid%3A0; gr_session_id_acec0eb2dafeaf05_c2ce5512-8128-49c5-bca2-f457d4abadf5=true
pragma: no-cache
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
"""
headers = ChromeHeaders2Dict(header)
# 请求网页原代码
resp = requests.get(url, headers=headers).text
# print(resp)
# xpath解析，获取图片链接地址
pattern = lxml.html.fromstring(resp)
picture = pattern.xpath('//*[@id="body"]/main/div[2]/div[2]/div[1]/div/div[3]/div[1]/img/@src')
# print(picture)
content = requests.get(picture[0]).content
# 保存图片
with open('图片.png', 'wb') as f:
    f.write(content)

# photo = pattern.xpath('//*[@id="body"]/main/div[2]/div[2]/div[1]/div/div[3]/div/img/@src')
# print(photo)
# n = 1
# for i in photo:
#     with open(f'{n}.gif','wb') as f:
#         f.write(i)
#     print(f'正在保存第{n}张图片')
#     n += 1
