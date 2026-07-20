# ScrapingBee Python SDK

[![lint-test-publish](https://github.com/scrapingbee/scrapingbee-python/workflows/lint-test-publish/badge.svg)](https://github.com/scrapingbee/scrapingbee-python/actions)
[![version](https://img.shields.io/pypi/v/scrapingbee.svg)](https://pypi.org/project/scrapingbee/)
[![python](https://img.shields.io/pypi/pyversions/scrapingbee.svg)](https://pypi.org/project/scrapingbee/)

[ScrapingBee](https://www.scrapingbee.com/) is a web scraping API that handles headless browsers and rotates proxies for you. The Python SDK makes it easier to interact with ScrapingBee's API.

## Installation

You can install ScrapingBee Python SDK with pip.

```bash
pip install scrapingbee
```

## Usage

The ScrapingBee Python SDK is a wrapper around the [requests](https://docs.python-requests.org/en/master/) library.

Signup to ScrapingBee to [get your API key](https://app.scrapingbee.com/account/register) and some free credits to get started.

## Table of Contents

- [HTML API](#html-api)
- [Google Search API](#google-search-api)
- [Fast Search API](#fast-search-api)
- [Amazon API](#amazon-api)
- [Walmart API](#walmart-api)
- [YouTube API](#youtube-api)
- [ChatGPT API](#chatgpt-api)
- [Gemini API](#gemini-api)
- [Usage API](#usage-api)

---

## HTML API

The HTML API allows you to scrape any webpage and get the HTML content.

### Basic Request

```python
from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='YOUR-API-KEY')

response = client.html_api(
    'https://www.scrapingbee.com',
    params={
        'render_js': False,
    }
)

print(response.content)
```

### Making a POST request

```python
response = client.html_api(
    'https://httpbin.org/post',
    method='POST',
    data={
        'key': 'value'
    }
)
```

---

## Google Search API

Scrape Google search results in real-time.

```python
response = client.google_search(
    search='web scraping tools',
    params={
        'language': 'en',
        'country_code': 'us',
        'nb_results': 10
    }
)

print(response.json())
```

---

## Fast Search API

Lightweight Google search results in under a second.

```python
response = client.fast_search(
    search='pizza in new york',
    params={
        'country_code': 'us',
        'language': 'en',
        'page': 1
    }
)

print(response.json())
```

---

## Amazon API

Scrape Amazon search results, product details, and pricing.

### Amazon Search

```python
response = client.amazon_search(
    query='laptop',
    params={
        'domain': 'com',
        'language': 'en',
        'pages': 1
    }
)

print(response.json())
```

### Amazon Product

```python
response = client.amazon_product(
    query='B0D2Q9397Y',  # ASIN
    params={
        'domain': 'com'
    }
)

print(response.json())
```

### Amazon Pricing

```python
response = client.amazon_pricing(
    asin='B0DPDRNSXV',
    params={
        'domain': 'com',
        'light_request': True
    }
)

print(response.json())
```

---

## Walmart API

Scrape Walmart search results and product details.

### Walmart Search

```python
response = client.walmart_search(
    query='laptop',
    params={
        'sort_by': 'best_match',
        'device': 'desktop'
    }
)

print(response.json())
```

### Walmart Product

```python
response = client.walmart_product(
    product_id='123456789',
    params={
        'device': 'desktop'
    }
)

print(response.json())
```

---

## YouTube API

Scrape YouTube search results, video metadata, and subtitles.

### YouTube Search

```python
response = client.youtube_search(
    search='web scraping tutorial',
    params={
        'sort_by': 'relevance',
        'type': 'video'
    }
)

print(response.json())
```

### YouTube Metadata

```python
response = client.youtube_metadata(video_id='dQw4w9WgXcQ')
print(response.json())
```

### YouTube Subtitles

```python
response = client.youtube_subtitles(
    video_id='dQw4w9WgXcQ',
    params={
        'language': 'en',
        'subtitle_origin': 'uploader_provided'
    }
)
print(response.json())
```

---

## ChatGPT API

Use ChatGPT with optional web search.

```python
response = client.chatgpt(
    prompt='What is web scraping?',
    params={
        'search': True,
        'country_code': 'us'
    }
)

print(response.json())
```

---

## Gemini API

Send prompts to Gemini and receive AI-generated responses.

```python
response = client.gemini(
    prompt='Best programming languages for data science',
    params={
        'country_code': 'us',
        'add_html': False
    }
)

print(response.json())
```

---

## Usage API

Check your API credit usage.

```python
response = client.usage()
print(response.json())
# {
#     "max_api_credit": 8000000,
#     "used_api_credit": 1000023,
#     "max_concurrency": 200,
#     "current_concurrency": 1
# }
```

---

## Legacy Methods (Deprecated)

The `get()` and `post()` methods are deprecated and will be removed in a future version. Please use `html_api()` instead.

```python
# Deprecated
client.get(url, params={...})

# Use instead
client.html_api(url, method='GET', params={...})
```

## Screenshot

Here is a little example on how to retrieve and store a screenshot from the ScrapingBee blog.

```python
from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='YOUR-API-KEY')

response = client.html_api(
    'https://www.scrapingbee.com/',
    params={
        'screenshot': True,
        'screenshot_full_page': True,
        'window_width': 375,
    }
)

with open('screenshot.png', 'wb') as f:
    f.write(response.content)
```

## Retries

The client includes a retry mechanism for 5XX responses.

```python
client.html_api(url, params={...}, retries=5)
```

## Using ScrapingBee with Scrapy

Scrapy is the most popular Python web scraping framework. You can easily [integrate ScrapingBee's API with the Scrapy middleware](https://github.com/ScrapingBee/scrapy-scrapingbee).