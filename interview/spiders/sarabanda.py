# #1. import the Scrapy library
# from urllib.parse import urljoin

# #2. Create a class called Sarabanda that inherits from  scrapy.Spider
# class .....................:
#     name = 'sarabanda'

#     allowed_domains = [
#         'sarabanda.it'
#     ]

#     def __init__(self, country, start_urls, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.country = country
#         self.start_urls = start_urls

# #3. The following two, format_price and join_url should run as independent methods.
# #Use a decorator to make them into static methods
#     # ............
#     def format_price(price, sign="€"):
#         return price.split(sign)[0].strip()

#     # explain the function

#     # ............
#     def join_url(url1, url2):
#         return urljoin(url1, url2)

#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#         # q:  what will happen if you remove this function?

#     def parse(self, response):
#         categories_urls = response.xpath(
#             '//*[@class="mega-item"]//@href'
#         ).extract()
#         categories_urls = list(set(categories_urls))
#         # what is list(set())
#         for category_url in categories_urls:
#             category_url = self.join_url(response.url, category_url)
#             yield scrapy.Request(
#                 category_url,
#                 callback=self.parse_category,
#             )

#     def parse_category(self, response):
#         products = response.xpath(
# #4..............................................................................
# # Using the previous xpath as an example write the one that would fit here
#         ).extract()
# #5. Why is the products list converted to a set?
#         products = set(products)
#         for product in products:
#             yield scrapy.Request(product,
#                                  callback=self.parse_item,
#                                  dont_filter=True)

#     def parse_item(self, response):
#         fields = dict()
#         fields["spider"] = self.name
#         fields["country"] = self.country

#         current_url = response.url
#         fields["url"] = current_url

#         # main_title: string, represents the title of the product.
#         main_title = response.xpath(
# #6..............................................................................
# # Using the previous xpath as an example write the one that would fit here.
# # and instead of @href, you will be using text()
#         ).extract_first()
#         fields['main_title'] = main_title

#         # description: string, product description
#         description = response.xpath(
#             '//*[@itemprop="description"]//text()'
#         ).extract()

# #7.Convert description list to string and remove all backslash characters using .join(), .replace() and .strip()
# #.................................................................................

#         # material: string, material of the product.
#         material = response.xpath(
# #8.................................................................................
# # Using the previous xpath as an example write the one that would fit here.
#         ).extract()

# # Convert material list to string and remove all unnecessary characters
# #9................................................................................


#         # color: string with current color
#         color = response.xpath(
# #10................................................................................
#          # Using the previous xpath as an example write the one that would fit here.
#         ).extract_first()
#         fields["color"] = color

#         # price: tuple with structured as (current_price, previous_price),
#         # the price of the items.
#         # previous_price: string, full price of the product.
#         # current_price: string, is the discounted price
#         # otherwise same as the first element
#         current_price = response.xpath(
# #11................................................................................
# # Using the previous xpath as an example write the one that would fit here.
#         ).extract_first()
#         previous_price = response.xpath(
# #12................................................................................
# # Using the previous xpath as an example write the one that would fit here.
#         ).extract_first()

#         previous_price = previous_price if previous_price else current_price
#         previous_price = self.format_price(previous_price)
#         current_price = self.format_price(current_price)

#         fields["price"] = (current_price, previous_price)

#         yield fields

# #13. Make a subclass called SarabandaIT
# # Requirements:
# # - Inherits Sarabanda
# # - Has an __init__ method that fits the parents' class __init__ method
# # - Has the following attributes:
# # name: "sarabanda_it",
# # country: "it",
# # start_urls: ["https://www.sarabanda.it/it/"]


# ................................................................................
