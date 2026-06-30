# Changelog

## [2.0.3](https://github.com/ScrapingBee/scrapingbee-python/compare/v2.0.2...v2.0.3) (2026-06-30)

### Improvement

- Document Auto-Mode (`mode=auto`) support: ScrapingBee picks the cheapest scraping configuration that succeeds and charges only for the winning one. Read the credits charged from the `Spb-auto-cost` response header, and optionally cap the cost with `max_cost`. No client changes are required — these are pass-through query parameters.

## [2.0.0](https://github.com/ScrapingBee/scrapingbee-python/compare/v1.2.0...v2.0.0) (2023-10-03)

### Improvement

- Properly url encode all params (Thanks to @tuky with [PR15](https://github.com/ScrapingBee/scrapingbee-python/pull/15)).

### Breaking change

- No need to url encode params anymore.
