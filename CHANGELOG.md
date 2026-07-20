# Changelog

## [2.1.0](https://github.com/ScrapingBee/scrapingbee-python/compare/v2.0.2...v2.1.0) (2026-07-20)

### Features

- Added `html_api()` method for HTML API with unified GET/POST support
- Added `google_search()` method for Google Search API
- Added `fast_search()` method for Fast Search API
- Added `amazon_search()` method for Amazon Search API
- Added `amazon_product()` method for Amazon Product API
- Added `amazon_pricing()` method for Amazon Pricing API
- Added `walmart_search()` method for Walmart Search API
- Added `walmart_product()` method for Walmart Product API
- Added `youtube_search()` method for YouTube Search API
- Added `youtube_metadata()` method for YouTube Metadata API
- Added `youtube_subtitles()` method for YouTube Subtitles API
- Added `chatgpt()` method for ChatGPT API
- Added `gemini()` method for Gemini API
- Added `usage()` method for Usage API
- Refactored internal `request()` method to be API-agnostic

### Deprecated

- `get()` and `post()` are deprecated in favor of `html_api()` and will be removed in version 3.0.0.

## [2.0.2](https://github.com/ScrapingBee/scrapingbee-python/compare/v2.0.1...v2.0.2) (2025-10-02)

### Features

- Added support for `ai_extract_rules` parameter in `SpbParams`.
- Added Python 3.11 support.

### Changes

- Dropped Python 3.7 support.

## [2.0.1](https://github.com/ScrapingBee/scrapingbee-python/compare/v2.0.0...v2.0.1) (2023-10-17)

### Bugfix

- Fix typos in `README.md` (`block_ressources` -> `block_resources`, `json_scenario` -> `js_scenario`).

## [2.0.0](https://github.com/ScrapingBee/scrapingbee-python/compare/v1.2.0...v2.0.0) (2023-10-03)

### Improvement

- Properly url encode all params (Thanks to @tuky with [PR15](https://github.com/ScrapingBee/scrapingbee-python/pull/15)).

### Breaking change

- No need to url encode params anymore.
