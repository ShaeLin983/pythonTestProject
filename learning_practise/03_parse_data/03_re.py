import re
import requests

url = 'http://news.baidu.com/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# response.text 不太准确 转码 是靠推测
data = requests.get(url, headers=headers).content.decode()

# 正则解析 数据
#  每个新闻的titile, url

# <a href="http://news.cnr.cn/native/gd/20181028/t20181028_524397644.shtml" target="_blank" mon="r=1">习近平给民营经济再吃定心丸,民企当体会怎样深意</a>

pattern = re.compile('<a href="(.*?)" target="_blank" mon="(.*?)">(.*?)</a>')
# pattern = re.compile('<a (.*?)</a>',re.S)

result = pattern.findall(data)

print(result)

# with open('02news.html', 'w') as f:
#     f.write(data)
