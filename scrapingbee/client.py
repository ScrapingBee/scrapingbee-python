from requests import Response, Session
from requests.adapters import HTTPAdapter
from typing_extensions import deprecated
from urllib3.util import Retry

from .utils import process_headers, process_params


class ScrapingBeeClient:
    # API Endpoints
    HTML_API_URL = "https://app.scrapingbee.com/api/v1/"
    GOOGLE_API_URL = "https://app.scrapingbee.com/api/v1/store/google"
    FAST_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/fast_search"
    AMAZON_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/amazon/search"
    AMAZON_PRODUCT_API_URL = "https://app.scrapingbee.com/api/v1/amazon/product"
    AMAZON_PRICING_API_URL = "https://app.scrapingbee.com/api/v1/amazon/pricing"
    WALMART_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/walmart/search"
    WALMART_PRODUCT_API_URL = "https://app.scrapingbee.com/api/v1/walmart/product"
    YOUTUBE_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/youtube/search"
    YOUTUBE_METADATA_API_URL = "https://app.scrapingbee.com/api/v1/youtube/metadata"
    YOUTUBE_SUBTITLES_API_URL = "https://app.scrapingbee.com/api/v1/youtube/subtitles"
    CHATGPT_API_URL = "https://app.scrapingbee.com/api/v1/chatgpt"
    GEMINI_API_URL = "https://app.scrapingbee.com/api/v1/gemini"
    USAGE_API_URL = "https://app.scrapingbee.com/api/v1/usage"

    def __init__(self, api_key: str):
        self.api_key = api_key

    # ============================================
    # Core Request Method
    # ============================================

    def request(
        self,
        method: str,
        url: str,
        params: dict,
        headers: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Core request method - adds api_key and makes the HTTP call."""
        params["api_key"] = self.api_key

        session = Session()
        if retries:
            retry_strategy = Retry(
                total=retries,
                raise_on_status=False,
                status_forcelist=frozenset(range(500, 600))
            )
            session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
            session.mount("http://", HTTPAdapter(max_retries=retry_strategy))

        if json is not None:
            return session.request(method, url, params=params, json=json, headers=headers, **kwargs)
        return session.request(method, url, params=params, data=data, headers=headers, **kwargs)

    # ============================================
    # HTML API (Legacy - WILL BE REMOVED)
    # ============================================

    @deprecated("Please use html_api() instead. This method will be removed in version 3.0.0.")
    def get(
        self,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
        cookies: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """HTML API - GET request. DEPRECATED: Use html_api() instead."""
        if params is None:
            params = {}

        params["url"] = url
        if cookies:
            params["cookies"] = cookies

        processed_headers = process_headers(headers)
        if headers:
            params["forward_headers"] = True

        return self.request(
            method="GET",
            url=self.HTML_API_URL,
            params=process_params(params),
            headers=processed_headers,
            retries=retries,
            **kwargs
        )

    @deprecated("Please use html_api() instead. This method will be removed in version 3.0.0.")
    def post(
        self,
        url: str,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
        cookies: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """HTML API - POST request. DEPRECATED: Use html_api() instead."""
        if params is None:
            params = {}

        params["url"] = url
        if cookies:
            params["cookies"] = cookies

        processed_headers = process_headers(headers)
        if headers:
            params["forward_headers"] = True

        return self.request(
            method="POST",
            url=self.HTML_API_URL,
            params=process_params(params),
            headers=processed_headers,
            data=data,
            json=json,
            retries=retries,
            **kwargs
        )

    # ============================================
    # HTML API (New)
    # ============================================

    def html_api(
        self,
        url: str,
        method: str = "GET",
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
        cookies: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """HTML API - Scrape any webpage."""
        if params is None:
            params = {}

        params["url"] = url
        if cookies:
            params["cookies"] = cookies

        processed_headers = process_headers(headers)
        if headers:
            params["forward_headers"] = True

        return self.request(
            method=method,
            url=self.HTML_API_URL,
            params=process_params(params),
            headers=processed_headers,
            data=data,
            json=json,
            retries=retries,
            **kwargs
        )

    # ============================================
    # Google Search API
    # ============================================

    def google_search(
        self,
        search: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Google Search API - Scrape Google search results."""
        if params is None:
            params = {}
        params["search"] = search

        return self.request(
            method="GET",
            url=self.GOOGLE_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # Fast Search API
    # ============================================

    def fast_search(
        self,
        search: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Fast Search API - Lightweight Google search results."""
        if params is None:
            params = {}
        params["search"] = search

        return self.request(
            method="GET",
            url=self.FAST_SEARCH_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # Amazon API
    # ============================================

    def amazon_search(
        self,
        query: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Amazon Search API - Scrape Amazon search results."""
        if params is None:
            params = {}
        params["query"] = query

        return self.request(
            method="GET",
            url=self.AMAZON_SEARCH_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    def amazon_product(
        self,
        query: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Amazon Product API - Scrape Amazon product details."""
        if params is None:
            params = {}
        params["query"] = query

        return self.request(
            method="GET",
            url=self.AMAZON_PRODUCT_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    def amazon_pricing(
        self,
        asin: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Amazon Pricing API - Scrape Amazon product pricing details."""
        if params is None:
            params = {}
        params["asin"] = asin

        return self.request(
            method="GET",
            url=self.AMAZON_PRICING_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # Walmart API
    # ============================================

    def walmart_search(
        self,
        query: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Walmart Search API - Scrape Walmart search results."""
        if params is None:
            params = {}
        params["query"] = query

        return self.request(
            method="GET",
            url=self.WALMART_SEARCH_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    def walmart_product(
        self,
        product_id: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Walmart Product API - Scrape Walmart product details."""
        if params is None:
            params = {}
        params["product_id"] = product_id

        return self.request(
            method="GET",
            url=self.WALMART_PRODUCT_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # YouTube API
    # ============================================

    def youtube_search(
        self,
        search: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """YouTube Search API - Scrape YouTube search results."""
        if params is None:
            params = {}
        params["search"] = search

        return self.request(
            method="GET",
            url=self.YOUTUBE_SEARCH_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    def youtube_metadata(
        self,
        video_id: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """YouTube Metadata API - Get YouTube video metadata."""
        if params is None:
            params = {}
        params["video_id"] = video_id

        return self.request(
            method="GET",
            url=self.YOUTUBE_METADATA_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    def youtube_subtitles(
        self,
        video_id: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """YouTube Subtitles API - Get YouTube video subtitles."""
        if params is None:
            params = {}
        params["video_id"] = video_id

        return self.request(
            method="GET",
            url=self.YOUTUBE_SUBTITLES_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # ChatGPT API
    # ============================================

    def chatgpt(
        self,
        prompt: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """ChatGPT API - Use ChatGPT with optional web search."""
        if params is None:
            params = {}
        params["prompt"] = prompt

        return self.request(
            method="GET",
            url=self.CHATGPT_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # Gemini API
    # ============================================

    def gemini(
        self,
        prompt: str,
        params: dict | None = None,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Gemini API - Send prompts to Gemini and receive AI-generated responses."""
        if params is None:
            params = {}
        params["prompt"] = prompt

        return self.request(
            method="GET",
            url=self.GEMINI_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    # ============================================
    # Usage API
    # ============================================

    def usage(
        self,
        retries: int | None = None,
        **kwargs
    ) -> Response:
        """Usage API - Check API credit usage and account limits."""
        return self.request(
            method="GET",
            url=self.USAGE_API_URL,
            params={},
            retries=retries,
            **kwargs
        )
