#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
#解析博文HTML，获取博文时间、标题标签
from bs4 import BeautifulSoup
#解决中文编码问题
import codecs
mdPath = '/Users/zhengquanhai/workspace/blog/csdn/csdn-blog-export/html/md/'
htmlPath = '/Users/zhengquanhai/workspace/blog/csdn/csdn-blog-export/html/'
mdPosts = os.listdir(mdPath)
for postName in mdPosts:
    if postName.endswith('.md'):
        #备份工具得到的文件名像这样：21049457.md，对当前文件夹中.md文件进行操作
        #获取文件名中8位数字，存于prefix中，用于匹配和它对应的HTML文件
        #然后从HTML文件中挖出博文发布时间，保存在timeStamp中
        prefix = postName[:8]
        html = open(htmlPath + prefix + '.html', 'r')
        soup = BeautifulSoup(html)
        print soup
        tag = soup.find_all('span', class_="link_postdate")
        print tag
        timeStamp = tag[0].string.strip()
        #print timeStamp
        timeStamp = timeStamp[:4] + '-' + timeStamp[5:7] + '-' + timeStamp[8:10] + " " + timeStamp[11:]
        #print timeStamp 
        #从HTML中获取博客标题，用于重命名.md文件
        title = soup.find('span', class_="link_title")
        newFileName = title.a.string.strip()
#        pos = temp.index(" - ")
 #       newFileName = temp[:pos]
        #print newFileName

        tags = soup.find('span', class_="link_categories")
        if tags :
            newtags = tags.a.string.strip()
        else :
            newtags = "undefined"
#        pos = temp.index(" - ")
 #       newFileName = temp[:pos]
        #print newtags

        print "---"
        category = soup.select('.category_r span')
        print category
        if len(category) :
            newcategory = category[0].get_text().split('\n')[1]
        else :
            newcategory = "csdn"
#        pos = temp.index(" - ")
 #       newFileName = temp[:pos]
        print newcategory
 
        #将.md中博文读入contents，往contents插入Hexo头部
        #然后写回.md文件
        mdFile = codecs.open(mdPath + postName, "r", 'utf-8')
        contents = mdFile.readlines()
        mdFile.close()
        contents.insert(0, "---\n")
        contents.insert(0, "category: " + newcategory + "\n")
        contents.insert(0, "tags: "+ newtags + "\n")
        contents.insert(0, "date: " + timeStamp + "\n")
        contents.insert(0, "title: " + newFileName + "\n")
        mdFile = codecs.open(postName, "w", 'utf-8')
        newContents = "".join(contents)
        mdFile.write(newContents)
        mdFile.close()
        html.close()
        #重命名.md文件
        os.rename(os.path.join(mdPath, postName), os.path.join(mdPath, newFileName + ".md"))
