import scrapy
import sqlite3

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
        # Afficher les résultats de la base de données juste avant de fermer la connexion
        self.print_database_results()
        self.cursor.close()
        self.conn.close()

    def parse(self, response):
        products = response.css('.dne-itemtile')
        for product in products:
            image = product.css('.dne-itemtile-imagewrapper a .slashui-image-cntr img::attr(src)').get()
            name = product.css('.dne-itemtile-detail .ebayui-ellipsis-2::text, .dne-itemtile-detail .ebayui-ellipsis-3::text').get()
            price = product.css('.dne-itemtile-detail .first::text').get()
            old_price = product.css('.dne-itemtile-detail .itemtile-price-strikethrough::text').get()
            discount = product.css('.dne-itemtile-detail .itemtile-price-bold::text').get()
            self.cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?)", (image, name, price, old_price, discount))
            self.conn.commit()

    def print_database_results(self):
        # Afficher les résultats de la base de données
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
