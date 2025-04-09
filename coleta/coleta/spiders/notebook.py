import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = [
        "https://lista.mercadolivre.com.br/notebook?sb%5C=rb%5C#D\[A:notebook\]"]

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('a.poly-component__title::text').get(),
                'seller': product.css('span.poly-component__seller::text').get(),
                'review_ratings_number': product.css('span.poly-reviews__rating::text').get(),
                'reviews_amount': product.css('span.poly-reviews__total::text').get()
            }
