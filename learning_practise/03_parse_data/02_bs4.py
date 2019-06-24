# pip install beautifulsoup4

from bs4 import BeautifulSoup

html_doc = """
<html><head>
<title id="one">The Dormouse's story</title>
</head>
<body>
<p class="story"><!--...--></p>
<p class="title">
    p标签的内容
    <b>The Dormouse's story</b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


"""
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json


class BtcSpider(object):
    def __init__(self):
        self.url = 'http://8btc.com/forum-61-{}.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

        # 保存列表页的数据
        self.data_list = []

        self.data_detail = []

    # 1.发请求
    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content
        return data

    # 2.解析数据list
    def parse_list_data(self, data):

        # 1.转类型
        soup = BeautifulSoup(data, 'lxml')
        # 2.解析内容 取出 所有的类选择器的 A
        title_list = soup.select('.xst')
        for title in title_list:
            list_dict_data = {}
            list_dict_data['title'] = title.get_text()
            list_dict_data['detail_url'] = title.get('href')
            self.data_list.append(list_dict_data)

    # 3.解析数据详情页
    def parse_detail_data(self, data):
        html_data = BeautifulSoup(data, 'lxml')

        # 取出问题--list[1][0]
        question = html_data.select('#thread_subject')[0].get_text()
        print(question)
        answer_list = html_data.select('.t_f')
        for answer in answer_list:
            answer_list = []
            answer_list.append(answer.get_text())

        detail_data = {
            "question": question,
            "answer": answer_list
        }

        self.data_detail.append(detail_data)

    # 3.保存数据
    def save_data(self, data, file_path):
        data_str = json.dumps(data)
        with open(file_path, 'w') as f:
            f.write(data_str)

    def start(self):
        # 列表页的请求
        for i in range(1, 2):
            url = self.url.format(1)
            data = self.get_response(url)
            self.parse_list_data(data)
        self.save_data(self.data_list, "04list.json")

        # 发送详情页的请求
        for data in self.data_list:
            detail_url = data['detail_url']
            detail_data = self.get_response(detail_url)

            # 解析详情页的数据
            self.parse_detail_data(detail_data)

        self.save_data(self.data_detail, 'detail.json')


BtcSpider().start()

"""
html_data = etree.HTML(data)

        result_list = html_data.xpath('//div[contains(@id,"stickthread")]')
        result_list = html_data.xpath('//head/following-sibling::*[1]')
        print(len(result_list))
        print(result_list)





# 1.转类型 bs4.BeautifulSoup'
soup = BeautifulSoup(html_doc, 'lxml')

# 2.通用解析方法

#  find--返回符合查询条件的 第一个标签对象
result = soup.find(name="p")
result = soup.find(attrs={"class": "title"})
result = soup.find(text="Tillie")
result = soup.find(
    name='p',
    attrs={"class": "story"},
)

# find_all--list(标签对象)
result = soup.find_all('a')
result = soup.find_all("a", limit=1)[0]
result = soup.find_all(attrs={"class": "sister"})

# select_one---css选择器
result = soup.select_one('.sister')

# select----css选择器---list
result = soup.select('.sister')
result = soup.select('#one')
result = soup.select('head title')
result = soup.select('title,.title')
result = soup.select('a[id="link3"]')

# 标签包裹的内容---list
result = soup.select('.title')[0].get_text()


# 标签的属性
# result = soup.select('#link1')[0].get('href')
print(result)



# 1.转类型
# 默认bs4会 调用你系统中lxml的解析库 警告提示
# 主动设置 bs4的解析库
soup = BeautifulSoup(html_doc, 'lxml')

# 2.格式化输出 补全
result = soup.prettify()


# 2. 解析数据

# Tag 标签对象 bs4.element.Tag'
result = soup.head

# 注释的内容  类型 'bs4.element.Comment'
result = soup.p.string
print(type(result))

result = soup.a


# 内容 Navigablestring  'bs4.element.NavigableString
result = soup.a.string

# 属性
result = soup.a['href']
"""

