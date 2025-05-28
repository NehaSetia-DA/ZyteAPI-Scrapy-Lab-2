import scrapy


class ZyteapiSolutionSpider(scrapy.Spider):
    """
    ✅ SOLUTION: Same spider + 3 lines = works everywhere!
    Handles JavaScript, avoids blocks, more reliable
    """
    name = "zyteapi_solution"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                meta={
                    "zyte_api": {
                        "browserHtml": True,  # 🎯 This is the magic line and key for JS pages!
                    }
                }
            )

    def parse(self, response):
        self.logger.info(f"🌐 Response length: {len(response.text)}")
        
        quotes = response.css('div.quote')
        self.logger.info(f"✅ Quotes found: {len(quotes)}")
        
        if len(quotes) > 0:
            self.logger.info("🎉 SUCCESS! JavaScript rendered with browserHtml!")
        else:
            self.logger.warning("❌ No quotes found - browserHtml might not be working")
        
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'method': 'zyte_api_browser',
            }

