from unittest import mock

import pytest

from scrapingbee import ScrapingBeeClient
from scrapingbee.utils import DEFAULT_HEADERS


@pytest.fixture(scope='module')
def client():
    return ScrapingBeeClient(api_key='API_KEY')


# ============================================
# Legacy HTML API Tests (get)
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_get(mock_session, client):
    '''It should make a GET request with the url and API key'''
    client.get('https://httpbin.org')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org'},
        data=None,
        headers=DEFAULT_HEADERS
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_params(mock_session, client):
    '''It should add parameters to the request'''
    client.get('https://httpbin.org', params={'render_js': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org', 'render_js': True},
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_headers(mock_session, client):
    '''It should prefix header names with Spb- and set forward_headers'''
    client.get('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org', 'forward_headers': True},
        data=None,
        headers={'Spb-Content-Type': 'text/html; charset=utf-8', **DEFAULT_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_cookies(mock_session, client):
    '''It should format the cookies and add them to the params'''
    client.get('https://httpbin.org', cookies={
        'name_1': 'value_1',
        'name_2': 'value_2',
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org', 'cookies': 'name_1=value_1;name_2=value_2'},
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_extract_rules(mock_session, client):
    '''It should format the extract_rules and add them to the params'''
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
            'api_key': 'API_KEY',
            'url': 'https://httpbin.org',
            'extract_rules': '{"title": "h1", "subtitle": "#subtitle"}'
        },
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_js_scenario(mock_session, client):
    '''It should format the js_scenario and add them to the params'''
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
            'api_key': 'API_KEY',
            'url': 'https://httpbin.org',
            'js_scenario': '{"instructions": [{"click": "#buttonId"}]}'
        },
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_ai_extract_rules(mock_session, client):
    '''It should format the ai_extract_rules and add them to the params'''
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
            'api_key': 'API_KEY',
            'url': 'https://httpbin.org',
            'ai_extract_rules': '{"product_name": "The name of the product", "price": "The price in USD"}'
        },
        data=None,
        headers=DEFAULT_HEADERS,
    )


# ============================================
# Legacy HTML API Tests (post)
# ============================================

@mock.patch('scrapingbee.client.Session')
def test_post(mock_session, client):
    '''It should make a POST request with some data'''
    client.post('https://httpbin.org', data={'KEY_1': 'VALUE_1'})

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org'},
        data={'KEY_1': 'VALUE_1'},
        headers=DEFAULT_HEADERS
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
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org'},
        data=None,
        headers=DEFAULT_HEADERS
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_post(mock_session, client):
    '''It should make a POST request with html_api'''
    client.html_api('https://httpbin.org', method='POST')

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org'},
        data=None,
        headers=DEFAULT_HEADERS
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_params(mock_session, client):
    '''It should add parameters to html_api request'''
    client.html_api('https://httpbin.org', params={'render_js': True, 'premium_proxy': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org', 'render_js': True, 'premium_proxy': True},
        data=None,
        headers=DEFAULT_HEADERS
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_with_headers(mock_session, client):
    '''It should prefix header names with Spb- and set forward_headers'''
    client.html_api('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org', 'forward_headers': True},
        data=None,
        headers={'Spb-Content-Type': 'text/html; charset=utf-8', **DEFAULT_HEADERS},
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
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org', 'cookies': 'name_1=value_1;name_2=value_2'},
        data=None,
        headers=DEFAULT_HEADERS,
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
                'api_key': 'API_KEY',
                'url': 'https://httpbin.org',
                'cookies': 'session=abc123',
                'forward_headers': True
            },
        data=None,
        headers={'Spb-X-Custom': 'value', **DEFAULT_HEADERS}
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
            'api_key': 'API_KEY',
            'url': 'https://httpbin.org',
            'extract_rules': '{"title": "h1", "subtitle": "#subtitle"}'
        },
        data=None,
        headers=DEFAULT_HEADERS,
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
            'api_key': 'API_KEY',
            'url': 'https://httpbin.org',
            'js_scenario': '{"instructions": [{"click": "#buttonId"}]}'
        },
        data=None,
        headers=DEFAULT_HEADERS,
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
            'api_key': 'API_KEY',
            'url': 'https://httpbin.org',
            'ai_extract_rules': '{"product_name": "The name of the product", "price": "The price in USD"}'
        },
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_html_api_post_with_data(mock_session, client):
    '''It should make a POST request with some data'''
    client.html_api('https://httpbin.org', method='POST', data={'KEY_1': 'VALUE_1'})

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/',
        params={'api_key': 'API_KEY', 'url': 'https://httpbin.org'},
        data={'KEY_1': 'VALUE_1'},
        headers=DEFAULT_HEADERS
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
        params={'api_key': 'API_KEY', 'search': 'test query'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_google_search_with_params(mock_session, client):
    '''It should add parameters to Google Search request'''
    client.google_search('test query', params={'language': 'en', 'country_code': 'us'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/store/google',
        params={'api_key': 'API_KEY', 'search': 'test query', 'language': 'en', 'country_code': 'us'},
        data=None,
        headers=None
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
        params={'api_key': 'API_KEY', 'query': 'laptop'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_search_with_params(mock_session, client):
    '''It should add parameters to Amazon Search request'''
    client.amazon_search('laptop', params={'domain': 'com', 'pages': 2})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/search',
        params={'api_key': 'API_KEY', 'query': 'laptop', 'domain': 'com', 'pages': 2},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_product(mock_session, client):
    '''It should make an Amazon Product request'''
    client.amazon_product('B0D2Q9397Y')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/product',
        params={'api_key': 'API_KEY', 'query': 'B0D2Q9397Y'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_amazon_product_with_params(mock_session, client):
    '''It should add parameters to Amazon Product request'''
    client.amazon_product('B0D2Q9397Y', params={'domain': 'com'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/amazon/product',
        params={'api_key': 'API_KEY', 'query': 'B0D2Q9397Y', 'domain': 'com'},
        data=None,
        headers=None
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
        params={'api_key': 'API_KEY', 'query': 'laptop'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_walmart_search_with_params(mock_session, client):
    '''It should add parameters to Walmart Search request'''
    client.walmart_search('laptop', params={'sort_by': 'best_match'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/search',
        params={'api_key': 'API_KEY', 'query': 'laptop', 'sort_by': 'best_match'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_walmart_product(mock_session, client):
    '''It should make a Walmart Product request'''
    client.walmart_product('123456789')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/product',
        params={'api_key': 'API_KEY', 'product_id': '123456789'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_walmart_product_with_params(mock_session, client):
    '''It should add parameters to Walmart Product request'''
    client.walmart_product('123456789', params={'device': 'desktop'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/walmart/product',
        params={'api_key': 'API_KEY', 'product_id': '123456789', 'device': 'desktop'},
        data=None,
        headers=None
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
        params={'api_key': 'API_KEY', 'search': 'web scraping'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_search_with_params(mock_session, client):
    '''It should add parameters to YouTube Search request'''
    client.youtube_search('web scraping', params={'sort_by': 'relevance', 'type': 'video'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/search',
        params={'api_key': 'API_KEY', 'search': 'web scraping', 'sort_by': 'relevance', 'type': 'video'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_metadata(mock_session, client):
    '''It should make a YouTube Metadata request'''
    client.youtube_metadata('dQw4w9WgXcQ')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/metadata',
        params={'api_key': 'API_KEY', 'video_id': 'dQw4w9WgXcQ'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_transcript(mock_session, client):
    '''It should make a YouTube Transcript request'''
    client.youtube_transcript('dQw4w9WgXcQ')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/transcript',
        params={'api_key': 'API_KEY', 'video_id': 'dQw4w9WgXcQ'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_transcript_with_params(mock_session, client):
    '''It should add parameters to YouTube Transcript request'''
    client.youtube_transcript('dQw4w9WgXcQ', params={'language': 'en'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/transcript',
        params={'api_key': 'API_KEY', 'video_id': 'dQw4w9WgXcQ', 'language': 'en'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_youtube_trainability(mock_session, client):
    '''It should make a YouTube Trainability request'''
    client.youtube_trainability('dQw4w9WgXcQ')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/youtube/trainability',
        params={'api_key': 'API_KEY', 'video_id': 'dQw4w9WgXcQ'},
        data=None,
        headers=None
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
        params={'api_key': 'API_KEY', 'prompt': 'What is web scraping?'},
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.Session')
def test_chatgpt_with_params(mock_session, client):
    '''It should add parameters to ChatGPT request'''
    client.chatgpt('What is web scraping?', params={'search': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/chatgpt',
        params={'api_key': 'API_KEY', 'prompt': 'What is web scraping?', 'search': True},
        data=None,
        headers=None
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
        params={'api_key': 'API_KEY'},
        data=None,
        headers=None
    )
