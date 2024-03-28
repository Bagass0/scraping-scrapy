import scrapy

class EbayItem(scrapy.Item):
    image = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    discount = scrapy.Field()
