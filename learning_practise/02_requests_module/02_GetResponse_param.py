# https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3&rsv_spt=1&rsv_iqid=0xefb8b43600013949&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E5%25A4%25B4%25E6%259D%25A1&rsv_t=6e3aSjYtw0WgEg7MAIuUlOc3D5lwFBJUVw3KsdkhkWYhZWcNMn9kLBO12GflHlOeUHxx&inputT=506&rsv_pq=81d8f9470001b348&rsv_sug3=19&rsv_sug1=16&rsv_sug7=100&bs=%E5%A4%B4%E6%9D%A1

import requests

# 参数 自动转译

# url = 'https://www.baidu.com/s?wd=美女'
url = 'https://www.baidu.com/s'

params = {
    'wd': "美女"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

response = requests.get(url, headers=headers, params=params)

data = response.content.decode()

with open('baidu.html', 'w') as f:
    f.write(data)

# 发送post 和添加参数
# requests.post(url, data=(参数{}), json=(参数))
