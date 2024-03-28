import sqlite3

class EbayPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('ebay.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products
                            (image TEXT, name TEXT, price TEXT, old_price TEXT, discount TEXT)''')
        self.conn.commit()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?)", (item['image'], item['name'], item['price'], item['old_price'], item['discount']))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
