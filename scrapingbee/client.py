from typing import Optional

from requests import Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from .utils import get_scrapingbee_url, process_headers


class ScrapingBeeClient:
    api_url = "https://app.scrapingbee.com/api/v1/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def request(
        self,
        method: str,
        url: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        cookies: Optional[dict] = None,
        retries: Optional[int] = None,
        **kwargs
    ) -> Response:
        if not params:
            params = {}

        # Process headers and set forward_headers
        if headers:
            params["forward_headers"] = True
        headers = process_headers(headers)

        # Add cookies to params
        if cookies:
            # ScrapingBee reads cookies from url parameters
            params["cookies"] = cookies

        # Get ScrapingBee API URL
        spb_url = get_scrapingbee_url(self.api_url, self.api_key, url, params)

        session = Session()
        if retries:
            # Retries if it is a network error or a 5xx error on an idempotent request (GET)
            retries = Retry(total=retries, raise_on_status=False, status_forcelist=frozenset(range(500, 600)))
            session.mount('https://', HTTPAdapter(max_retries=retries))
            session.mount('http://', HTTPAdapter(max_retries=retries))

        if not data and json is not None:
            return session.request(method, spb_url, json=json, headers=headers, **kwargs)
        return session.request(method, spb_url, data=data, headers=headers, **kwargs)

    def get(
        self,
        url: str,
        params: dict = None,
        headers: dict = None,
        cookies: dict = None,
        retries: Optional[int] = None,
        **kwargs
    ) -> Response:
        return self.request("GET", url, params=params, headers=headers, cookies=cookies, retries=retries, **kwargs)

    def post(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        json: dict = None,
        headers: dict = None,
        cookies: dict = None,
        **kwargs
    ) -> Response:
        return self.request(
            "POST", url, params=params, data=data, json=json, headers=headers, cookies=cookies, **kwargs
        )
