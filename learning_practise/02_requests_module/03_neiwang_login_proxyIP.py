import requests

# 发送post请求
# data = {
#
# }
# response = requests.post(url, data=data)

# 内网 需要 认证
# auth = (user, pwd)
# response = requests.get(url, auth=auth)


# 1.请求url
url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

free_proxy = {'http': '27.17.45.90:43411'}

response = requests.get(url=url, headers=headers, proxies=free_proxy)

print(response.status_code)

# 因为hhtps  是有第三方 CA 证书认证的
# 但是 12306  虽然是https 但是 它不是 CA证书, 他是自己 颁布的证书
# 解决方法 是: 告诉 web 忽略证书 访问
response = requests.get(url=url, headers=headers, verify=False)
data = response.content.decode()
