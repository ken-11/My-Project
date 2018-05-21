# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import codecs
import json
import MySQLdb
import pymysql
# from twisted.enterprise import adbapi
from scrapy.conf import settings


class FictionPipeline(object):

    def __init__(self):
        self.file = open('17k.csv', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\r\n'
        self.file.write(line.encode('gbk'))
        return item

    def spider_close(self):
        self.file.close()


class DBPipeline(object):

     def process_item(self, item, spider):
         host = settings['MYSQL_HOST']
         db = settings['MYSQL_DBNAME']
         user = settings['MYSQL_USER']
         passwd = settings['MYSQL_PASSWD']
         charset = 'utf8'
         con = pymysql.connect(host=host, db=db,
                               user=user, passwd=passwd,
                               charset=charset, use_unicode=True)        
                               cur = con.cursor()
         sql = "insert into Qik(top,url,type,name,update_time,author)" \
              " value(%s,%s,%s,%s,%s,%s)"
         params = (item['top'], item['url'], item['type_'],
                 item['name'], item['update_time'], item['author'])
         try:
            cur.execute(sql, params)
         except Exception as e:
            print(e)
            con.rollback()
         else:
            con.commit()
         cur.close()
         con.close()
         return item
