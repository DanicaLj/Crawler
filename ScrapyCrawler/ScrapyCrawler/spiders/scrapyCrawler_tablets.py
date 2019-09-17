# -*- coding: utf-8 -*-
import scrapy


class ScrapycrawlerTabletsSpider(scrapy.Spider):
    name = 'scrapyCrawler_tablets'
    allowed_domains = ['www.ricardo.ch']
    start_urls = ['https://www.ricardo.ch/de/c/kleidung-und-accessoires-40748/']

    custom_settings={ 'FEED_URI': "scrapyCrawler_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract-uje vrednosti pomocu css selektora
        productName=response.css('.ric-article__name::text').extract()

        products=zip(productName)

        for product in products:
            #pravi dictionary da bi smetili proizvode
            scraped_info = {
                'page':response.url,
                'productName' : product[0]
            }

            #yield daje podatke scrapy-ju
            yield scraped_info

            next_page = response.css('.ric-pagination__button + a::attr(href)').extract_first()
            if next_page:
                yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)
