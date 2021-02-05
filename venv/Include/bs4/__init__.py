from bs4 import BeautifulSoup
import requests
#将本地的html文档数据加载对象中
#url='https://baike.sogou.com/v136053.htm?fromTitle=%E5%94%90%E8%AF%97'
#headers={
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
#}
#reponse=requests.get(url=url,headers=headers).text
#with open('./text.html','w',encoding='utf-8') as fp:
#    fp.write(reponse)
fp=open('text.html','r',encoding='utf-8')#在线实例化 soup=BeautifulSoup(reponse.text,'lxml')
soup=BeautifulSoup(fp,'lxml')
#print(soup.div)soup.tagName返回的是html中第一次出现的tagName标签
#print(soup.find('div'))soup.find返回的是html中第一次出现的tagName标签
#print(soup.find('div', class_='sub_nav'))soup.find属性定位
#print(soup.find_all('a'))返回符合要求的所有标签，属性定位
#print(soup.select('.sub'))某种选择器，返回列表是复合选择
#print(soup.select('.topnavbox>ul>li>a')[0]) >一个层级 空格多个层级 层级选择器
#print(soup.a.text)获取对应的文本内容 string get_text()可以获得标签中所有文本内容 string只可以获取该标签直系内容
#print(soup.a['href'])属性获取

