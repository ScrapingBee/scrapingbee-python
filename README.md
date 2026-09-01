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

### Authentication

Pass your API key to the client constructor. Since version 2.2.0 the SDK authenticates via the `Authorization: Bearer <api_key>` request header (previously the `api_key` query parameter), keeping your key out of URLs and server logs.

```python
from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='YOUR-API-KEY')
```

### Common parameters

Every endpoint (except Usage, which takes no parameters) additionally accepts an optional `tag` parameter (string, max 36 characters, letters/digits/`-`/`_`/spaces) to label requests for your own analytics.

## Table of Contents

- [HTML API](#html-api)
  - [Auto-Mode](#auto-mode)
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

### Auto-Mode

With Auto-Mode, ScrapingBee picks the cheapest scraping configuration that successfully scrapes the page for you: it tries the cheaper options first and stops at the first one that works. You are charged only for the winning configuration (and 0 credits if every configuration fails).

```python
>>> from scrapingbee import ScrapingBeeClient

>>> client = ScrapingBeeClient(api_key='REPLACE-WITH-YOUR-API-KEY')

# Auto-Mode: ScrapingBee picks the cheapest config that works; you're charged only for the winning one.
>>> response = client.html_api(
    'https://example.com',
    method='GET',
    params={
        'mode': 'auto',
        # Optional: cap the credits a single request may cost (omit for uncapped).
        'max_cost': 25
    }
)

# Spb-auto-cost reports the credits actually charged (0 if every config failed).
>>> response.headers['Spb-auto-cost']
'1'
```

Notes:

- Auto-Mode is only available on `GET` requests.
- `max_cost` is optional and must be `>= 1`; omit it to leave the cost uncapped. Sending `max_cost` without `mode=auto` returns a `400`.
- `mode=auto` cannot be combined with `render_js`, `premium_proxy`, `stealth_proxy` (ScrapingBee chooses these for you) or `transparent_status_code`. Sending them together returns a `400`.

### HTML API Parameters

Parameters accepted on both `GET` and `POST` requests:

| Parameter | Type | Description |
|---|---|---|
| `url` | string | **Required.** The URL to scrape (set automatically from the first argument). |
| `ai_query` | string | AI query describing what to extract (max 300 chars). |
| `ai_selector` | string | CSS selector to narrow AI extraction (max 100 chars). |
| `ai_extract_rules` | dict | AI extraction rules (the SDK JSON-stringifies dicts for you). |
| `cookies` | dict | Cookies to forward (pass via the `cookies=` argument; the SDK formats them). |
| `country_code` | string | Country to proxy the request from. |
| `extract_rules` | dict | CSS/XPath extraction rules (the SDK JSON-stringifies dicts for you). |
| `forward_headers` | bool | Forward your headers to the target (set automatically when you pass `headers=`). |
| `forward_headers_pure` | bool | Forward headers without ScrapingBee's defaults. |
| `json_response` | bool | Wrap the response in JSON with extra metadata. |
| `own_proxy` | string | Use your own proxy (`protocol://user:password@host:port`). |
| `premium_proxy` | bool | Use premium (residential) proxies. |
| `scraping_config` | string | Name of a saved scraping configuration (max 32 chars). |
| `session_id` | int | Reuse the same proxy across requests. |
| `timeout` | int | Request timeout in ms (1000–141000). |
| `transparent_status_code` | bool | Return the target's HTTP status code as-is. |

Parameters accepted on `GET` requests only:

| Parameter | Type | Description |
|---|---|---|
| `block_ads` | bool | Block ads when rendering JavaScript. |
| `block_resources` | bool | Block images and CSS when rendering JavaScript. |
| `custom_google` | bool | **Required (`True`) when scraping Google domains** — a `400` is returned if a `google.*` URL is sent without it, or if it is set on a non-Google URL. |
| `device` | string | `desktop` (default) or `mobile`. |
| `js_scenario` | dict | Browser instructions to execute (the SDK JSON-stringifies dicts for you). |
| `max_cost` | int | Auto-Mode cost cap (`>= 1`, only with `mode=auto`). |
| `mode` | string | `auto` — see [Auto-Mode](#auto-mode). |
| `render_js` | bool | Render the page in a headless browser (default `True`). |
| `return_page_source` | bool | Return the HTML before JavaScript execution. |
| `return_page_markdown` | bool | Return the page converted to Markdown. |
| `return_page_text` | bool | Return the page's text content only. |
| `screenshot` | bool | Return a screenshot of the visible viewport. |
| `screenshot_full_page` | bool | Return a full-page screenshot. |
| `screenshot_selector` | string | Screenshot only the element matching this CSS selector. |
| `stealth_proxy` | bool | Use stealth proxies for hard-to-scrape sites. |
| `wait` | int | Fixed wait in ms before returning (0–35000). |
| `wait_browser` | string | Wait until: `load`, `domcontentloaded`, `networkidle0` or `networkidle2`. |
| `wait_for` | string | Wait for a CSS selector to appear. |
| `window_height` | int | Viewport height in px. |
| `window_width` | int | Viewport width in px. |

Deprecated parameters (still accepted, but avoid in new code): `no_html`, `js_scroll`, `js_scroll_count`, `js_scroll_wait`, `js_snippet`.

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

### Google Search Parameters

| Parameter | Type | Description |
|---|---|---|
| `search` | string | **Required.** The search query (set automatically from the first argument). |
| `add_html` | bool | Include the raw HTML in the response. |
| `country_code` | string | Country to search from (default `us`). |
| `date_range` | string | `past_hour`, `past_day`, `past_week`, `past_month` or `past_year`. |
| `device` | string | `desktop` or `mobile` (`mobile` is not available with `search_type=news`). |
| `extra_params` | string | Extra Google query-string params; allowed keys: `filter`, `fpstate`, `locale`, `nfpr`, `safe`, `safe_search`, `tbm`, `tbs`, `udm`. |
| `language` | string | **Deprecated** — accepted but ignored. |
| `latitude` / `longitude` | float | Geo-target results; must be provided together. |
| `light_request` | bool | Lighter, cheaper scrape (default `True`). |
| `min_price` / `max_price` | float | Price filters; only with `search_type=shopping`. |
| `nb_results` | int | Number of results to request (default 10; capped at 20 for `search_type=maps`). |
| `nfpr` | bool | Disable auto-corrected spelling results. |
| `page` | int | Result page to fetch (default 1). |
| `pages` | int | Number of pages to fetch (1–10, default 1). |
| `radius` | int | Search radius; requires `latitude`/`longitude`. |
| `search_type` | string | `classic` (default), `news`, `maps`, `images`, `lens`, `shopping`, `ai_mode` or `ads`. For `lens`, `search` must be an image URL; for `ai_mode`, `search` is capped at 400 chars. |
| `sort_by` | string | `relevance`, `reviews`, `price_asc` or `price_desc`; only with `search_type=shopping`. |

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

### Fast Search Parameters

| Parameter | Type | Description |
|---|---|---|
| `search` | string | **Required.** The search query (set automatically from the first argument). |
| `country_code` | string | Country to search from (default `us`). |
| `language` | string | **Deprecated** — accepted but ignored. |
| `page` | int | Result page to fetch (`>= 1`). |

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

### Amazon Parameters

Shared by all three Amazon endpoints:

| Parameter | Type | Description |
|---|---|---|
| `add_html` | bool | Include the raw HTML in the response (default `False`). |
| `country` | string | Country to geo-target. Only takes effect when `domain` is not set — on search/product `domain` defaults to `com`, so `country` there is either rejected with a `400` (when it matches the domain's country) or ignored. Effective on pricing only (where `us` is the default and ignored). |
| `currency` | string | Currency for prices. |
| `domain` | string | Amazon domain, e.g. `com`, `co.uk` (default `com` on search/product, unset on pricing). |
| `language` | string | Result language. |
| `light_request` | bool | Lighter, cheaper scrape (default `True`). |
| `zip_code` | string | Zip code to geo-target offers. |

Endpoint-specific:

| Parameter | Type | Endpoints | Description |
|---|---|---|---|
| `query` | string | search, product | **Required.** Search terms (search) or a 10-char ASIN (product). |
| `asin` | string | pricing | **Required.** 10-char ASIN (`[A-Z0-9]{10}`). |
| `autoselect_variant` | bool | search, product | Auto-select the default product variant. |
| `category_id` | string | search | Restrict results to a category. |
| `device` | string | all | `desktop` (all); product also allows `mobile` and `tablet`. |
| `merchant_id` | string | search | Restrict results to a merchant. |
| `pages` | int | search | Number of pages to fetch (default 1). |
| `screenshot` | bool | search, product | Return a screenshot. |
| `sort_by` | string | search | `most_recent`, `price_low_to_high`, `price_high_to_low`, `featured`, `average_review` or `bestsellers` (default `bestsellers`). |
| `start_page` | int | search | First page to fetch (default 1). |

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

### Walmart Parameters

Shared by both Walmart endpoints:

| Parameter | Type | Description |
|---|---|---|
| `add_html` | bool | Include the raw HTML in the response. |
| `delivery_zip` | string | Zip code to geo-target offers. |
| `device` | string | `desktop`, `mobile` or `tablet`. |
| `domain` | string | Walmart domain. |
| `light_request` | bool | Lighter, cheaper scrape (default `True`). |
| `screenshot` | bool | Return a screenshot. |
| `store_id` | string | Restrict results to a specific store. |

Endpoint-specific:

| Parameter | Type | Endpoints | Description |
|---|---|---|---|
| `query` | string | search | **Required.** Search terms. |
| `product_id` | string | product | **Required.** Walmart product ID. |
| `fulfillment_speed` | string | search | `today`, `tomorrow`, `2_days` or `anytime`. |
| `fulfillment_type` | string | search | `in_store`. |
| `min_price` / `max_price` | int | search | Price filters (whole numbers only; `400` if `min_price > max_price`). |
| `sort_by` | string | search | `price_low`, `price_high`, `best_seller` or `best_match` (default `best_match`). |
| `start_page` | int | search | First page to fetch (`>= 1`, default 1). |

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

### YouTube Parameters

YouTube Search:

| Parameter | Type | Description |
|---|---|---|
| `search` | string | **Required.** The search query (set automatically from the first argument). |
| `duration` | string | `<4`, `4-20` or `>20` (minutes). |
| `sort_by` | string | `rating`, `relevance`, `view_count` or `upload_date` (default `relevance`). |
| `type` | string | `video`, `channel`, `playlist` or `movie`. |
| `upload_date` | string | `today`, `last_hour`, `this_week`, `this_month` or `this_year`. |
| `360`, `3d`, `4k`, `creative_commons`, `hd`, `hdr`, `live`, `location`, `purchased`, `subtitles`, `vr180` | bool | Result filters (use the exact names shown, e.g. `params={'4k': True}`; `location` filters for videos that have location data). |

YouTube Metadata:

| Parameter | Type | Description |
|---|---|---|
| `video_id` | string | **Required.** The video ID (set automatically from the first argument). |

YouTube Subtitles:

| Parameter | Type | Description |
|---|---|---|
| `video_id` | string | **Required.** The video ID (set automatically from the first argument). |
| `language` | string | Subtitle language. |
| `subtitle_origin` | string | `auto_generated` or `uploader_provided`. |

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

### ChatGPT Parameters

| Parameter | Type | Description |
|---|---|---|
| `prompt` | string | **Required.** The prompt (max 3999 chars; set automatically from the first argument). |
| `add_html` | bool | Include the raw HTML in the response. |
| `country_code` | string | Two-letter country code to route the request from. |
| `search` | bool | Enable web search (default `True`). |

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

### Gemini Parameters

| Parameter | Type | Description |
|---|---|---|
| `prompt` | string | **Required.** The prompt (max 7999 chars; set automatically from the first argument). |
| `add_html` | bool | Include the raw HTML in the response. |
| `country_code` | string | Two-letter country code to route the request from. |

Unlike ChatGPT, the Gemini API does not accept a `search` parameter — sending one returns a `400`.

---

## Usage API

Check your API credit usage. Takes no parameters and is rate-limited to 6 requests per minute.

```python
response = client.usage()
print(response.json())
# {
#     "max_api_credit": 8000000,
#     "used_api_credit": 1000023,
#     "max_concurrency": 200,
#     "current_concurrency": 1,
#     "renewal_subscription_date": "2026-09-01T04:57:13.580067"
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