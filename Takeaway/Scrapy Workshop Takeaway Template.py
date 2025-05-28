# ==============================================================================
# 🎁 SCRAPY + ZYTE API WORKSHOP TAKEAWAY GIFT
# Template to Try Zyte API on YOUR Website
# ==============================================================================

"""
🎉 CONGRATULATIONS! You completed the Scrapy + Zyte API workshop!

This template is your takeaway gift - use it to try Zyte API on any website.
Just follow the steps below and you'll have a working spider in minutes!

🎯 WHAT YOU'LL GET:
✅ Convert any website scraping to use Zyte API
✅ Handle JavaScript-heavy sites automatically  
✅ Bypass anti-bot protection
✅ Professional-grade scraping setup

🚀 LET'S GET STARTED!
"""

# ==============================================================================
# STEP 1: QUICK SETUP (Copy these files to your project)
# ==============================================================================

# requirements.txt
"""
scrapy>=2.10.0
scrapy-zyte-api>=0.14.0
"""

# .env (Create this file and add your API key)
"""
ZYTE_API_KEY=your_zyte_api_key_here
"""

# settings.py
"""
BOT_NAME = 'my_zyte_project'

# Import your API key
import os
from dotenv import load_dotenv
load_dotenv()

ZYTE_API_KEY = os.getenv('ZYTE_API_KEY')

# Enable Zyte API
ADDONS = {
    "scrapy_zyte_api.Addon": 500,
}

# Basic settings
ROBOTSTXT_OBEY = True
USER_AGENT = 'my_zyte_project (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 1
"""

# ==============================================================================
# STEP 2: CHOOSE YOUR TEMPLATE
# ==============================================================================

"""
📋 CHOOSE THE RIGHT TEMPLATE FOR YOUR WEBSITE:

🌐 Template A: SIMPLE WEBSITES (regular HTML)
   → Use for: Blogs, news sites, simple e-commerce

⚡ Template B: JAVASCRIPT WEBSITES (dynamic content)  
   → Use for: SPAs, React sites, heavy JavaScript

🔧 Template C: PROTECTED WEBSITES (anti-bot, forms)
   → Use for: Sites that block scrapers, require login

🎯 Template D: MIXED CONTENT (some pages JS, some not)
   → Use for: Large sites with different page types
"""

# ==============================================================================
# TEMPLATE A: SIMPLE WEBSITES 🌐
# ==============================================================================

import scrapy

class MySimpleSpider(scrapy.Spider):
    """
    🌐 FOR SIMPLE HTML WEBSITES
    Use this template for regular websites without heavy JavaScript
    """
    name = "my_simple_spider"
    
    # 📝 STEP 1: Replace with your website
    start_urls = [
        "https://YOUR_WEBSITE_HERE.com",         # ← Replace this!
        "https://YOUR_WEBSITE_HERE.com/page2",   # ← Add more URLs
    ]
    
    # ✨ Transparent mode - all requests use Zyte API automatically
    custom_settings = {
        'ADDONS': {'scrapy_zyte_api.Addon': 500},
        # Transparent mode is enabled by default with the Addon
    }

    def parse(self, response):
        """
        📝 STEP 2: Update extraction logic with your CSS selectors
        """
        
        # 🎯 CUSTOMIZE THESE SELECTORS FOR YOUR WEBSITE:
        items = response.css('YOUR_ITEM_SELECTOR')  # ← e.g., 'div.product', 'article', etc.
        
        self.logger.info(f"Found {len(items)} items on {response.url}")
        
        for item in items:
            yield {
                # 📝 STEP 3: Replace with your data fields
                'title': item.css('YOUR_TITLE_SELECTOR::text').get(),           # ← e.g., 'h2::text'
                'price': item.css('YOUR_PRICE_SELECTOR::text').get(),           # ← e.g., '.price::text' 
                'description': item.css('YOUR_DESC_SELECTOR::text').get(),      # ← e.g., 'p.desc::text'
                'link': item.css('YOUR_LINK_SELECTOR::attr(href)').get(),       # ← e.g., 'a::attr(href)'
                'image': item.css('YOUR_IMAGE_SELECTOR::attr(src)').get(),      # ← e.g., 'img::attr(src)'
                
                # Metadata
                'scraped_from': response.url,
                'scraped_with': 'zyte_api',
            }
        
        # 📝 STEP 4: Add pagination handling if needed
        next_page = response.css('YOUR_NEXT_PAGE_SELECTOR::attr(href)').get()  # ← e.g., 'a.next::attr(href)'
        if next_page:
            yield response.follow(next_page, self.parse)

