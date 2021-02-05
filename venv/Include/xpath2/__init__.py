from lxml import etree
import requests
import os
if not os.path.exists('./tupian'):
    os.mkdir('./tupian')
url='https://www.ivsky.com/tupian/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
attend=[]
reponse=requests.get(url=url,headers=headers).text
tree=etree.HTML(reponse)
list_img=tree.xpath('/html/body/div[@class="box"][2]/div[@class="left"]/ul/li')
for li in list_img:
    li=li.xpath('./div[@class="il_img"]/a/@href')[0]
    li_scr='https://www.ivsky.com/'+li
    attend.append(li_scr)
for attend_url in attend:
    reponsel = requests.get(url=attend_url, headers=headers).text
    print(reponsel)
    treel = etree.HTML(reponsel)
    list_imgl = treel.xpath('/html/body/div[@class="box"][2]/div[@class="left"]/ul/li')
    for attend_urli in list_imgl:
        attend_urli=attend_urli.xpath('./div[@class="il_img"]/a/img/@src')[0]
        src='http:'+attend_urli
        img_data = requests.get(url=src,headers=headers).content
        img_name = src.split('/')[-1]
        imgpath = './tupian/' + img_name
        with open(imgpath, 'wb') as fp:
            fp.write(img_data)
            print("下载成功")
