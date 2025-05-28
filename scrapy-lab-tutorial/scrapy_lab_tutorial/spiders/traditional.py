import scrapy


# class TraditionalSpider(scrapy.Spider):
#     name = "traditional"
#     allowed_domains = ["quotes.toscrape.com"]
#     start_urls = ["https://quotes.toscrape.com/js/"]

#     def parse(self, response):
#         pass



import scrapy

class TraditionalSpider(scrapy.Spider):
    """
    🚫 PROBLEM: Traditional spider that often gets blocked
    Try this on JavaScript-heavy sites - it will fail!
    """
    name = "traditional"
    start_urls = [
        "https://quotes.toscrape.com/js/",  # JavaScript-rendered page
    ]

    def parse(self, response):
        self.logger.info(f"📄 Response length: {len(response.text)}")
        
        # Try to extract quotes
        quotes = response.css('div.quote')
        self.logger.info(f"📊 Quotes found: {len(quotes)}")
        
        if len(quotes) == 0:
            self.logger.warning("⚠️  NO QUOTES FOUND - Page might be JavaScript-rendered!")
            self.logger.warning("⚠️  Or we might be getting blocked...")
        
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'method': 'traditional_scrapy',
                'success': len(quotes) > 0,
            }
