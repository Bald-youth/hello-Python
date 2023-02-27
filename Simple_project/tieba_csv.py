import requests
import json
from lxml import etree
import csv


class baiduSpider:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
        }

    def get_html(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()

    def get_data(self, rs):
        elem = etree.HTML(rs)
        div_list = elem.xpath('//div[@class="t_con cleafix"]')

        data_list = []
        for div in div_list:
            item = {}
            item['title'] = div.xpath('.//a[@class="j_th_tit "]/text()')[0]
            item['writer'] = div.xpath('.//a[@target="_blank"]/text()')[1]
            item['reply Quantity'] = div.xpath('.//div[@class="col2_left j_threadlist_li_left"]/span/text()')[0]
            item['creatTime'] = div.xpath('.//div/div/div/span[contains(@title,"创建时间")]/text()')[0]
            item['text'] = div.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')[0].strip() if len(
                div.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')) > 0 else None

            data_list.append(item)
        return data_list

    def save_data(self, data_list, tb):
        filename = tb + '.csv'
        # encoding='gbk' windows 使用'gbk' 否者会乱码，Linux等使用'utf-8'
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['标题', '作者', '回复数', '创建时间', '内容'])
            for item in data_list:
                writer.writerow([item['title'], item['writer'], item['reply Quantity'], item['creatTime'], item['text']])
        print('数据已保存到 %s' % filename)

    def run(self):
        tb = input('请输入你要获取的贴吧：')
        begin = int(input('输入起始页：'))
        stop = int(input('请输入页数：'))
        data_list = []
        for i in range(begin, stop + 1):
            url = self.url.format(tb, i * 50)
            rs = self.get_html(url)
            print('第 %d 页抓取成功' % i)
            rs = rs.replace('<!--', '')
            rs = rs.replace('-->', '')
            items = self.get_data(rs)
            data_list.extend(items)
        self.save_data(data_list, tb)


if __name__ == '__main__':
    spider = baiduSpider()
    spider.run()
