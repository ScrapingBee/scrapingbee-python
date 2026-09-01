from unittest import mock

import pytest

from scrapingbee import ScrapingBeeClient
from scrapingbee.utils import DEFAULT_HEADERS

AUTH_HEADERS = {'Authorization': 'Bearer API_KEY'}

DEPRECATION_MESSAGE = (
    r"Please use html_api\(\) instead\. "
    r"This method will be removed in version 3\.0\.0\."
)


@pytest.fixture(scope='module')
def client():
    return ScrapingBeeClient(api_key='API_KEY')


# ============================================
# Legacy HTML API Tests (get)
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_get(mock_session, client):
    '''It should make a GET request with the url and API key'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_params(mock_session, client):
    '''It should add parameters to the request'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org', params={'render_js': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org', 'render_js': True},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_headers(mock_session, client):
    '''It should prefix header names with Spb- and set forward_headers'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org', 'forward_headers': True},
        data=None,
        headers={'Spb-Content-Type': 'text/html; charset=utf-8', **DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_cookies(mock_session, client):
    '''It should format the cookies and add them to the params'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org', cookies={
            'name_1': 'value_1',
            'name_2': 'value_2',
        })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org', 'cookies': 'name_1=value_1;name_2=value_2'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_extract_rules(mock_session, client):
    '''It should format the extract_rules and add them to the params'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org', params={
            'extract_rules': {
                "title": "h1",
                "subtitle": "#subtitle"
            }
        })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={
            'url': 'https://httpbin.org',
            'extract_rules': '{"title": "h1", "subtitle": "#subtitle"}'
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_js_scenario(mock_session, client):
    '''It should format the js_scenario and add them to the params'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org', params={
            'js_scenario': {
                'instructions': [
                    {"click": "#buttonId"}
                ]
            }
        })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={
            'url': 'https://httpbin.org',
            'js_scenario': '{"instructions": [{"click": "#buttonId"}]}'
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_ai_extract_rules(mock_session, client):
    '''It should format the ai_extract_rules and add them to the params'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.get('https://httpbin.org', params={
            'ai_extract_rules': {
                "product_name": "The name of the product",
                "price": "The price in USD"
            }
        })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={
            'url': 'https://httpbin.org',
            'ai_extract_rules': '{"product_name": "The name of the product", "price": "The price in USD"}'
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


# ============================================
# Legacy HTML API Tests (post)
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_post(mock_session, client):
    '''It should make a POST request with some data'''
    with pytest.warns(DeprecationWarning, match=DEPRECATION_MESSAGE):
        client.post('https://httpbin.org', data={'KEY_1': 'VALUE_1'})

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org'},
        data={'KEY_1': 'VALUE_1'},
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# New HTML API Tests (html_api)
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_html_api_get(mock_session, client):
    '''It should make a GET request with html_api'''
    client.html_api('https://httpbin.org')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_post(mock_session, client):
    '''It should make a POST request with html_api'''
    client.html_api('https://httpbin.org', method='POST')

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_params(mock_session, client):
    '''It should add parameters to html_api request'''
    client.html_api('https://httpbin.org', params={'render_js': True, 'premium_proxy': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org', 'render_js': True, 'premium_proxy': True},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_headers(mock_session, client):
    '''It should prefix header names with Spb- and set forward_headers'''
    client.html_api('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org', 'forward_headers': True},
        data=None,
        headers={'Spb-Content-Type': 'text/html; charset=utf-8', **DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_cookies(mock_session, client):
    '''It should format the cookies and add them to the params'''
    client.html_api('https://httpbin.org', cookies={
        'name_1': 'value_1',
        'name_2': 'value_2',
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org', 'cookies': 'name_1=value_1;name_2=value_2'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_headers_and_cookies(mock_session, client):
    '''It should handle headers and cookies in html_api'''
    client.html_api(
        'https://httpbin.org',
        method='POST',
        headers={'X-Custom': 'value'},
        cookies={'session': 'abc123'}
    )

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={
                'url': 'https://httpbin.org',
                'cookies': 'session=abc123',
                'forward_headers': True
            },
        data=None,
        headers={'Spb-X-Custom': 'value', **DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_extract_rules(mock_session, client):
    '''It should format the extract_rules and add them to the params'''
    client.html_api('https://httpbin.org', params={
        'extract_rules': {
            "title": "h1",
            "subtitle": "#subtitle"
        }
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={
            'url': 'https://httpbin.org',
            'extract_rules': '{"title": "h1", "subtitle": "#subtitle"}'
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_js_scenario(mock_session, client):
    '''It should format the js_scenario and add them to the params'''
    client.html_api('https://httpbin.org', params={
        'js_scenario': {
            'instructions': [
                {"click": "#buttonId"}
            ]
        }
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={
            'url': 'https://httpbin.org',
            'js_scenario': '{"instructions": [{"click": "#buttonId"}]}'
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_ai_extract_rules(mock_session, client):
    '''It should format the ai_extract_rules and add them to the params'''
    client.html_api('https://httpbin.org', params={
        'ai_extract_rules': {
            "product_name": "The name of the product",
            "price": "The price in USD"
        }
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={
            'url': 'https://httpbin.org',
            'ai_extract_rules': '{"product_name": "The name of the product", "price": "The price in USD"}'
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_post_with_data(mock_session, client):
    '''It should make a POST request with some data'''
    client.html_api('https://httpbin.org', method='POST', data={'KEY_1': 'VALUE_1'})

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={'url': 'https://httpbin.org'},
        data={'KEY_1': 'VALUE_1'},
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Google Search API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_google_search(mock_session, client):
    '''It should make a Google Search request'''
    client.google_search('test query')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/store/google',
        params={'search': 'test query'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_google_search_with_params(mock_session, client):
    '''It should add parameters to Google Search request'''
    client.google_search('test query', params={'language': 'en', 'country_code': 'us'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/store/google',
        params={'search': 'test query', 'language': 'en', 'country_code': 'us'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Fast Search API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_fast_search(mock_session, client):
    '''It should make a Fast Search request'''
    client.fast_search('test query')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/fast_search',
        params={'search': 'test query'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_fast_search_with_params(mock_session, client):
    '''It should add parameters to Fast Search request'''
    client.fast_search('test query', params={'page': 2, 'country_code': 'us', 'language': 'en'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/fast_search',
        params={
            'search': 'test query',
            'page': 2,
            'country_code': 'us',
            'language': 'en',
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Amazon API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_amazon_search(mock_session, client):
    '''It should make an Amazon Search request'''
    client.amazon_search('laptop')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/search',
        params={'query': 'laptop'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_search_with_params(mock_session, client):
    '''It should add parameters to Amazon Search request'''
    client.amazon_search('laptop', params={'domain': 'com', 'pages': 2})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/search',
        params={'query': 'laptop', 'domain': 'com', 'pages': 2},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_product(mock_session, client):
    '''It should make an Amazon Product request'''
    client.amazon_product('B0D2Q9397Y')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/product',
        params={'query': 'B0D2Q9397Y'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_product_with_params(mock_session, client):
    '''It should add parameters to Amazon Product request'''
    client.amazon_product('B0D2Q9397Y', params={'domain': 'com'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/product',
        params={'query': 'B0D2Q9397Y', 'domain': 'com'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_pricing(mock_session, client):
    '''It should make an Amazon Pricing request'''
    client.amazon_pricing('B0DPDRNSXV')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/pricing',
        params={'asin': 'B0DPDRNSXV'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_pricing_with_params(mock_session, client):
    '''It should add parameters to Amazon Pricing request'''
    client.amazon_pricing('B0DPDRNSXV', params={'domain': 'com', 'light_request': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/pricing',
        params={
            'asin': 'B0DPDRNSXV',
            'domain': 'com',
            'light_request': True,
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Walmart API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_walmart_search(mock_session, client):
    '''It should make a Walmart Search request'''
    client.walmart_search('laptop')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/search',
        params={'query': 'laptop'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_walmart_search_with_params(mock_session, client):
    '''It should add parameters to Walmart Search request'''
    client.walmart_search('laptop', params={'sort_by': 'best_match'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/search',
        params={'query': 'laptop', 'sort_by': 'best_match'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_walmart_product(mock_session, client):
    '''It should make a Walmart Product request'''
    client.walmart_product('123456789')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/product',
        params={'product_id': '123456789'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_walmart_product_with_params(mock_session, client):
    '''It should add parameters to Walmart Product request'''
    client.walmart_product('123456789', params={'device': 'desktop'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/product',
        params={'product_id': '123456789', 'device': 'desktop'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# YouTube API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_youtube_search(mock_session, client):
    '''It should make a YouTube Search request'''
    client.youtube_search('web scraping')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/search',
        params={'search': 'web scraping'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_search_with_params(mock_session, client):
    '''It should add parameters to YouTube Search request'''
    client.youtube_search('web scraping', params={'sort_by': 'relevance', 'type': 'video'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/search',
        params={'search': 'web scraping', 'sort_by': 'relevance', 'type': 'video'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_metadata(mock_session, client):
    '''It should make a YouTube Metadata request'''
    client.youtube_metadata('dQw4w9WgXcQ')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/metadata',
        params={'video_id': 'dQw4w9WgXcQ'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_subtitles(mock_session, client):
    '''It should make a YouTube Subtitles request'''
    client.youtube_subtitles('dQw4w9WgXcQ')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/subtitles',
        params={'video_id': 'dQw4w9WgXcQ'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_subtitles_with_params(mock_session, client):
    '''It should add parameters to YouTube Subtitles request'''
    client.youtube_subtitles(
        'dQw4w9WgXcQ',
        params={'language': 'en', 'subtitle_origin': 'uploader_provided'}
    )

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/subtitles',
        params={
            'video_id': 'dQw4w9WgXcQ',
            'language': 'en',
            'subtitle_origin': 'uploader_provided',
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# ChatGPT API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_chatgpt(mock_session, client):
    '''It should make a ChatGPT request'''
    client.chatgpt('What is web scraping?')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/chatgpt',
        params={'prompt': 'What is web scraping?'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_chatgpt_with_params(mock_session, client):
    '''It should add parameters to ChatGPT request'''
    client.chatgpt('What is web scraping?', params={'search': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/chatgpt',
        params={'prompt': 'What is web scraping?', 'search': True},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Gemini API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_gemini(mock_session, client):
    '''It should make a Gemini request'''
    client.gemini('What is web scraping?')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/gemini',
        params={'prompt': 'What is web scraping?'},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


@mock.patch('scrapingbee.client.Session')
def test_gemini_with_params(mock_session, client):
    '''It should add parameters to Gemini request'''
    client.gemini('What is web scraping?', params={'country_code': 'us', 'add_html': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/gemini',
        params={
            'prompt': 'What is web scraping?',
            'country_code': 'us',
            'add_html': True,
        },
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Usage API Tests
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_usage(mock_session, client):
    '''It should make a Usage request'''
    client.usage()

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/usage',
        params={},
        data=None,
        headers={**DEFAULT_HEADERS, **AUTH_HEADERS}
    )


# ============================================
# Auth invariant: every method authenticates via header, never query param
# ============================================

@pytest.mark.parametrize('call', [
    lambda c: c.html_api('https://httpbin.org'),
    lambda c: c.html_api('https://httpbin.org', method='POST'),
    lambda c: c.google_search('test'),
    lambda c: c.fast_search('test'),
    lambda c: c.amazon_search('laptop'),
    lambda c: c.amazon_product('B0D2Q9397Y'),
    lambda c: c.amazon_pricing('B0DPDRNSXV'),
    lambda c: c.walmart_search('laptop'),
    lambda c: c.walmart_product('123456789'),
    lambda c: c.youtube_search('test'),
    lambda c: c.youtube_metadata('dQw4w9WgXcQ'),
    lambda c: c.youtube_subtitles('dQw4w9WgXcQ'),
    lambda c: c.chatgpt('hi'),
    lambda c: c.gemini('hi'),
    lambda c: c.usage(),
], ids=[
    'html_api_get', 'html_api_post', 'google_search', 'fast_search',
    'amazon_search', 'amazon_product', 'amazon_pricing', 'walmart_search',
    'walmart_product', 'youtube_search', 'youtube_metadata',
    'youtube_subtitles', 'chatgpt', 'gemini', 'usage',
])
@mock.patch('scrapingbee.client.Session')
def test_every_method_authenticates_via_header(mock_session, call, client):
    '''No method may put api_key in the query params or lose the Bearer header'''
    call(client)

    _, kwargs = mock_session.return_value.request.call_args
    assert 'api_key' not in kwargs['params']
    assert kwargs['headers']['Authorization'] == 'Bearer API_KEY'


@mock.patch('scrapingbee.client.Session')
def test_caller_headers_cannot_override_auth(mock_session, client):
    '''A user-supplied Authorization header must not clobber authentication'''
    client.html_api('https://httpbin.org', headers={'Authorization': 'target-site-token'})

    _, kwargs = mock_session.return_value.request.call_args
    assert kwargs['headers']['Authorization'] == 'Bearer API_KEY'
    # the user's header is forwarded to the target site under the Spb- prefix
    assert kwargs['headers']['Spb-Authorization'] == 'target-site-token'
