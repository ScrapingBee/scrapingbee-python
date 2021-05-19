from requests import request

from .utils import get_scrapingbee_url, process_headers


class ScrapingBeeClient:
    api_url = 'https://app.scrapingbee.com/api/v1/'

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, method, url, params=None, data=None, headers=None, cookies=None, **kwargs):
        if not params:
            params = {}

        # Process headers and set forward_headers
        if headers:
            headers = process_headers(headers)
            params['forward_headers'] = True

        # Add cookies to params
        if cookies:
            # ScrapingBee reads cookies from url parameters
            params['cookies'] = cookies

        # Get ScrapingBee API URL
        spb_url = get_scrapingbee_url(
            self.api_url, self.api_key, url, params)

        return request(method, spb_url, data=data, headers=headers, **kwargs)

    def get(self, url, params=None, headers=None, cookies=None, **kwargs):
        return self.request('GET', url, params=params, headers=headers, cookies=cookies, **kwargs)

    def post(self, url, params=None, data=None, headers=None, cookies=None, **kwargs):
        return self.request(
            'POST',
            url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookies,
            **kwargs
        )
