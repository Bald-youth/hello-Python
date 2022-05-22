
import requests
import json
from lxml import etree


class baiduSpider:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
           
        }
    def get_html(self, url):

        response = requests.get(
            url=url, headers=self.headers)
        return response.content.decode()

    def get_data(self, rs):
        elem = etree.HTML(rs)
        div_list = elem.xpath('//div[@class="t_con cleafix"]')
        
        data_list = []
        for div in div_list:
            dict = {}
            dict['title'] =div.xpath('.//a[@class="j_th_tit "]/text()')[0]
            dict['href'] ="https://tieba.baidu.com"+str(div.xpath('.//a[@class="j_th_tit "]/@href')[0])
            dict['text']=div.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')[0].strip()if len(
                div.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')) > 0 else None
            
            data_list.append(dict)
        return data_list

    def save_data(self, data_list,tb):
        name=tb+".txt"
        for data in data_list:
            with open(name, 'a', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2))

    def run(self):
        tb=input('请输入你要获取的贴吧：')
        ys=int(input('请输入页数：'))
        for i in range(ys):
            url = self.url.format(tb,i*50)
            rs = self.get_html(url)
            rs = rs.replace('<!--', '')
            rs = rs.replace('-->', '')
            data_list = self.get_data(rs)
            self.save_data(data_list,tb)
        

if __name__ == '__main__':
    baidu = baiduSpider()
 
    baidu.run()
  
