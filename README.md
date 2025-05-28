# 🚀 Scrapy + Zyte API Training Lab: From Traditional to Modern Web Scraping

> **Transform any Scrapy spider to handle JavaScript and anti-bot protection with just 3 lines of code!**
> 
> **The 3 Lines:** Add Zyte API addon + API key in settings.py + browserHtml in request meta

Based on the official [Zyte Web Scraping Tutorial](https://docs.zyte.com/web-scraping/tutorials/main/setup.html), this workshop demonstrates how to modernize your web scraping approach using Scrapy with Zyte API.

## 🎯 What You'll Learn

- **The Problem**: Why traditional Scrapy fails on modern JavaScript-heavy websites
- **The Solution**: How Zyte API seamlessly handles JavaScript rendering and anti-bot protection
- **Three Integration Modes**: Transparent, Automap, and Manual control
- **Hands-on Practice**: Convert traditional spiders to work with any website

---

## 📋 Prerequisites

- Python 3.8+ installed
- Basic knowledge of Scrapy
- A Zyte API key (get one free at [zyte.com](https://www.zyte.com/zyte-api/))

---

## ⚡ Quick Setup

### 1. Clone and Navigate to Project
```bash
git clone <repository-url>
cd Scrapy-ZyteAPI-TrainingLab-2
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv workshop-venv

# Activate it
# On macOS/Linux:
source workshop-venv/bin/activate
# On Windows:
# workshop-venv\Scripts\activate
```

### 3. Install Dependencies
```bash
cd scrapy-lab-tutorial
pip install -r requirements.txt
```

### 4. Configure Your API Key
Edit `scrapy_lab_tutorial/settings.py` and replace the placeholder API key:
```python
ZYTE_API_KEY = "your_actual_api_key_here"  # Replace with your key
```

### 5. Verify Setup
```bash
# Test that everything is working
scrapy list
```

You should see:
```
traditional
zyteapi_solution
```

---

## 🎪 The Core Demo: See the Transformation

### Problem: Traditional Spider Fails
```bash
cd scrapy-lab-tutorial
scrapy crawl traditional
```

**Expected Output:**
```
📄 Response length: 11,000+ characters
📊 Quotes found: 0
⚠️  NO QUOTES FOUND - Page might be JavaScript-rendered!
```

**Why it fails**: The page `https://quotes.toscrape.com/js/` uses JavaScript to load content. Traditional Scrapy only gets the initial HTML, not the JavaScript-rendered content.

### Solution: Zyte API Spider Succeeds
```bash
scrapy crawl zyteapi_solution
```

**Expected Output:**
```
🌐 Response length: 11,000+ characters
✅ Quotes found: 10
🎉 SUCCESS! JavaScript rendered with browserHtml!
```

**Why it works**: Zyte API renders the JavaScript and returns the fully loaded page to Scrapy.

---

## 📁 Project Structure

```
scrapy-lab-tutorial/
├── scrapy_lab_tutorial/
│   ├── spiders/
│   │   ├── traditional.py              # ❌ Fails on JS pages
│   │   ├── zyteapi_solution.py         # ✅ Works everywhere  
│   │   └── Scrapy_ZyteAPI_Modes_Guide.py # 📚 Complete guide to 3 modes
│   └── settings.py                     # 🔧 Zyte API configuration
├── requirements.txt                    # 📦 Dependencies
└── scrapy.cfg                         # ⚙️ Scrapy project config
```

---

## 🔧 Three Ways to Use Zyte API

This workshop includes a comprehensive guide showing three different integration approaches:

### 1. 🌐 Transparent Mode (Easiest)
**What**: All requests automatically use Zyte API
```python
# In settings.py - already configured!
ADDONS = {"scrapy_zyte_api.Addon": 500}
# That's it! All spiders now use Zyte API automatically
```

### 2. ⚡ Automap Mode (Selective)
**What**: Choose per request, automatic parameters
```python
yield scrapy.Request(
    url="https://quotes.toscrape.com/js/",
    meta={'zyte_api_automap': {'browserHtml': True}},
    callback=self.parse
)
```

### 3. 🔧 Manual Mode (Full Control)
**What**: Complete control over every parameter
```python
yield scrapy.Request(
    url="https://quotes.toscrape.com/js/",
    meta={
        "zyte_api": {
            "browserHtml": True,
            "screenshot": True,
            "actions": [{"action": "waitForSelector", "selector": "div.quote"}]
        }
    },
    callback=self.parse
)
```

**View the complete guide**: Check `scrapy_lab_tutorial/spiders/Scrapy_ZyteAPI_Modes_Guide.py` for detailed examples of all three modes.

---

## 🛠 Hands-On Exercise

### Convert Your Own Spider

1. **Start with a traditional spider** that targets a JavaScript-heavy site
2. **Test it first** to see it fail: `scrapy crawl your_spider`
3. **Add the three magic lines**:
   
   **In `settings.py`:**
   ```python
   ADDONS = {"scrapy_zyte_api.Addon": 500}        # Line 1
   ZYTE_API_KEY = "your_actual_api_key_here"      # Line 2
   ```
   
   **In your spider:**
   ```python
   def start_requests(self):
       for url in self.start_urls:
           yield scrapy.Request(
               url=url,
               meta={"zyte_api": {"browserHtml": True}},  # Line 3
               callback=self.parse
           )
   ```
4. **Test again** and see it succeed!

### Practice Sites
- `https://quotes.toscrape.com/js/` (JavaScript quotes)
- `https://quotes.toscrape.com/js/page/2/` (Pagination)
- Any modern SPA (Single Page Application)

---

## 🎯 Key Takeaways

### The 3-Line Transformation
```python
# Step 1: Add to settings.py
ADDONS = {"scrapy_zyte_api.Addon": 500}        # Line 1: Enable Zyte API addon
ZYTE_API_KEY = "your_actual_api_key_here"      # Line 2: Set your API key

# Step 3: Add to your spider's start_requests method
yield scrapy.Request(
    url=url,
    meta={"zyte_api": {"browserHtml": True}},   # Line 3: Enable browser rendering
    callback=self.parse
)
```

**That's it! Three lines transform any spider from failing on JavaScript to working everywhere.**

### When to Use Zyte API
✅ **Use Zyte API when:**
- Target site uses JavaScript/React/Vue/Angular
- Getting blocked by anti-bot protection
- Need reliable, scalable scraping
- Want to avoid proxy management

✅ **Stick with traditional Scrapy when:**
- Simple static HTML sites
- Internal/friendly APIs
- Cost is a major concern
- Learning/prototyping

---

## 🎁 Workshop Takeaway: Ready-to-Use Templates

After completing this workshop, you get a **comprehensive takeaway gift** - professional spider templates you can immediately use on your own projects!

### 📁 What's Included: `Takeaway/Scrapy Workshop Takeaway Template.py`

**Four Production-Ready Templates:**

#### 🌐 **Template A: Simple Websites**
- For regular HTML sites (blogs, news, basic e-commerce)
- Uses transparent mode for automatic Zyte API integration
- Perfect for sites without heavy JavaScript

#### ⚡ **Template B: JavaScript Websites** 
- For SPAs, React sites, dynamic content
- Includes browser rendering with `browserHtml: True`
- Handles modern JavaScript-heavy applications

#### 🔧 **Template C: Protected Websites**
- For sites with anti-bot protection
- Advanced features: geolocation, custom headers, browser actions
- Bypasses common blocking mechanisms

#### 🎯 **Template D: Mixed Content**
- Smart routing for sites with both simple and JS pages
- Cost-optimized: uses HTTP for simple pages, browser for JS
- Perfect for large sites with varied content types

### 🛠 How to Use the Templates

1. **Copy the template** that matches your target website type
2. **Replace placeholders** with your actual URLs and CSS selectors
3. **Update data fields** to match what you want to extract
4. **Test and iterate** until you get perfect results

### 💡 Bonus Features Included

- **Step-by-step customization guide**
- **CSS selector examples** for common site types (e-commerce, news, blogs, jobs)
- **Troubleshooting guide** with solutions to common issues
- **Pro tips** for cost optimization and scaling
- **Ready-to-copy examples** for popular website patterns

### 🎯 From Workshop to Production

The takeaway templates bridge the gap between learning and real-world application. You'll have:

✅ **Professional-grade setup** with proper error handling  
✅ **Cost optimization** strategies for different page types  
✅ **Scalable architecture** that grows with your needs  
✅ **Best practices** learned from production scraping  

**Location**: Check the `Takeaway/` folder for your complete template collection!

---

## 📚 Additional Resources

- **Official Documentation**: [Scrapy-Zyte-API Docs](https://scrapy-zyte-api.readthedocs.io/)
- **Zyte API Guide**: [Web Scraping Tutorial](https://docs.zyte.com/web-scraping/tutorials/main/setup.html)
- **Community Support**: [Scrapy Discord](https://discord.gg/scrapy)
- **Advanced Features**: Browser actions, screenshots, geolocation, custom headers

---

## 🚨 Troubleshooting

### Common Issues

**1. "No quotes found" with Zyte API spider**
- Check your API key in `settings.py`
- Verify your account has credits
- Ensure `browserHtml: True` is set for JavaScript pages

**2. "ImportError: No module named scrapy_zyte_api"**
```bash
pip install scrapy-zyte-api
```

**3. "API key not found"**
- Make sure `ZYTE_API_KEY` is set in `settings.py`
- Check for typos in your API key

**4. Spider not found**
```bash
# Make sure you're in the right directory
cd scrapy-lab-tutorial
scrapy list  # Should show available spiders
```

---

## 🎊 Success Criteria

By the end of this workshop, you should be able to:
- [ ] Run both traditional and Zyte API spiders
- [ ] See the clear difference in results (0 vs 10 quotes)
- [ ] Understand the three integration modes
- [ ] Convert any existing spider to use Zyte API
- [ ] Know when to use Zyte API vs traditional Scrapy

---


**🎯 Workshop Goal**: Transform your web scraping from fragile and limited to robust and scalable - with the same elegant Scrapy code you already know! 