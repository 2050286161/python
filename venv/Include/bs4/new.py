import requests
from bs4 import BeautifulSoup
import os
url='https://so.gushiwen.cn/guwen/book_46653FD803893E4F7F702BCF1F7CCE17.aspx'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
if not os.path.exists('./three'):
    os.mkdir('./three')
reponse=requests.get(url=url,headers=headers)
soup=BeautifulSoup(reponse.text,'lxml')
print(soup.select('.main3>div p')[0].text)
li_list=soup.select('.sons span')
for li in li_list:
    title=li.a.string
    datali_url='https://so.gushiwen.cn'+li.a['href']
    dateil_page=requests.get(url=datali_url,headers=headers)
    soup_data=BeautifulSoup(dateil_page.text,'lxml')
    data_page=soup_data.find('div', class_='contson').text
    data = './three/' + title
    with open(data, 'w',encoding='utf-8') as fp:
        fp.write(data_page)
        print('下载成功')
