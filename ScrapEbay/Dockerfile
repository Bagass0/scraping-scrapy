FROM python

WORKDIR /app

RUN pip install --no-cache-dir scrapy

COPY . .

CMD scrapy runspider ScrapEbay/spiders/ebay_spider.py