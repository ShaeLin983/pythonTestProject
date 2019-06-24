import urllib.request
import random


def load_baidu():
    url = "http://www.baidu.com"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"

    ]
    # 每次请求的浏览器都是不一样的
    random_user_agent = random.choice(user_agent_list)

    request = urllib.request.Request(url)

    # 增加对应的请求头信息(user_agent)
    request.add_header("User-Agent", random_user_agent)

    # 请求数据
    response = urllib.request.urlopen(request)
    # 请求头的信息
    print(request.get_header("User-agent"))


load_baidu()
