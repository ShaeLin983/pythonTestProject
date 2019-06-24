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
        # 'Cookie': '_ga=GA1.2.1820447474.1535025127; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; UtzD_f52b_ulastactivity=1511944816%7C0; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=7jsc60esmb6krgthnj99dfq7r3; _gid=GA1.2.358950482.1540209934; _gat=1; MEIQIA_VISIT_ID=1BviNX3zYEKVS7bQVpTRHOTFV8M; yaozh_logintime=1540209949; yaozh_user=381740%09xiaomaoera12; yaozh_userId=381740; db_w_auth=368675%09xiaomaoera12; UtzD_f52b_saltkey=CfYyYFY2; UtzD_f52b_lastvisit=1540206351; UtzD_f52b_lastact=1540209951%09uc.php%09; UtzD_f52b_auth=2e13RFf%2F3R%2BNjohcx%2BuoLcVRx%2FhF0NvwUbslgSZX%2FOUMkCRRcgh5Ayg6RGnklcG3d2DkUFAXJxjhlIS8fPvr9rrwa%2FY; yaozh_uidhas=1; yaozh_mylogin=1540209953; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1535025126%2C1535283389%2C1535283401%2C1539351081%2C1539512967%2C1540209934; MEIQIA_VISIT_ID=1BviNX3zYEKVS7bQVpTRHOTFV8M; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540209958'
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
