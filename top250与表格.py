# https://movie.douban.com/top250?start=0&filter= 第一页
# https://movie.douban.com/top250?start=25&filter= 第二页
# https://movie.douban.com/top250?start=50&filter= 第三页
#//div/ol//li 页面数据
# //div/ol//li//p 演员数据评论
# //div[@class="info"]/div[@class="hd"]/a/@href 电影链接
# //p[@class="quote"]/span[@class="inq"]/text() 电影评论
# //div/ol//li//img/@alt 电影标题
# ////div/ol//li//p[@class='']/text()  0 2 4 演员数据 1 3 5 年份
# //div/ol//li//span[@class='rating_num'] 评分
from requests import Session
from lxml import etree
import random
import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
# worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
urls = []
# url_list = ['https://movie.douban.com/top250?start=0&filter=']
url1 = ('https://movie.douban.com/top250')

ua_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko']
# ua_1 = ua[random.randint(0,5)]
session = Session()
def req_1(urls,ua):
    with session:
        i = 0
        for url in urls:
            ua_s = ua[random.randint(0,4)]
            response = session.request('GET',url, headers={
                'User-agent':ua_s
            })
            content = response.text
            content.encode('utf-8')
            html = etree.HTML(content)
            html_data = html.xpath("//div/ol//li")
            for html in html_data:
                title = html.xpath("//div/ol//li//img/@alt")
                actor = html.xpath("//div/ol//li//p[@class='']/text()")
                grade = html.xpath("//div/ol//li//span[@class='rating_num']/text()")
                movie_url = html.xpath('//div[@class="info"]/div[@class="hd"]/a/@href')
            # print(title[0])
            # print(grade[0])
            # print(actor[0].strip())
            # print(actor[1].strip())
            # print(movie_url[0].strip())
            # print("-"*30)
            print('----准备写入数据----')
            # Data_play(title,grade,actor,movie_url)
            i +=1
            worksheet = workbook.add_sheet('豆瓣Top250排行第%d页'%i, cell_overwrite_ok=True)
            Data_play(title,worksheet,grade,actor,movie_url)
# def Data_play(title,grade,actor,movie_url):
def Data_play(title,worksheet,grade,actor,movie_url):
    style = xlwt.easyxf('font: bold on')
    worksheet.write(0, 1, '评分', style)
    worksheet.write(0, 2, '电影名称', style)
    worksheet.write(0, 5, '主演', style)
    worksheet.write(0, 11, '电影链接', style)
    for i in range(25):
        worksheet.write(i+1, 1 ,label =grade[i])
        worksheet.write(i + 1, 2, label=title[i])
        worksheet.write(i + 1, 4, label=actor[2*i].strip())
        worksheet.write(i + 1, 10, label=movie_url[i])
    workbook.save('豆瓣Top250排行榜.xls')
def url_change(url_ls,url1):
    urls1 = url_ls
    for i in range(1,11):
        url_list = url1
        url_1 = ('start=%d&filter='%((i-1)*25))
        urls = '{}?{}'.format(url_list,url_1)
        urls1.append(urls)
        print('-----web数据生成中-----------')
    print('------web数据已经全部生成--------')
    # print(urls1)

# req_1(url_list,ua_list)
# url_change(urls,url1)
# print(urls)
if __name__ == '__main__':
    url_change(urls,url1)
    req_1(urls,ua_list)
    print('---任务完成---谢谢使用!---')