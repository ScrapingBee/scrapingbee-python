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

The ScrapingBee Python SDK is a wrapper around the [requests](https://docs.python-requests.org/en/master/) library. ScrapingBee supports GET and POST requests.

Signup to ScrapingBee to [get your API key](https://app.scrapingbee.com/account/register) and some free credits to get started.

### Making a GET request

```python
>>> from scrapingbee import ScrapingBeeClient

>>> client = ScrapingBeeClient(api_key='REPLACE-WITH-YOUR-API-KEY')

>>> response = client.get(
    'https://www.scrapingbee.com/blog/', 
    params={
        # Block ads on the page you want to scrape	
        'block_ads': False,
        # Block images and CSS on the page you want to scrape	
        'block_ressources': True,
        # Premium proxy geolocation
        'country_code': '',
        # Control the device the request will be sent from	
        'device': 'desktop',
        # Use some data extraction rules
        'extract_rules': {'title': 'h1'},
        # Wrap response in JSON
        'json_response': False,
        # JavaScript snippet to execute (clicking on a button, scrolling ...)
        'js_snippet': '',
        # Scrolling to the end of the page before returning your results
        'js_scroll': False,
        # The time to wait between each scroll	
        'js_scroll_wait': 1000,
        # The number of scrolls you want to make	
        'js_scroll_count': 1,
        # Use premium proxies to bypass difficult to scrape websites (10-25 credits/request)
        'premium_proxy': False,
        # Execute JavaScript code with a Headless Browser (5 credits/request)
        'render_js': True,
        # Return the original HTML before the JavaScript rendering	
        'return_page_source': False,
        # Transparently return the same HTTP code of the page requested.
        'transparent_status_code': False,
        # Wait, in miliseconds, before returning the response
        'wait': 0,
        # Wait for CSS selector before returning the response, ex ".title"
        'wait_for': ''
    },
    headers={
        # Forward custom headers to the target website
        "key": "value"
    },
    cookies={
        # Forward custom cookies to the target website
        "name": "value"
    }
)
>>> response.text
'<!DOCTYPE html><html lang="en"><head>...'
```

ScrapingBee takes various parameters to render JavaScript, execute a custom JavaScript script, use a premium proxy from a specific geolocation and more. 

You can find all the supported parameters on [ScrapingBee's documentation](https://www.scrapingbee.com/documentation/).

You can send custom cookies and headers like you would normally do with the requests library.

## Using ScrapingBee with Scrapy

Scrapy is the most popular Python web scraping framework. You can easily [integrate ScrapingBee's API with the Scrapy middleware](https://github.com/ScrapingBee/scrapy-scrapingbee).