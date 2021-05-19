from unittest import mock

import pytest

from scrapingbee import ScrapingBeeClient


@pytest.fixture(scope='module')
def scrapingbee():
    return ScrapingBeeClient(api_key='API_KEY')


@mock.patch('scrapingbee.client.request')
def test_get(mock_request, scrapingbee):
    '''It should make a GET request with the url and API key'''
    scrapingbee.get('https://httpbin.org')

    mock_request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A//httpbin.org',
        data=None,
        headers=None
    )


@mock.patch('scrapingbee.client.request')
def test_get_with_params(mock_request, scrapingbee):
    '''It should add parameters to the url'''
    scrapingbee.get('https://httpbin.org', params={'render_js': True})

    mock_request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A//httpbin.org&render_js=True',
        data=None,
        headers=None,
    )


@mock.patch('scrapingbee.client.request')
def test_get_with_headers(mock_request, scrapingbee):
    '''It should prefix header names with Spb- and set forward_headers'''
    scrapingbee.get('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A//httpbin.org&forward_headers=True',
        data=None,
        headers={'Spb-Content-Type': 'text/html; charset=utf-8'},
    )


@mock.patch('scrapingbee.client.request')
def test_get_with_cookies(mock_request, scrapingbee):
    '''It should format the cookies and add them to the url'''
    scrapingbee.get('https://httpbin.org', cookies={
        'name_1': 'value_1',
        'name_2': 'value_2',
    })

    mock_request.assert_called_with(
        'GET',
        'https://app.scrapingbee.com/api/v1/'
        '?api_key=API_KEY&url=https%3A//httpbin.org&cookies=name_1=value_1;name_2=value_2',
        data=None,
        headers=None,
    )


@mock.patch('scrapingbee.client.request')
def test_post(mock_request, scrapingbee):
    '''It should make a POST request with some data'''
    scrapingbee.post('https://httpbin.org', data={'KEY_1': 'VALUE_1'})

    mock_request.assert_called_with(
        'POST',
        'https://app.scrapingbee.com/api/v1/?api_key=API_KEY&url=https%3A//httpbin.org',
        data={'KEY_1': 'VALUE_1'},
        headers=None
    )
