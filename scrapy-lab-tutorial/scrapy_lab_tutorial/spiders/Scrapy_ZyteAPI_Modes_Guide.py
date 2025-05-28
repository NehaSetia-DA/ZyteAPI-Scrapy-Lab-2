# ==============================================================================
# SIMPLE GUIDE: 3 MODES OF ZYTE API WITH SCRAPY
# ==============================================================================

"""
🎯 THREE WAYS TO USE ZYTE API:

1. TRANSPARENT MODE  → All requests automatically use Zyte API
2. AUTOMAP MODE     → Choose per request, automatic parameters  
3. MANUAL MODE      → Full control over every parameter

Each mode gives you different levels of control and complexity.
"""

# ==============================================================================
# BASIC SETUP (Same for all modes)
# ==============================================================================

# settings.py
ZYTE_API_KEY = "your_api_key_here"
# The Addon enables transparent mode by default!
ADDONS = {
    "scrapy_zyte_api.Addon": 500,
}

# requirements.txt
# scrapy>=2.10.0
# scrapy-zyte-api>=0.14.0

# ==============================================================================
# MODE 1: TRANSPARENT MODE 🌐
# ==============================================================================

"""
🌐 TRANSPARENT MODE: "Set and Forget"

WHAT IT DOES:
- Every request automatically uses Zyte API
- No changes needed to your existing parsing code
- Simplest way to add Zyte API to existing spiders

WHEN TO USE:
✅ Converting existing spiders quickly
✅ All pages need the same treatment
✅ You want the simplest possible setup
"""

import scrapy

class TransparentSpider(scrapy.Spider):
    name = "transparent"
    start_urls = ["https://quotes.toscrape.com/js/"]
    
    # The Addon enables transparent mode by default!
    # All requests will automatically use Zyte API, you can put it in the custom_settings here if you want to override the default settings in settings.py file
    # custom_settings = {
    #     'ADDONS': {'scrapy_zyte_api.Addon': 500},
    # }

    def parse(self, response):
        # Same parsing code as always - no changes needed!
        quotes = response.css('div.quote')
        
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'mode': 'transparent'
            }

# Result: All requests automatically use Zyte API


# ==============================================================================
# MODE 2: AUTOMAP MODE ⚡ (Automatic Request Parameters)
# ==============================================================================

"""
⚡ AUTOMAP MODE: "Smart Per-Request Control"

WHAT IT DOES:
- Choose which requests use Zyte API
- Automatic parameter mapping based on your request
- Can enhance requests with specific features

WHEN TO USE:
✅ Different pages need different handling
✅ Want to optimize costs (selective usage)
✅ Need some requests to use browser rendering
"""

import scrapy

class AutomapSpider(scrapy.Spider):
    name = "automap"
    
    custom_settings = {
        'ADDONS': {'scrapy_zyte_api.Addon': 500},
        'ZYTE_API_TRANSPARENT_MODE': False,  # Turn off transparent mode
    }

    def start_requests(self):
        # Request 1: Basic Zyte API usage
        yield scrapy.Request(
            url="https://quotes.toscrape.com/",
            meta={'zyte_api_automap': True},  # ← Use Zyte API with automatic parameters
            callback=self.parse
        )
        
        # Request 2: JavaScript page with browser rendering
        yield scrapy.Request(
            url="https://quotes.toscrape.com/js/",
            meta={
                'zyte_api_automap': {
                    'browserHtml': True,  # ← Need browser for JavaScript
                }
            },
            callback=self.parse
        )
        
        # Request 3: Regular Scrapy (no Zyte API)
        yield scrapy.Request(
            url="https://httpbin.org/json",
            meta={'zyte_api_automap': False},  # ← Use regular Scrapy
            callback=self.parse
        )

    def parse(self, response):
        # Same parsing logic for all responses
        quotes = response.css('div.quote')
        
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'mode': 'automap'
            }

# Result: You control which requests use Zyte API


# ==============================================================================
# MODE 3: MANUAL MODE 🔧
# ==============================================================================

"""
🔧 MANUAL MODE: "Full Control"

WHAT IT DOES:
- Manually specify every Zyte API parameter
- Complete control over request configuration
- Access to advanced features

WHEN TO USE:
✅ Need advanced features (actions, screenshots, etc.)
✅ Production systems with specific requirements
✅ Maximum cost optimization
✅ Complex interactions needed
"""

import scrapy

class ManualSpider(scrapy.Spider):
    name = "manual"
    
    custom_settings = {
        'ADDONS': {'scrapy_zyte_api.Addon': 500},
        'ZYTE_API_TRANSPARENT_MODE': False,
    }

    def start_requests(self):
        # Manual HTTP request
        yield scrapy.Request(
            url="https://quotes.toscrape.com/",
            meta={
                "zyte_api": {
                    "httpResponseBody": True,      # Get HTML content
                    "httpResponseHeaders": True,   # Required for proper decoding
                }
            },
            callback=self.parse
        )
        
        # Manual browser request with advanced features
        yield scrapy.Request(
            url="https://quotes.toscrape.com/js/",
            meta={
                "zyte_api": {
                    "browserHtml": True,     # Browser rendering
                    "screenshot": True,      # Take screenshot
                    "actions": [             # Perform actions
                        {
                            "action": "waitForSelector",
                            "selector": "div.quote",
                            "timeout": 10
                        }
                    ]
                }
            },
            callback=self.parse
        )

    def parse(self, response):
        quotes = response.css('div.quote')
        
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'mode': 'manual'
            }

# Result: Complete control over every Zyte API parameter


# ==============================================================================
# QUICK COMPARISON
# ==============================================================================

"""
📊 MODES COMPARISON:

                TRANSPARENT    AUTOMAP       MANUAL
Setup           Easiest        Medium        Complex
Control         None           Per-request   Complete
Cost Control    Low            Medium        High
Use Case        Quick convert  Mixed needs   Advanced

TRANSPARENT: Just add the Addon, everything uses Zyte API
AUTOMAP:     Choose per request, automatic smart parameters
MANUAL:      Full control, specify every parameter yourself

WHICH TO CHOOSE?
- Learning/prototyping → TRANSPARENT
- Production with mixed needs → AUTOMAP  
- Advanced features needed → MANUAL
"""

# ==============================================================================
# TEST ALL THREE MODES
# ==============================================================================

# Run these commands to test:
# scrapy crawl transparent
# scrapy crawl automap  
# scrapy crawl manual

print("🎯 Three Modes Guide Ready!")
print("📝 Key Points:")
print("   • Transparent: Addon enables this by default")
print("   • Automap: Set zyte_api_automap in Request.meta")
print("   • Manual: Set zyte_api dict in Request.meta")
print("   • Remember: httpResponseBody needs httpResponseHeaders!")
