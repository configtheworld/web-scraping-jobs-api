import requests as _requests
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://stackoverflow.com/jobs']

    def parse(self, response):
        for title in response.css('.s-link stretched-link'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

        print(response.data)

