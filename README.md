# ScrapingBee Python SDK

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

>>> response = client.get('https://www.scrapingbee.com', params={
    # Execute JavaScript code with a Headless Browser
    'render_js': True,
    # Scroll once
    'js_scroll': True,
    # Wait 5 seconds before returning the response
    'wait': 5000,
    # Use a premium proxy
    'premium_proxy': True,
    # Use a premium proxy in France
    'country_code': 'fr',
})

>>> response.text
'<!DOCTYPE html><html lang="en"><head>...'
```

ScrapingBee takes various parameters to render JavaScript, execute a custom JavaScript script, use a premium proxy from a specific geolocation and more. You can find all the supported parameters on [ScrapingBee's documentation](https://www.scrapingbee.com/documentation/).

You can send custom cookies and headers like you would normally do with the requests library.

## Using ScrapingBee with Scrapy

Scrapy is the most popular Python web scraping framework. You can easily [integrate ScrapingBee's API with the Scrapy middleware](https://github.com/ScrapingBee/scrapy-scrapingbee).