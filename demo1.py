# 豆瓣音乐前二十排行榜
from lxml import etree
import requests
i=1
urls = ['https://music.douban.com/chart']
session = requests.Session()
with session:
    for url in urls:
        response = session.request('GET',url,headers={
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 Chrome/83.0.4103.61 Safari/537.36'
        })
        content = response.text

        html = etree.HTML(content)
        # music_number = html.xpath('//*[@id="content"]/div/div[1]/div/ul/li[1]/span[1]')
        music_name = html.xpath('//*[@id="content"]/div/div[1]/div/ul//a')
        # print(music_name)
        for name in music_name:
            txt = name.xpath('.//text()')
            print(''.join(map(lambda x: x.strip(),txt)))
            print('-'*30)