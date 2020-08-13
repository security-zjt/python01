# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/18 22:22
@Auth ： Suk
@File ： 4.网易云音乐下载.py
@IDE  ： PyCharm
@Motto： Knowing your ignorance is the best way to succeed.

"""

# 功能：（网易云）根据歌单链接爬取歌单排名，歌手，时长，所属专辑，歌曲链接(点击即可下载)
import requests
from bs4 import BeautifulSoup

print('\n\t\t请输入网易云歌单链接,为了避免回车后弹窗，请在回车前加上空格，如未输入将自动输入作者歌单链接')
url = input('\t现在，请输入网易云歌单链接：')
if url == '':
    url = 'https://music.163.com/playlist?id=321446375'
elif '/#/' in url:
    url = url.replace('/#/', '/')
headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

s = requests.session()
try:
    response = s.get(url, headers=headers).content
    soup = BeautifulSoup(response, 'lxml')
    # print(soup.prettify())
    lis = list(soup.find('ul'))
    sonlis = []
    fatherlis = ['歌单名：' + str(soup.find('h2').string)]
    for i in lis:
        sonlis = []
        sonlis.append(str(len(fatherlis)) + '.')
        sonlis.append(i.a.string)
        sonlis.append(str(i.a.get('href'))[str(i.a.get('href')).find('=') + 1:-1] + str(i.a.get('href'))[-1])
        fatherlis.append(sonlis)
except:
    print("\n\t歌曲链接输入错误")
    exit('ERROR!')
format = '{0:<10}\t{1:{3}<10}\t{2:<10}'
print("从'{}'中找到了{}条歌曲".format(str(soup.find('h2').string), len(fatherlis) - 1))
print('-------------------------------------------------------------------------------------------------')
print('序号         歌曲名称       歌曲链接，点击即可立即下载此歌曲(此功能仅用于学习，请勿用作其他用途)')
for i in fatherlis:
    if fatherlis.index(i) == 0:
        continue
    else:
        print(format.format(i[0], i[1], 'http://music.163.com/song/media/outer/url?id=' + i[2] + '.mp3', chr(12288)))
print('-------------------------------------------------完毕！----------------------------------------------')