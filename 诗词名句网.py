# -*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


url = "http://www.shicimingju.com/book/sanguoyanyi.html"  # 要爬取的网络地址
menuCode = urllib.request.urlopen(url).read()  # 将网页源代码赋予menuCode
soup = BeautifulSoup(menuCode, 'html.parser')  # 使用html解析器进行解析
menu = soup.find_all(id="mulu")  # 在soup中找到id为mulu的节点
values = ','.join(str(v) for v in menu)  # 将 menu转换为str类型
soup2 = BeautifulSoup(values, 'html.parser')
soup2 = soup2.ul  # 用子节点代替soup2
print("-------------------soup2.contents----------------------------")
print(soup2.contents)


bookName = soup.h1.string  # 找到了书名
print(u"----------------------'书名'------------------------------")
print(u"书名："+bookName)
f = open('C://Users/xxxx/Downloads/'+bookName+'.txt', 'a', encoding='utf8')
f.write(bookName+"\n\n")  # 写入书名
Desc = soup.p.get_text()  # 简介
f.write(Desc+"\n\n\n")  # 写入简介
print(u"---------------------'简介'------------------------------")
print(Desc)


bookMenu=[]  # 章节list
bookMenuUrl=[]  # 章节url的list
# 遍历list要in len(list)-1,因为list第一个元素list[0]
print(u"----------------------------章节和对应的url链接----------------------------")
for i in range(1,len(soup2.contents)-1):  # 依次爬取书的章节
  bookMenu.append(soup2.contents[i].string)
  bookMenuUrl.append(soup2.contents[i].a['href'])
  con=u'章节：%s,URL：%s' %(soup2.contents[i].string,soup2.contents[i].a['href'])
  print(con)
  f.write(con+"\n")  # 写入章节以及对应的URL链接

f.write("\n\n")
# 获取文章内容：通过遍历章节的url来获取每个url对应的文章内容。

urlBegin = "http://www.shicimingju.com"  # 初始URL
for i in range(0, len(bookMenuUrl)):  # 依次替换每个章节的url，读取每章页面的内容
 chapterCode = urllib.request.urlopen(urlBegin+bookMenuUrl[i]).read()  # 拼接成完整的URL，然后读出内容
 chapterSoup = BeautifulSoup(chapterCode, 'html.parser')  # 使用BS读取解析网页代码
 chapterResult = chapterSoup.find_all(id='con2')  # 找到id=‘con2’的节点
 chapterResult = ','.join(str(v) for v in chapterResult)  # 将节点内的代码转为str类型
 chapterSoup2 = BeautifulSoup(chapterResult, 'html.parser')  # 使用BS解析节点内代码
 # print(chapterSoup2.contents)  # .contents把内容转化为list形式
 chapterText = chapterSoup2.get_text()  # 获取节点内文档内容
 print(chapterText)
 f.write(bookMenu[i]+'\n\n')  # 写入文件每章标题
 f.write(chapterText+'\n\n\n')
