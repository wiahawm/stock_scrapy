# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class StockscraperPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        time = item.get('time','').strip()
        volume = item.get('volume','').strip()
        price = item.get('price','').strip()
        top_price = item.get('top_price','').strip()
        low_price = item.get('low_price','').strip()
        code = item.get('code', '').strip()

        sql = '''
        INSERT INTO stock_data(id, time, volume, price, top_price, low_price, code) VALUES(null, %s, %s, %s, %s, %s, %s)
        '''
        self.cur.execute(sql, (time, volume, price, top_price, low_price, code))
        self.conn.commit()

    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='mydb', charset='utf8', port=3307)
        self.cur = self.conn.cursor()

        print("DB Connected")

    def createTable(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_data(
            id INT AUTO_INCREMENT PRIMARY KEY,
            time VARCHAR(50),
            volume VARCHAR(50),
            price VARCHAR(50),
            top_price VARCHAR(50),
            low_price VARCHAR(50),
            code VARCHAR(50)
        )
        """)
