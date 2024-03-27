import scrapy
import time
import random

class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/deals']

    def parse(self, response):
        products = response.css('.dne-itemtile, .dne-itemtile-detail')
        for product in products:
            image = product.css('.dne-itemtile-imagewrapper a .slashui-image-cntr img::attr(src)').get()
            name = product.css('.ebayui-ellipsis-2::text').get()
            price = product.css('.first::text').get()
            oldprice = product.css('.itemtile-price-strikethrough::text').get()
            discount = product.css('.itemtile-price-bold::text').get()
            yield {
                'image': image,
                'name': name,
                'price': price,
                'old price': oldprice,
                'discount': discount,
            }
        time.sleep(random.uniform(1, 5))
