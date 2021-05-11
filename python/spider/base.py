#!/usr/bin/python
#coding:utf-8

from urllib import request
from lxml import etree
AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
class BaseSpider(object):
    def __init__(self, agent=AGENT):
        self.agent = agent
    
    def setUrl(self, url):
        #请求网页，的到网页数据
        heade = {"User-Agent":self.agent}
        req_obj = request.Request(url, headers=heade)
        html_obj = request.urlopen(req_obj)
        self.html = html_obj.read()
    
    def setXpath(self, xpath):
        #根据传入的xpath来得到想要的内容
        ehtml_obj = etree.HTML(self.html)
        self.ehtml_part_list = ehtml_obj.xpath(xpath)
        #for ehtml_part in ehtml_part_list:
            #print(ehtml_part.text)

    def getText(self):
        #获得text文本内容
        for ehtml_part in self.ehtml_part_list:
            print(ehtml_part.text)
    
    def returnAttrib(self, attrib):
        #获得指定属性内容
        the_att = []
        print(1)
        for att in self.ehtml_part_list:
            the_att_part = att.attrib.get(attrib)
            if the_att_part:
                the_att.append(the_att_part)
        print(the_att)
        return the_att

    def savePicture(self, path=None, url_list=None, name=None):
        if path is None or url_list is None or name is None:
            print("Please set path and name and url of picture!")
            return None
        for index, pic_url in enumerate(url_list):
            current_file = path + name +str(index) +'.jpg'
            with open(current_file, 'w') as fd:
                    request.urlretrieve(pic_url, current_file)
            

if __name__ == "__main__":
    bs_obj = BaseSpider()
    bs_obj.setUrl("https://book.douban.com/chart?subcat=F&icn=index-topchart-fiction")
    bs_obj.setXpath('//*[@id="content"]/div/div[1]/ul//div[2]/h2/a')
    bs_obj.getText()
    bs_obj.setXpath('//*[@id="content"]/div/div[1]/ul//div[1]/a/img')
    if bs_obj.returnAttrib('src'):
        print("yes")
    bs_obj.savePicture('./', bs_obj.returnAttrib('src'), 'pic')