# Test with: scrapy crawl my_simple_spider


# ==============================================================================
# TEMPLATE B: JAVASCRIPT WEBSITES ⚡
# ==============================================================================

import scrapy

class MyJavaScriptSpider(scrapy.Spider):
    """
    ⚡ FOR JAVASCRIPT-HEAVY WEBSITES
    Use this template for SPAs, React sites, or sites requiring browser rendering
    """
    name = "my_js_spider"
    
    custom_settings = {
        'ADDONS': {'scrapy_zyte_api.Addon': 500},
        'ZYTE_API_TRANSPARENT_MODE': False,  # We'll control per request
    }

    def start_requests(self):
        """Generate requests with browser rendering"""
        
        urls = [
            "https://YOUR_JS_WEBSITE_HERE.com",      # ← Replace this!
            "https://YOUR_JS_WEBSITE_HERE.com/spa",  # ← Add more URLs
        ]
        
        for url in urls:
            yield scrapy.Request(
                url=url,
                meta={
                    "zyte_api": {
                        "browserHtml": True,    # ✨ Browser rendering for JavaScript
                        "screenshot": True,     # 📸 Bonus: get screenshots
                    }
                }
            )

    def parse(self, response):
        """Extract data from JavaScript-rendered pages"""
        
        # 🎯 CUSTOMIZE THESE SELECTORS FOR YOUR WEBSITE:
        items = response.css('YOUR_JS_ITEM_SELECTOR')  # ← Often different from server-side HTML
        
        self.logger.info(f"Found {len(items)} JS-rendered items on {response.url}")
        
        for item in items:
            yield {
                # 📝 UPDATE WITH YOUR DATA FIELDS:
                'title': item.css('YOUR_TITLE_SELECTOR::text').get(),
                'content': item.css('YOUR_CONTENT_SELECTOR::text').get(),
                'data_attribute': item.css('YOUR_SELECTOR::attr(data-id)').get(),  # JS apps often use data attributes
                
                # Metadata
                'scraped_from': response.url,
                'scraped_with': 'zyte_api_browser',
                'has_screenshot': True,
            }

# Test with: scrapy crawl my_js_spider


# ==============================================================================
# TEMPLATE C: PROTECTED WEBSITES 🔧
# ==============================================================================

import scrapy

class MyProtectedSpider(scrapy.Spider):
    """
    🔧 FOR PROTECTED/ANTI-BOT WEBSITES
    Use this template for sites that block regular scrapers
    """
    name = "my_protected_spider"
    
    custom_settings = {
        'ADDONS': {'scrapy_zyte_api.Addon': 500},
        'ZYTE_API_TRANSPARENT_MODE': False,
    }

    def start_requests(self):
        """Advanced requests with anti-bot circumvention"""
        
        yield scrapy.Request(
            url="https://YOUR_PROTECTED_WEBSITE.com",  # ← Replace this!
            meta={
                "zyte_api": {
                    "browserHtml": True,
                    "geolocation": "US",        # 🌍 Geographic targeting if needed
                    "requestHeaders": {
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    },
                    "actions": [                # 🎭 Advanced interactions
                        {
                            "action": "waitForSelector",
                            "selector": "YOUR_CONTENT_SELECTOR",  # ← Wait for content to load
                            "timeout": 10
                        },
                        {
                            "action": "scroll",
                            "coordinate": [0, 1000]  # Scroll down to trigger lazy loading
                        }
                    ]
                }
            }
        )

    def parse(self, response):
        """Extract data from protected sites"""
        
        items = response.css('YOUR_PROTECTED_ITEM_SELECTOR')  # ← Update this
        
        self.logger.info(f"Bypassed protection! Found {len(items)} items")
        
        for item in items:
            yield {
                'title': item.css('YOUR_TITLE_SELECTOR::text').get(),
                'content': item.css('YOUR_CONTENT_SELECTOR::text').get(),
                
                # Metadata
                'scraped_from': response.url,
                'scraped_with': 'zyte_api_protected',
                'bypassed_protection': True,
            }

