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
        # Interact with the webpage you want to scrape 
        'json_scenario': {
            "instructions": [
                {"wait_for": "#slow_button"},
                {"click": "#slow_button"},
                {"scroll_x": 1000},
                {"wait": 1000},
                {"scroll_x": 1000},
                {"wait": 1000},            
            ]
        },
        # Use premium proxies to bypass difficult to scrape websites (10-25 credits/request)
        'premium_proxy': False,
        # Execute JavaScript code with a Headless Browser (5 credits/request)
        'render_js': True,
        # Return the original HTML before the JavaScript rendering	
        'return_page_source': False,
        # Return page screenshot as a png image
        'screenshot': False,
        # Take a full page screenshot without the window limitation
        'screenshot_full_page': False,
        # Transparently return the same HTTP code of the page requested.
        'transparent_status_code': False,
        # Wait, in miliseconds, before returning the response
        'wait': 0,
        # Wait for CSS selector before returning the response, ex ".title"
        'wait_for': '',
        # Set the browser window width in pixel
        'window_width': 1920,
        # Set the browser window height in pixel
        'window_height': 1080
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

## Screenshot

Here a little exemple on how to retrieve and store a screenshot from the ScrapingBee blog in its mobile resolution.

```python
>>> from scrapingbee import ScrapingBeeClient

>>> client = ScrapingBeeClient(api_key='REPLACE-WITH-YOUR-API-KEY')

>>> response = client.get(
    'https://www.scrapingbee.com/blog/', 
    params={
        # Take a screenshot
        'screenshot': True,
        # Specify that we need the full height
        'screenshot_full_page': True,
        # Specify a mobile width in pixel
        'window_width': 375
    }
)

>>> if response.ok:
        with open("./scrapingbee_mobile.png", "wb") as f:
            f.write(response.content)
```

## Using ScrapingBee with Scrapy

Scrapy is the most popular Python web scraping framework. You can easily [integrate ScrapingBee's API with the Scrapy middleware](https://github.com/ScrapingBee/scrapy-scrapingbee).
