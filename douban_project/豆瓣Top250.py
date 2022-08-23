# https://movie.douban.com/top250?start=0&filter=
# https://movie.douban.com/top250?start=25&filter=
# https://movie.douban.com/top250?start=50&filter=
import requests
from lxml import etree
file_name = open('mvoies_content.txt','a+',encoding='utf-8')

urls = ['https://movie.douban.com/top250?start=0&filter=']
session = requests.Session()
with session:
    for url in urls:
        response = session.request('GET', url,headers={
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

        })
        response.encoding = 'utf-8'
        content = response.text
        html = etree.HTML(content)
        html_content = html.xpath('//div[@class="info"]')

        for content_1 in html_content:
           title = content_1.xpath('div[@class="hd"]/a/span[@class="title"]/text()')

           info = content_1.xpath('div[@class="bd"]/p/text()')
           # print(title[0])
           # print(info[0],info[1])
           # print('-'*30)
           # print('%s%s\n%s\n'%(title[0],info[0],info[1]))
           file_name.writelines('%s\n'%title[0])

        print('写入完成')



