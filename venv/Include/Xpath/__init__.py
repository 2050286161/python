from lxml import etree
import requests

url='https://cs.58.com/ershoufang/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
li_list=tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')
fp=open('58.txt','w',encoding='utf-8')
for li in li_list:
    title=li.xpath('./div[2]/h2/a/text()')[0]
    print(title)
    fp.write(title+'\n')