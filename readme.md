# CSDN 博客导出工具

一个用python2.7写的博客导出工具，导出为markdown或者html。

# 新增特性
1、修复获取博客页数的bug、去除正文中博文标题  

2、新增脚本**md2hexo.py**将从csdn导出的博客润色满足hexo格式的博客，主要是在.md格式文件头添加一段文件描述，同时将文件名改为博文名。 

## 使用

### 依赖
	
	Python 2.7
		beautifulsoup4

此外，在导出markdown格式的时候使用了开源项目[html2text](https://github.com/aaronsw/html2text)

### 使用方法

1、从csdn导出博客	（注意：博客主题需切回“碧海蓝”，我的“极客世界”主题失效）  

    main.py -u <username> [-f <format>] [-p <page>] [-o <outputDirectory>]
		<format>： html | markdown，缺省为markdown
		<page>为导出特定页面的文章，缺省导出所有文章
		<outputDirectory>暂不可用 

2、导出文件转换为hexo格式  

	1、分别在两个文件下从csdn导出md和html格式的文件
	2、执行md2hexo.py脚本从.html文件中提取出博文标题和博文创建时间，将它们插入.md文件  

效果如下面所示： 

    title: Hello World
    date: 2014-05-27 10:04:08
    tag: 博客
    category: 博客建设
    ---
### Example

如果想导出[http://blog.csdn.net/cecesjtu](http://blog.csdn.net/cecesjtu)的文章，格式为markdown，命令为：

	./main.py -u cecesjtu -f markdown
	or
	./main.py -u cecesjtu

格式为html，命令为：

	./main.py -u cecesjtu -f html

## To Do

1. 导出到指定目录

## Licence

GPLv3