# 爬取盗版小说的爬虫
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib


# 获取小说网页
def gethtml(url, headers={}):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    response.close()
    return content


# 解析章节列表网页
def parsehtmlMusicList(html):
    soup = BeautifulSoup(html, 'lxml')
    list_title = soup.select('h1')  # 找到书名的标签
    list_intro = soup.select('div.cover div.intro')  # 找到简介的标签
    list_menu = soup.select('div.cover ul.chapter li a')  # 找到目录的标签
    print('书名：'+list_title[0].text+'\n\n')
    print('简介：'+list_intro[0].text+'\n\n')
    f = open('C://Users/xxxx/'+list_title[0].text+'.txt', 'a', encoding='utf8')  # 指定存储位置
    f.write(list_title[0].text+"\n")  # 写入书名
    f.write(list_intro[0].text+"\n\n\n")  # 写入简介
    n = 0
    length = len(list_menu)-1  # 获取章节总数
    while n < length:
        # print('章节：'+list_menu[n].text+'\n\n章节链接：'+list_menu[n]['href']+'\n\n')
        #  print('正文：'+list_content[n]['title']+'\n\n作者主页：'+list_author[n]['href']+'\n\n\n')
        chapterCode = urllib.request.urlopen(list_menu[n]['href']).read()  # 拼接成完整的URL，然后读出内容
        chapterSoup = BeautifulSoup(chapterCode, 'html.parser')  # 使用BS读取解析网页代码
        chapterResult = chapterSoup.find_all(id='nr1')  # 找到id=‘con2’的节点
        chapterResult = ','.join(str(v) for v in chapterResult)  # 将节点内的代码转为str类型
        chapterSoup2 = BeautifulSoup(chapterResult, 'html.parser')  # 使用BS解析节点内代码
        chapterText = chapterSoup2.get_text()  # 获取节点内文档内容
        # print(chapterText+'\n\n')
        f.write('章节：'+list_menu[n].text+'\n\n章节链接：\n'+list_menu[n]['href']+'\n\n')  # 写入
        f.write(chapterText+"\n\n\n")  # 写入简介
        n += 1

url = 'https://transcoder.baiducontent.com/tc?srd=1&dict=32&h5...................'  # 小说章节目录页
url = gethtml(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host': 'transcoder.baiducontent.com'
})
parsehtmlMusicList(url)
