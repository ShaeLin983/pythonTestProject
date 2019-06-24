import urllib.request
import urllib.parse
import http.cookiejar

def load_douban():

    # 准备登陆界面
    login_url = "https://accounts.douban.com/j/mobile/login/basic"

    # 准备登陆数据
    form_data = {
        "tk": "",
        "name": "linx0220@163.com",
        "password": "919531401.",
        "remember": "false",
        "ticket": ""
    }

    # 准备请求头数据，模拟用户的浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    encode_form_data = urllib.parse.urlencode(form_data).encode('utf-8')

    # 导入cookiejar模块，模拟cookie登陆
    cookie_jar = http.cookiejar.CookieJar()

    # 模拟urlopen的底层逻辑，创建自定义的cookie处理器
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(cookie_handler)

    # 发送登陆请求
    login_request = urllib.request.Request(login_url, headers=headers, data=encode_form_data)
    opener.open(login_request)

    # 试着访问用户中心，成功即登陆成功
    person_url = "https://www.douban.com/"
    person_request = urllib.request.Request(person_url, headers=headers)
    response = opener.open(person_url)
    person_data = response.read().decode("utf-8")

    with open("douban.html", "w", encoding='utf-8')as f:
        f.write(person_data)

load_douban()