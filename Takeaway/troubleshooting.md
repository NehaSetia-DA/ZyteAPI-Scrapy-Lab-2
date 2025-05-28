# 🔧 Workshop Troubleshooting Guide

Common issues and solutions for the Scrapy + Zyte API workshop.

---

## 🚨 Setup Issues

### ❌ "Module not found: scrapy"
**Problem**: Scrapy not installed or virtual environment not activated

**Solutions**:
```bash
# Check if virtual environment is active
which python  # Should show venv path

# If not active:
source scrapy-workshop/bin/activate

# Install missing packages:
pip install -r setup/requirements.txt
```

### ❌ "Module not found: scrapy_zyte_api"
**Problem**: Zyte API addon not installed

**Solutions**:
```bash
pip install scrapy-zyte-api
# Or reinstall everything:
pip install -r setup/requirements.txt
```

### ❌ "No module named 'dotenv'"
**Problem**: python-dotenv not installed

**Solutions**:
```bash
pip install python-dotenv
```

---

## 🔑 API Key Issues

### ❌ "ZYTE_API_KEY not set"
**Problem**: API key not configured

**Solutions**:
```bash
# Method 1: Check .env file exists
ls -la .env
cat .env  # Should contain ZYTE_API_KEY=your_actual_key

# Method 2: Set environment variable
export ZYTE_API_KEY="your_actual_key_here"

# Method 3: Copy from example
cp env.example .env
# Then edit .env file
```

### ❌ "401 Unauthorized" from Zyte API
**Problem**: Invalid API key

**Solutions**:
- Get new API key from https://app.zyte.com/
- Check for extra spaces or quotes in .env file
- Verify key has correct permissions

### ❌ "403 Forbidden" from Zyte API
**Problem**: API quota exceeded or account issue

**Solutions**:
- Check account status at https://app.zyte.com/
- Wait for quota reset
- Contact Zyte support if needed

---

## 🕷️ Spider Issues

### ❌ "No such spider: traditional"
**Problem**: Spider not found or wrong directory

**Solutions**:
```bash
# Check current directory
pwd  # Should be in workshop root

# List available spiders
scrapy list

# Check spider files exist
ls spiders/

# Run from correct location
cd /path/to/workshop
scrapy crawl traditional
```

### ❌ Spider runs but finds 0 items (traditional spider)
**Expected behavior**: This is the point! Traditional spider should fail on JS pages.

**Verification**:
```bash
# This should fail (0 quotes):
scrapy crawl traditional

# This should succeed (10 quotes):
scrapy crawl solution
```

### ❌ Both spiders find 0 items
**Problem**: Website might be down or changed

**Solutions**:
```bash
# Test website manually
curl -s https://quotes.toscrape.com/js/ | grep -c "quote"

# Try alternative test site
# Edit spider start_urls to use backup site
```

---

## 🌐 Network Issues

### ❌ "Connection timeout" or "DNS error"
**Problem**: Network connectivity issues

**Solutions**:
```bash
# Test internet connection
ping google.com

# Test specific site
curl -I https://quotes.toscrape.com/

# Use different DNS if needed
# Or try from different network
```

### ❌ "SSL Certificate verification failed"
**Problem**: Corporate firewall or SSL issues

**Solutions**:
```bash
# Temporary workaround (not recommended for production):
export PYTHONHTTPSVERIFY=0

# Or add to spider settings:
# DOWNLOAD_HANDLERS = {
#     'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
# }
```

---

## 💻 Platform-Specific Issues

### 🪟 Windows Issues

#### "Command not found: source"
```bash
# Use this instead of 'source':
scrapy-workshop\Scripts\activate
```

#### Path separator issues
```bash
# Use backslashes in Windows paths:
python setup\test_setup.py
```

### 🍎 macOS Issues

#### Permission denied errors
```bash
# Use --user flag if needed:
pip install --user -r setup/requirements.txt
```

### 🐧 Linux Issues

#### Python version conflicts
```bash
# Specify Python version:
python3 -m venv scrapy-workshop
python3 -m pip install -r setup/requirements.txt
```

---

## 🎓 Workshop-Specific Issues

### ❌ Template spider not working
**Problem**: Attendee hasn't customized selectors properly

**Debugging steps**:
```bash
# Test selectors in Scrapy shell:
scrapy shell "https://target-website.com"
response.css('div.quote').get()  # Test if selector works

# Check for JavaScript requirement:
# If empty, try with Zyte API:
fetch('https://target-website.com', {'zyte_api_automap': True})
```

### ❌ "Can't modify template"
**Problem**: File permissions or git conflicts

**Solutions**:
```bash
# Check file permissions:
ls -la spiders/04_template.py

# Reset from git:
git checkout spiders/04_template.py

# Copy to new file:
cp spiders/04_template.py spiders/my_spider.py
```

### ❌ Comparison spider shows same results
**Problem**: Both methods working (rare but possible)

**Solutions**:
- Try a more JavaScript-heavy site
- Use a site with anti-bot protection
- Show the response.meta difference

---

## 🆘 Emergency Fixes

### If Demo Completely Breaks:
1. Have backup virtual environment ready
2. Use pre-recorded terminal sessions
3. Show expected output from JSON files
4. Focus on code explanation instead

### If Internet Fails:
1. Use local HTML files
2. Show cached results
3. Focus on code walkthrough
4. Emphasize concepts over live demo

### If Time Runs Short:
1. Skip comparison spider
2. Focus on before/after demo
3. Send materials for later practice
4. Extend Q&A time

---

## 📞 Getting Help

### During Workshop:
- Check this troubleshooting guide first
- Ask presenter or assistants
- Help fellow attendees
- Take notes for follow-up

### After Workshop:
- **Documentation**: https://scrapy-zyte-api.readthedocs.io/
- **Community**: https://discord.gg/scrapy
- **Issues**: GitHub issues on scrapy-zyte-api
- **Support**: support@zyte.com

---

## 🔍 Diagnostic Commands

Use these to gather information for troubleshooting:

```bash
# System info
python --version
pip --version
which python
echo $VIRTUAL_ENV

# Package versions
pip list | grep -E "(scrapy|zyte)"

# Environment variables
echo $ZYTE_API_KEY | cut -c1-10  # Show first 10 chars only

# Test basic connectivity
python -c "import scrapy; print('Scrapy OK')"
python -c "import scrapy_zyte_api; print('Zyte API addon OK')"

# Spider diagnostics
scrapy list
scrapy check traditional
```

---

**💡 Pro tip**: Most issues are environment-related. When in doubt, recreate the virtual environment and reinstall packages. 