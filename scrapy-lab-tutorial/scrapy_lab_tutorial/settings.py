# Scrapy settings for scrapy_lab_tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_lab_tutorial"

SPIDER_MODULES = ["scrapy_lab_tutorial.spiders"]
NEWSPIDER_MODULE = "scrapy_lab_tutorial.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_lab_tutorial (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_lab_tutorial.middlewares.ScrapyLabTutorialSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_lab_tutorial.middlewares.ScrapyLabTutorialDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_lab_tutorial.pipelines.ScrapyLabTutorialPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


"""
🔧 ZYTE API CONFIGURATION

📋 WORKSHOP DEMO INSTRUCTIONS:
- For TRADITIONAL SPIDER demo → COMMENT OUT the lines below
- For ZYTE API SPIDER demo → UNCOMMENT the lines below

🔄 Quick Toggle:
- Traditional mode: Comment out ADDONS and ZYTE_API_KEY
- Zyte API mode: Uncomment ADDONS and ZYTE_API_KEY
"""

# 🌐 ENABLE ZYTE API (Uncomment these lines for Zyte API demo)
ADDONS = {
    "scrapy_zyte_api.Addon": 500,
}

# 🔑 ADD YOUR ZYTE API KEY HERE
# Get your free API key at: https://www.zyte.com/zyte-api/
ZYTE_API_KEY = "your_zyte_api_key_here"  # ← Replace with your actual API key

# Example: ZYTE_API_KEY = "1234567890abcdef1234567890abcdef"

# 📝 FOR TRADITIONAL SPIDER DEMO:
# Comment out the ADDONS and ZYTE_API_KEY lines above like this:
# 
# # ADDONS = {
# #     "scrapy_zyte_api.Addon": 500,
# # }
# # ZYTE_API_KEY = "your_zyte_api_key_here"

