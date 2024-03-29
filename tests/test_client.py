from unittest import mock

import pytest

from scrapingbee import ScrapingBeeClient
from scrapingbee.utils import DEFAULT_HEADERS


@pytest.fixture(scope='module')
def client():
    return ScrapingBeeClient(api_key='API_KEY')


@mock.patch('scrapingbee.client.Session')
def test_get(mock_session, client):
    '''It should make a GET request with the url and API key'''
    client.get('https://httpbin.org')

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org',
        data=None,
        headers=DEFAULT_HEADERS
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_params(mock_session, client):
    '''It should add parameters to the url'''
    client.get('https://httpbin.org', params={'render_js': True})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&render_js=True',
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_headers(mock_session, client):
    '''It should prefix header names with Spb- and set forward_headers'''
    client.get('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&forward_headers=True',
        data=None,
        headers={'Spb-Content-Type': 'text/html; charset=utf-8',
                 **DEFAULT_HEADERS},
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_cookies(mock_session, client):
    '''It should format the cookies and add them to the url'''
    client.get('https://httpbin.org', cookies={
        'name_1': 'value_1',
        'name_2': 'value_2',
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&cookies=name_1%3Dvalue_1%3Bname_2%3Dvalue_2',
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_extract_rules(mock_session, client):
    '''It should format the extract_rules and add them to the url'''
    client.get('https://httpbin.org', params={
        'extract_rules': {
            "title": "h1",
            "subtitle": "#subtitle"
        }
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&'
        'extract_rules=%7B%22title%22%3A+%22h1%22%2C+%22'
        'subtitle%22%3A+%22%23subtitle%22%7D',
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_get_with_js_scenario(mock_session, client):
    '''It should format the extract_rules and add them to the url'''
    client.get('https://httpbin.org', params={
        'js_scenario': {
            'instructions': [
                {"click": "#buttonId"}
            ]
        }
    })

    mock_session.return_value.request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&'
        'js_scenario=%7B%22instructions%22%3A+%5B%7B%22click%22%3A+%22%23buttonId%22%7D%5D%7D',
        data=None,
        headers=DEFAULT_HEADERS,
    )


@mock.patch('scrapingbee.client.Session')
def test_post(mock_session, client):
    '''It should make a POST request with some data'''
    client.post('https://httpbin.org', data={'KEY_1': 'VALUE_1'})

    mock_session.return_value.request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org',
        data={'KEY_1': 'VALUE_1'},
        headers=DEFAULT_HEADERS
    )
