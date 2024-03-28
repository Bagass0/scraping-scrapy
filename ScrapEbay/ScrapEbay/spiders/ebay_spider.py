import scrapy
from ScrapEbay.items import EbayItem

class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/deals']

    def parse(self, response):
        products = response.css('.dne-itemtile')
        for product in products:
            item = EbayItem()
            item['image'] = product.css('.dne-itemtile-imagewrapper a .slashui-image-cntr img::attr(src)').get()
            item['name'] = product.css('.dne-itemtile-detail .ebayui-ellipsis-2::text, .dne-itemtile-detail .ebayui-ellipsis-3::text').get()
            item['price'] = product.css('.dne-itemtile-detail .first::text').get()
            item['old_price'] = product.css('.dne-itemtile-detail .itemtile-price-strikethrough::text').get()
            item['discount'] = product.css('.dne-itemtile-detail .itemtile-price-bold::text').get()
            yield item