from scrapingbee.utils import (
    process_url,
    process_js_snippet,
    process_headers,
    process_cookies,
    process_extract_rules,
    process_params,
    get_scrapingbee_url
)


def test_process_url():
    '''It should encode the url'''
    output = process_url('https://example.com?p=1')
    assert output == 'https%3A//example.com%3Fp%3D1'


def test_process_js_snippet():
    '''It should encode JavaScript code'''
    output = process_js_snippet(
        'window.scrollTo(0, document.body.scrollHeight);')
    assert output == \
        'd2luZG93LnNjcm9sbFRvKDAsIGRvY3VtZW50LmJvZHkuc2Nyb2xsSGVpZ2h0KTs='


def test_process_headers():
    '''It should add a Spb- prefix to header names'''
    output = process_headers({'Accept-Language': 'En-US'})
    assert output == {'Spb-Accept-Language': 'En-US'}


def test_process_cookies():
    '''It should format cookies to a string'''
    output = process_cookies({
        'name_1': 'value_1',
        'name_2': 'value_2'
    })
    assert output == 'name_1=value_1;name_2=value_2'


def test_process_extract_rules():
    '''It should format extract_rules to a stringified JSON'''
    output = process_extract_rules({
        'title': '.title'
    })
    assert output == '%7B%22title%22%3A%20%22.title%22%7D'


def test_process_params():
    '''It should keep boolean parameters'''
    output = process_params({'render_js': True})
    assert output == {'render_js': True}


def test_get_scrapingbee_url():
    '''It should generate a url'''
    output = get_scrapingbee_url(
        'https://app.scrapingbee.com/api/v1/',
        'API_KEY',
        'https://httpbin.org',
        {'render_js': True}
    )
    assert output == 'https://app.scrapingbee.com/api/v1/' \
        '?api_key=API_KEY&url=https%3A//httpbin.org&render_js=True'
