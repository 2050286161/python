import requests
import re
import os

if not os.path.exists('./qiutulibs'):
    os.mkdir('./qiutulibs')
url='https://www.qiushibaike.com/imgrank/page/%d/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
ex='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
#爬虫工具解析
#<a href="/article/123437396" target="_blank">
#<img src="//pic.qiushibaike.com/system/pictures/12343/123437396/medium/04YXAR1BC59QVZ4L.jpg" alt="糗事#123437396" class="illustration" width="100%" height="auto">
#</a>
for i in range(1,13):
    new_url=format(url%i)
    page_text=requests.get(url=new_url,headers=headers).text
    img_src=re.findall(ex,page_text,re.S)
    print(img_src)
    for src in img_src:
        #拼接图片链接
        src='https:'+src
        img_data=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split('/')[-1]
        imgpath='./qiutulibs/'+img_name
        with open(imgpath,'wb') as fp:
            fp.write(img_data)
            print('下载成功')