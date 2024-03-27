import scrapy
import sqlite3
import time
import random

class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/deals']

    def __init__(self):
        self.conn = sqlite3.connect('ebay.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products
                            (image TEXT, name TEXT, price TEXT, old_price TEXT, discount TEXT)''')
        self.conn.commit()

    def close(self, reason):
        self.conn.close()

    def parse(self, response):
        products = response.css('.dne-itemtile')
        for product in products:
            image = product.css('.dne-itemtile-imagewrapper a .slashui-image-cntr img::attr(src)').get()
            name = product.css('.dne-itemtile-detail .ebayui-ellipsis-2::text, .dne-itemtile-detail .ebayui-ellipsis-3::text').get()
            price = product.css('.dne-itemtile-detail .first::text').get()
            old_price = product.css('.dne-itemtile-detail .itemtile-price-strikethrough::text').get()
            discount = product.css('.dne-itemtile-detail .itemtile-price-bold::text').get()
            yield {
                'image': image,
                'name': name,
                'price': price,
                'old price': old_price,
                'discount': discount,
            }
            self.cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?)", (image, name, price, old_price, discount))
            self.conn.commit()
            time.sleep(random.uniform(1, 2))