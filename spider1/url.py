import scrapy

class NewSpider(scrapy.Spider):
    name = "New_spider"
    start_urls = ['http://192.168.242.171/hr2/']
    def parse(self, response):
        for x in response.css('img'):
            yield {
                'Image Link': x.xpath('@src').extract_first(),
            }
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoim(next_page),
                    callback=self.parse
                )