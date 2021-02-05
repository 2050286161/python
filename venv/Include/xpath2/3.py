for attend_urli in list_imgl:
    attend_urli = attend_urli.xpath('./div[@class="il_img"]/a/img/@src')[0]
    src = 'http:' + attend_urli
    img_data = requests.get(url=src, headers=headers).content
    img_name = src.split('/')[-1]
    imgpath = './tupian/' + img_name
    with open(imgpath, 'wb') as fp:
        fp.write(img_data)
        print("下载成功")