# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class OECDLeadersItem(scrapy.Item):
    work = scrapy.Field()         #职位
    name = scrapy.Field()         #姓名
    resume = scrapy.Field()       #简历
    englishname = scrapy.Field()  #组织英文缩写
    url = scrapy.Field()          #领导人连接

class WIPOLeadersItem(scrapy.Item):
    section = scrapy.Field()      #部门
    work = scrapy.Field()         #职位
    name = scrapy.Field()         #姓名
    englishname = scrapy.Field()  # 组织英文缩写
    url = scrapy.Field()          # 领导人连接

class UNDPLeadersItem(scrapy.Item):
    work = scrapy.Field()         #职位
    name = scrapy.Field()         #姓名
    resume = scrapy.Field()       #简历
    englishname = scrapy.Field()  #组织英文缩写
    url = scrapy.Field()          #领导人连接
