#!usr/bin/env python3
# -*- coding:utf-8 -*-

"""
获取喜玛拉雅听《万物简史》的音频文件
"""

import requests
import json

def load_ximaFM():
    base_url = "https://www.ximalaya.com/revision/play/album?albumId=383635&pageNum="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    for page in range(1, 14):
        url = base_url + str(page) + "&sort=0&pageSize=30"
        print(url)
        response = requests.get(url, headers=headers)
        data = response.content

        dict_data = json.loads(data)['data']['tracksAudioPlay']

        for album_data in dict_data:
            album_name = album_data['trackName']
            album_url = album_data['src']
            print(album_name)

            with open("A Brief History of Time/{}.m4a".format(album_name), "wb")as f:
                f.write(requests.get(album_url, headers=headers).content)
load_ximaFM()