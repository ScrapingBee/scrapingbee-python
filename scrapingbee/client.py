from requests import Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from .utils import process_headers, process_params


class ScrapingBeeClient:
    # API Endpoints
    HTML_API_URL = "https://app.scrapingbee.com/api/v1/"
    GOOGLE_API_URL = "https://app.scrapingbee.com/api/v1/store/google"
    AMAZON_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/amazon/search"
    AMAZON_PRODUCT_API_URL = "https://app.scrapingbee.com/api/v1/amazon/product"
    WALMART_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/walmart/search"
    WALMART_PRODUCT_API_URL = "https://app.scrapingbee.com/api/v1/walmart/product"
    YOUTUBE_SEARCH_API_URL = "https://app.scrapingbee.com/api/v1/youtube/search"
    YOUTUBE_METADATA_API_URL = "https://app.scrapingbee.com/api/v1/youtube/metadata"
    YOUTUBE_TRANSCRIPT_API_URL = "https://app.scrapingbee.com/api/v1/youtube/transcript"
    YOUTUBE_TRAINABILITY_API_URL = "https://app.scrapingbee.com/api/v1/youtube/trainability"
    CHATGPT_API_URL = "https://app.scrapingbee.com/api/v1/chatgpt"
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
        headers: dict = None,
        data: dict = None,
        json: dict = None,
        retries: int = None,
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

    def get(
        self,
        url: str,
        params: dict = None,
        headers: dict = None,
        cookies: dict = None,
        retries: int = None,
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

    def post(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        json: dict = None,
        headers: dict = None,
        cookies: dict = None,
        retries: int = None,
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
        params: dict = None,
        data: dict = None,
        json: dict = None,
        headers: dict = None,
        cookies: dict = None,
        retries: int = None,
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
        params: dict = None,
        retries: int = None,
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
    # Amazon API
    # ============================================

    def amazon_search(
        self,
        query: str,
        params: dict = None,
        retries: int = None,
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
        params: dict = None,
        retries: int = None,
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

    # ============================================
    # Walmart API
    # ============================================

    def walmart_search(
        self,
        query: str,
        params: dict = None,
        retries: int = None,
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
        params: dict = None,
        retries: int = None,
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
        params: dict = None,
        retries: int = None,
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
        params: dict = None,
        retries: int = None,
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

    def youtube_transcript(
        self,
        video_id: str,
        params: dict = None,
        retries: int = None,
        **kwargs
    ) -> Response:
        """YouTube Transcript API - Get YouTube video transcript."""
        if params is None:
            params = {}
        params["video_id"] = video_id

        return self.request(
            method="GET",
            url=self.YOUTUBE_TRANSCRIPT_API_URL,
            params=params,
            retries=retries,
            **kwargs
        )

    def youtube_trainability(
        self,
        video_id: str,
        params: dict = None,
        retries: int = None,
        **kwargs
    ) -> Response:
        """YouTube Trainability API - Check video trainability."""
        if params is None:
            params = {}
        params["video_id"] = video_id

        return self.request(
            method="GET",
            url=self.YOUTUBE_TRAINABILITY_API_URL,
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
        params: dict = None,
        retries: int = None,
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
    # Usage API
    # ============================================

    def usage(
        self,
        retries: int = None,
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
