import requests
import lxml.html
from CrawlerUtility import ChromeHeaders2Dict


url = 'https://news.163.com/'

header = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: vjuids=-105410e83.16781422748.0.178d8f20cd36b; _ntes_nnid=239b189ae2a204c754444561a979c669,1544061855586; _ntes_nuid=239b189ae2a204c754444561a979c669; UM_distinctid=167834b10e1164-082de36c1249db-3f674604-100200-167834b10e2150; mail_psc_fingerprint=c7bfd1b94a1a7a15a17f5641b1ca9e01; usertrack=CrHtglwY2b0m06itAwTaAg==; Province=0370; City=0379; nts_mail_user=cheungpengwei@163.com:-1:1; P_INFO=cheungpengwei@163.com|1546569035|0|mail163|00&99|hen&1546429384&mail163#hen&410100#10#0#0|&0|mail163|cheungpengwei@163.com; s_n_f_l_n3=703921c11637119d1546828553457; NNSSPID=e5b3614f20f241fe97e7598c7c3ed66a; CNZZDATA5661126=cnzz_eid%3D1962845684-1546823301-https%253A%252F%252Fnews.163.com%252F%26ntime%3D1546823301; vjlast=1544061856.1546828628.11; ne_analysis_trace_id=1546828627658; vinfo_n_f_l_n3=703921c11637119d.1.14.1544061855601.1546577553244.1546830017870
Host: news.163.com
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
"""
headers = ChromeHeaders2Dict(header)
resp = requests.get(url, headers=headers).text
pattern = lxml.html.fromstring(resp)
new = pattern.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[3]/div[3]/div[11]/ul/li/a/text()')
num = pattern.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[3]/div[3]/div[11]/ul/li/span/text()')
# print(new)
# print(num)
for i in range(len(new)):
    print('标题：', new[i], '数量：', num[i])
