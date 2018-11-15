# -*- coding: utf-8 -*-
import lxml
from goose3 import Goose

url = "http://blog.sina.com.cn/s/blog_49818dcb0102zhny.html"
g = Goose({'browser_user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2)', 'use_meta_langauge': False,
           'target_language': 'en'})
article = g.extract(url=url)
print(article.meta_encoding)
print(type(article.doc))
print(article.doc.xpath('//*'))
result = lxml.etree.tostring(article.doc, encoding="utf-8")
print(result.decode('utf-8'))
