import scrapy
from urllib.parse import urljoin


class Sarabanda(scrapy.Spider):
    allowed_domains = [
        'sarabanda.it'
    ]

    def __init__(self, country, start_urls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.country = country
        self.start_urls = start_urls

    @staticmethod
    def format_price(price, sign="€"):
        return price.split(sign)[0].strip()
    # explain the function

    @staticmethod
    def join_url(url1, url2):
        return urljoin(url1, url2)

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)
        # q:  what will happen if you remove this function?

    def parse(self, response):
        categories_urls = response.xpath(
            '//*[@class="mega-item"]//@href'
        ).extract()
        categories_urls = list(set(categories_urls))
        for category_url in categories_urls:
            category_url = self.join_url(response.url, category_url)
            yield scrapy.Request(
                category_url,
                callback=self.parse_category,
            )

    def parse_category(self, response):
        products = response.xpath(
            "//@data-originalurl"
        ).extract()
        # best variant I could find. no need for set()
        products = set(products)
        for product in products:
            yield scrapy.Request(product,
                                 callback=self.parse_item,
                                 dont_filter=True)

    def parse_item(self, response):
        fields = dict()
        fields["spider"] = self.name
        fields["country"] = self.country

        current_url = response.url
        fields["url"] = current_url

        # main_title: string, represents the title of the product.
        main_title = response.xpath(
            "//*[has-class('product-name')]//text()"
        ).extract_first()
        fields['main_title'] = main_title

        # description: string, product description
        description = response.xpath(
            '//*[@itemprop="description"]//text()'
        ).extract()
        description = [desc.strip() for desc in description if desc.strip()]
        # list comp
        description = "".join(description)
        fields['description'] = description

        # material: string, material of the product.
        material = response.xpath(
            '//*[class="compo-container"]//text()'
        ).extract()
        material = [mat.strip() for mat in material if mat.strip()]
        material = "".join(material)
        # list comp
        fields['material'] = material

        # color: string with current color
        color = response.xpath(
            "//*[@class='current-color']//text()"
        ).extract_first()
        # use @class -> optional. also works with has-class
        fields["color"] = color

        # price: tuple with structured as (current_price, previous_price),
        # the price of the items.
        # previous_price: string, full price of the product.
        # current_price: string, is the discounted price
        # otherwise same as the first element
        current_price = response.xpath(
            "//*[has-class('old-price')]//text()"
        ).extract_first()
        previous_price = response.xpath(
            "//*[has-class('highlighted', 'price')]//text()"
        ).extract_first()
        # use 2 classes with has-class
        previous_price = previous_price if previous_price else current_price
        previous_price = self.format_price(previous_price)
        current_price = self.format_price(current_price)
        # why is working with just one parameter?
        fields["price"] = (current_price, previous_price)

        yield fields


class SarabandaITSpider(Sarabanda):
    name = "sarabanda_it"
    country = "it"
    start_urls = ["https://www.sarabanda.it/en/"]

    def __init__(self):
        super(Sarabanda, self).__init__(
            country=self.country,
            start_urls=self.start_urls
        )
