import scrapy
from scrapy import Request

class MarisfrolgSpider(scrapy.Spider):
    name = 'marisfrolg'

    allowed_domains = ['marisfrolg.com', ]

    def __init__(self, country, start_urls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.country = country
        self.start_urls = start_urls

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        categories = response.xpath(
            '//*[contains(@href, "category")]/@href'
        ).extract()
        for category in set(categories):
            yield Request(response.urljoin(category),
                          callback=self.parse_category)

    def parse_category(self, response):
        products = response.xpath(
            '//*[contains(@class, "row")]//*[contains(@href, "goods")]/@href'
        ).extract()
        for product in set(products):
            yield Request(response.urljoin(product),
                          callback=self.parse_item
                          )

    def parse_item(self, response):

        loader = {}

        current_url = response.url
        loader["url"] = current_url

        main_title = response.xpath(
            '//*[contains(@class, "title")]/text()'
        ).extract_first()
        loader["main_title"] = main_title

        price = response.xpath(
            '//*[contains(@id, "SHOPPRICE")]/text()'
        ).extract_first()
        price_tuple = (price, price)
        loader["price"] = price_tuple

        material = response.xpath(
            '//*[contains(@id, "collapse3")]//text()'
        ).extract()
        material = " ".join(material).strip()
        loader["material"] = material

        yield loader


class MarisfrolgCNSpider(MarisfrolgSpider):
    name = 'marisfrolg_cn'
    country = 'cn'
    start_urls = ['http://www.marisfrolg.com/cn/', ]

    def __init__(self, *args, **kwargs):
        super(MarisfrolgCNSpider, self).__init__(
            country=self.country,
            start_urls=self.start_urls,
            *args, **kwargs
        )