# Test with: scrapy crawl my_protected_spider


# ==============================================================================
# TEMPLATE D: MIXED CONTENT WEBSITES 🎯
# ==============================================================================

import scrapy

class MyMixedSpider(scrapy.Spider):
    """
    🎯 FOR MIXED CONTENT WEBSITES
    Use this template for sites with both simple and JavaScript pages
    """
    name = "my_mixed_spider"
    
    custom_settings = {
        'ADDONS': {'scrapy_zyte_api.Addon': 500},
        'ZYTE_API_TRANSPARENT_MODE': False,
    }

    def start_requests(self):
        """Smart request routing based on page type"""
        
        # Simple pages - use HTTP (faster, cheaper)
        simple_pages = [
            "https://YOUR_SITE.com/blog",          # ← Replace with your simple pages
            "https://YOUR_SITE.com/about",
        ]
        
        for url in simple_pages:
            yield scrapy.Request(
                url=url,
                meta={'zyte_api_automap': True},     # Basic Zyte API
                callback=self.parse_simple
            )
        
        # JavaScript pages - use browser rendering
        js_pages = [
            "https://YOUR_SITE.com/products",      # ← Replace with your JS pages
            "https://YOUR_SITE.com/search",
        ]
        
        for url in js_pages:
            yield scrapy.Request(
                url=url,
                meta={
                    'zyte_api_automap': {
                        'browserHtml': True
                    }
                },
                callback=self.parse_javascript
            )

    def parse_simple(self, response):
        """Parse simple HTML pages"""
        # 📝 UPDATE FOR YOUR SIMPLE PAGES:
        items = response.css('YOUR_SIMPLE_SELECTOR')  # ← e.g., 'article'
        
        for item in items:
            yield {
                'title': item.css('h2::text').get(),           # ← Update selectors
                'content': item.css('p::text').get(),
                'page_type': 'simple_html',
            }

    def parse_javascript(self, response):
        """Parse JavaScript-rendered pages"""
        # 📝 UPDATE FOR YOUR JS PAGES:
        items = response.css('YOUR_JS_SELECTOR')      # ← e.g., '[data-testid="product"]'
        
        for item in items:
            yield {
                'name': item.css('.product-name::text').get(),  # ← Update selectors
                'price': item.css('.price::text').get(),
                'page_type': 'javascript_rendered',
            }

# Test with: scrapy crawl my_mixed_spider


# ==============================================================================
# 🛠️ STEP-BY-STEP CUSTOMIZATION GUIDE
# ==============================================================================

"""
📋 HOW TO CUSTOMIZE ANY TEMPLATE:

STEP 1: CHOOSE YOUR TEMPLATE
- Simple HTML site → Template A
- JavaScript/SPA → Template B  
- Gets blocked → Template C
- Mixed content → Template D

STEP 2: UPDATE THE URLS
Replace "YOUR_WEBSITE_HERE" with your actual target URLs

STEP 3: FIND YOUR SELECTORS
1. Open your target website in browser
2. Right-click on data you want → "Inspect Element"  
3. Copy the CSS selector
4. Replace "YOUR_SELECTOR_HERE" with your actual selectors

STEP 4: UPDATE DATA FIELDS
Replace the example fields (title, price, etc.) with what you actually want to extract

STEP 5: TEST AND ITERATE
Run: scrapy crawl your_spider_name
Check the results and adjust selectors as needed

STEP 6: SCALE UP
Once it works, add more URLs and data fields!
"""

