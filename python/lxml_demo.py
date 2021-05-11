#!/usr/bin/python
#coding:utf-8

from lxml import etree

root = etree.Element("root")
print root.tag  #root
root.append(etree.Element("title"))
print etree.tostring(root, pretty_print=True)
print list(root)    #[<class E root at 0x??>, <class E title at 0x??>]
root.insert(1,etree.Element("body"))
print root[0].tag   #title
print root[0].getparent().tag   #root
print root[0].getnext().tag #body
print root[1].getprevious().tag #title
root[1].append(etree.Element("chapter1", src="baidu.com"))
print root[1][0].tag    #chapter1
print root[1][0].get("src")   #baidu.com
root[1][0].set("id", '1')
print root[1][0].keys()     #['src','id']
print root[1][0].attrib    #{'src':'baidu.com','id':'1'}
root[1][0].text = "hello world!"
print root[1][0].text    #hello world
print root.xpath("//text()")   #[hello world]
for i in  root.iter():
    print i.tag #打印所有tag
for i in  root.iter("chapter1"):
    print i.tag #chapter1
print etree.tostring(root, method="text", encoding='utf-8')   #打印多有text

xml = "<root>data</root>"
root = etree.XML(xml)
root = etree.fromstring(xml)

tree = etree.parse(fd)





