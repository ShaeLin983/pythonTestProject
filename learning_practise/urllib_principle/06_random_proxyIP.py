import urllib.request


def proxy_user():
    proxy_list = [
        {"https": ""},
        # {"https":"106.75.226.36:808"},
        # {"https":"61.135.217.7:80"},
        # {"https":"125.70.13.77:8080"},
        # {"https":"118.190.95.35:9001"}
    ]
    for proxy in proxy_list:
        print(proxy)
        # 利用遍历出来的ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        # 创建opener
        opener = urllib.request.build_opener(proxy_handler)

        try:
            data = opener.open("http://www.baidu.com", timeout=1)

            haha = data.read()
            print(haha)
        except Exception as e:
            print(e)


proxy_user()
