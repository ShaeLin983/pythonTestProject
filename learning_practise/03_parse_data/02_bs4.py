import requests
from bs4 import BeautifulSoup
from bs4 import CData
from lxml import etree
import json


def parse_data():
    url = "http://bbs.np163.net/thread-2791491-1-1.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    data = response.content
    with open("test.html", "wb")as f:
        f.write(data)
    soup = BeautifulSoup(open("test.html"), 'lxml')


    # bs4和xpath区别
    # bs4可以读取文件解析，xpath不可以，只能解析字符串
    # bs4解析出来的数据是str（find_all是序列），可以保留格式，xpath不可以，解析出来的是序列。
    # bs4把数据过滤清洗了一遍,可以修改、删除、增加数据


parse_data()
