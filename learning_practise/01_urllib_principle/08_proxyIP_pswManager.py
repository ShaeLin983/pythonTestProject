import urllib.request

#付费的代理发送
#1.用户名密码(带着)
#通过验证的处理器来发送

def money_proxy_use():
    # #第一种方式付费代理发送请求
    # #1.代理ip
    # money_proxy ={"http":"username:pwd@192.168.12.11:8080"}
    # #2.代理的处理器
    # proxy_handler=urllib.request.ProxyHandler(money_proxy)
    #
    # #3.通过处理器创建opener
    # opener = urllib.request.build_opener(proxy_handler)
    # #4.open发送请求
    # opener.open("http://www.baidu.com")
    # #第二种方式发送付费的ip地址
    use_name = "abcname"
    pwd = "123456"
    proxy_money = "123.158.63.130:8888"
    #2.创建密码管理器,添加用户名和密码
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    #uri定位 uri>url
    #url 资源定位符
    password_manager.add_password(None,proxy_money,use_name,pwd)
    #3.创建可以验证代理ip的处理器
    handle_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
    #4.根据处理器创建opener
    opener_auth = urllib.request.build_opener(handle_auth_proxy)
    #5.发送请求
    response = opener_auth.open("http://www.baidu.com")
    print(response.read())

    #爬取自己公司的数据,做数据分析
    #admin

money_proxy_use()