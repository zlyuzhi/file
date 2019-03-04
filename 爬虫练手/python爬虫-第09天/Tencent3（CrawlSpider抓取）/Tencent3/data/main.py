#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline
#cmdline.execute(["scrapy", "crawl", "tencent_crawl"])
cmdline.execute("scrapy crawl tencent_crawl".split(" "))
