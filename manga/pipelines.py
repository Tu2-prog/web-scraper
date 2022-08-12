# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class MangaPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("mymanga.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""
                DROP TABLE IF EXISTS manga_tb
        """)
        self.curr.execute("""create table manga_tb(
            title text,
            views number,
            chapter text
        )   
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipelines :" + item["title"])
        return item

    def store_db(self, item):
        self.curr.execute("""insert into manga_tb values (?, ?, ?)""",(
            item["title"],
            item["views"],
            item["chapter"]
        ))
        self.conn.commit()
