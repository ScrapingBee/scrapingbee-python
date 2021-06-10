from requests import request, Response

from .default_headers import default_headers
from .utils import get_scrapingbee_url, process_headers


class ScrapingBeeClient:
    api_url = 'https://app.scrapingbee.com/api/v1/'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def request(self, method: str, url: str, params: dict = None, data: dict = None,
                headers: dict = None, cookies: dict = None, **kwargs
                ) -> Response:
        if not params:
            params = {}

        # Process headers and set forward_headers
        if headers:
            headers = process_headers(headers)
            params['forward_headers'] = True
        else:
            headers = {}
        headers.update(default_headers)

        # Add cookies to params
        if cookies:
            # ScrapingBee reads cookies from url parameters
            params['cookies'] = cookies

        # Get ScrapingBee API URL
        spb_url = get_scrapingbee_url(
            self.api_url, self.api_key, url, params)

        return request(method, spb_url, data=data, headers=headers, **kwargs)

    def get(self, url: str, params: dict = None, headers: dict = None, cookies: dict = None,
            **kwargs
            ) -> Response:
        return self.request('GET', url, params=params, headers=headers, cookies=cookies, **kwargs)

    def post(self, url: str, params: dict = None, data: dict = None, headers: dict = None,
             cookies: dict = None, **kwargs
             ) -> Response:
        return self.request('POST', url, params=params, data=data, headers=headers,
                            cookies=cookies, **kwargs)