# ==============================================================================
# 🧰 HELPFUL TOOLS & COMMANDS
# ==============================================================================

"""
🔧 USEFUL SCRAPY COMMANDS:

# Test your selectors interactively:
scrapy shell "https://your-website.com"
# Then try: response.css('your-selector').get()

# Run spider and save to file:
scrapy crawl your_spider -o results.json

# Run with verbose logging:
scrapy crawl your_spider -L DEBUG

# Test specific URL:
scrapy parse https://your-website.com --spider=your_spider

🎯 CSS SELECTOR TIPS:

Basic selectors:
- 'h1'           → All h1 tags
- '.class-name'  → Elements with class
- '#id-name'     → Element with ID
- 'div.class'    → Div with specific class

Get text/attributes:
- '::text'       → Get text content
- '::attr(href)' → Get href attribute
- '::attr(src)'  → Get src attribute

Multiple elements:
- '.getall()'    → Get all matches (list)
- '.get()'       → Get first match (string)
"""

# ==============================================================================
# 🚨 TROUBLESHOOTING GUIDE
# ==============================================================================

"""
❓ COMMON ISSUES & SOLUTIONS:

❌ "No API key found"
✅ Check your .env file has ZYTE_API_KEY=your_actual_key

❌ "No items found" 
✅ Test your CSS selectors in browser dev tools first
✅ Try browserHtml=True if site uses JavaScript

❌ "Request failed"
✅ Check if website blocks your IP/user-agent  
✅ Try adding requestHeaders or using browserHtml

❌ "Too expensive"
✅ Use automap mode to selectively apply Zyte API
✅ Use httpResponseBody for simple pages, browserHtml only when needed

❌ "Selectors don't work"
✅ Check if content is loaded by JavaScript → use browserHtml
✅ Use browser dev tools to find correct selectors
✅ Try data attributes: [data-testid="product"]

💡 PRO TIPS:
- Start simple, then add complexity
- Test one page first before scaling
- Use scrapy shell to test selectors
- Check robots.txt compliance
- Monitor your API usage/costs
"""

# ==============================================================================
# 🎁 BONUS: READY-TO-USE EXAMPLES
# ==============================================================================

"""
🎁 COPY-PASTE EXAMPLES FOR COMMON SITES:

# E-commerce products:
items = response.css('[data-testid="product"], .product-item, .product-card')
title = item.css('h2::text, .product-title::text, [data-testid="product-name"]::text').get()
price = item.css('.price::text, [data-testid="price"]::text, .product-price::text').get()

# News articles:
articles = response.css('article, .article-item, .news-item')
headline = article.css('h1::text, h2::text, .headline::text').get()
content = article.css('p::text, .article-content::text').getall()

# Blog posts:
posts = response.css('.post, article, .blog-post')
title = post.css('h1::text, h2::text, .post-title::text').get()
author = post.css('.author::text, .by-author::text, [data-author]::text').get()

# Job listings:
jobs = response.css('.job, .job-listing, [data-testid="job"]')
job_title = job.css('h2::text, .job-title::text').get()
company = job.css('.company::text, .employer::text').get()
location = job.css('.location::text, .job-location::text').get()
"""

# ==============================================================================
# 🎉 YOU'RE READY TO GO!
# ==============================================================================

print("🎉 WORKSHOP TAKEAWAY TEMPLATE LOADED!")
print()
print("🎯 NEXT STEPS:")
print("1. Choose your template (A, B, C, or D)")
print("2. Update URLs and selectors")  
print("3. Set your ZYTE_API_KEY in .env file")
print("4. Run: scrapy crawl your_spider_name")
print("5. Enjoy professional web scraping! 🚀")
print()
print("💡 REMEMBER:")
print("- Start simple, then scale up")
print("- Test selectors in browser first")
print("- Use browserHtml for JavaScript sites")
print("- Monitor your API usage")
print()
print("🆘 NEED HELP?")
print("- Check the troubleshooting guide above")
print("- Use scrapy shell to test selectors")
print("- Visit Zyte API documentation")
print()
print("HAPPY SCRAPING! 🎊")
