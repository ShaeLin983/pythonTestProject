import requests

# 请求数据url
member_url = 'https://www.yaozh.com/member/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
# session 类 可以自动保存cookies === cookiesJar
session = requests.session()
# 1.代码登录
login_url = 'https://www.yaozh.com/login'
login_form_data = {
    'username':'xiaomaoera12',
    'pwd': 'lina081012',
    'formhash': '54AC1EE419',
    'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F',
}
login_response = session.post(login_url,data=login_form_data,headers=headers)
print(login_response.content.decode())
# 2.登录成功之后 带着 有效的cookies 访问 请求目标数据
data = session.get(member_url,headers=headers).content.decode()

with open('05-cookie2.html','w') as f:
    f.write(data)