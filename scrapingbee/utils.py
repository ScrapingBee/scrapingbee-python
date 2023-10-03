import base64
import json
import urllib
from typing import Optional

from .__version__ import __version__

DEFAULT_HEADERS = {"User-Agent": f"ScrapingBee-Python/{__version__}"}


def process_js_snippet(js_snippet: str) -> str:
    return base64.b64encode(js_snippet.encode()).decode()


def process_headers(headers: Optional[dict], prefix: str = 'Spb-') -> dict:
    headers = headers or {}
    headers = {f'{prefix}{k}': v for k, v in headers.items()}
    return {**DEFAULT_HEADERS, **headers}


def process_cookies(cookies: dict) -> str:
    if isinstance(cookies, dict):
        return ';'.join(f'{k}={v}' for k, v in cookies.items())
    elif isinstance(cookies, list):
        # ScrapingBee only supports name=value cookies ATM
        raise NotImplementedError
    elif isinstance(cookies, str):
        return cookies


def process_json_stringify_param(param: dict, param_name: str) -> str:
    if isinstance(param, dict):
        return json.dumps(param)
    else:
        raise ValueError(f"{param_name} must be a dict or a stringified JSON")


def process_params(params: dict) -> dict:
    new_params = {}
    for k, v in params.items():
        if v in (None, '', [], {}):
            continue
        elif k == 'js_snippet':
            new_params[k] = process_js_snippet(v)
        elif k == 'cookies':
            new_params[k] = process_cookies(v)
        elif k == 'extract_rules':
            new_params[k] = process_json_stringify_param(v, 'extract_rules')
        elif k == 'js_scenario':
            new_params[k] = process_json_stringify_param(v, 'js_scenario')
        else:
            new_params[k] = v
    return new_params


def get_scrapingbee_url(api_url: str, api_key: str, url: str, params: dict) -> str:
    all_params = {
        'api_key': api_key,
        'url': url
    }
    if params:
        all_params.update(params)

    # Process params
    spb_params = process_params(all_params)

    # Format url query string
    qs = urllib.parse.urlencode(spb_params)

    return f'{api_url}?{qs}'
