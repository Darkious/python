import requests
from lxml import etree
import re
def getYearCollege():
    r = requests.get("http://csujwc.its.csu.edu.cn/XSXJ/FB_BJXS.aspx")
    r.encoding = 'GBK'
    page = etree.HTML(r.text)
    nj=page.xpath('//*[@id="theNJ"]/select')
    nj_data = []
    nj_data.append('2014')
    for i in nj[0]:
        nj_data.append(i.attrib['value'])
    yx = page.xpath('//*[@id="theYX"]/select')
    yx_data = []
    for i in yx[0]:
        yx_data.append(i.attrib['value'])
    yx_data.pop(0)
    return nj_data,yx_data
def getSubject(nj,yx):
    r = requests.get("http://csujwc.its.csu.edu.cn/XSXJ/Private/List_NJYXZY.aspx?yx=%s&nj=%s" %(yx, nj))
    r.encoding = 'GBK'
    page = etree.HTML(r.text)
    js = page.xpath('/html/head/script[1]')[0].text
    html = eval(re.findall(r"innerHTML=('[^']*')", js)[0])
    page = etree.HTML(html)
    zy = page.xpath("//option[@value!='']")
    zy_data = []
    for i in zy:
        zy_data.append((i.attrib['value'],i.text))
    return zy_data
def getClass(nj,zy):
    r = requests.get("http://csujwc.its.csu.edu.cn/XSXJ/Private/List_ZYBJ.aspx?zy=%s&nj=%s" %(zy,nj))
    r.encoding = 'GBK'
    page = etree.HTML(r.text)
    js = page.xpath('/html/head/script[1]')[0].text
    html = eval(re.findall(r"innerHTML=('[^']*')", js)[0])
    page = etree.HTML(html)
    class_ = page.xpath("//option[@value!='']")
    class_data = []
    for i in class_:
        class_data.append((i.attrib['value'],i.text))
    return class_data
if __name__=="__main__":
    nj_data,yx_data = getYearCollege()
    banji_data = []
    for i in nj_data:
        print(i)
        for j in yx_data:
            data=getSubject(i,j)
            for item in data:
                new_data = getClass(i,item[0])
                for k in new_data:
                    if k[0]!='Nothing':
                        with open('new.txt','a+') as f:
                            print(k[0])
                            f.write(k[0]+'  '+k[1]+'\n')
                            banji_data.append(k[0])
##            zy_data.append(data)
##    new_zy_data = []
##    for i in zy_data:
##        if i!=[('Nothing', None)]:
##            new_zy_data.append(i)
