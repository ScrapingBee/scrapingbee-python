from scrapingbee.utils import (
    process_js_snippet,
    process_json_stringify_param,
    process_headers,
    process_cookies,
    process_params,
    get_scrapingbee_url
)


def test_process_js_snippet():
    '''It should encode JavaScript code'''
    output = process_js_snippet(
        'window.scrollTo(0, document.body.scrollHeight);')
    assert output == \
        'd2luZG93LnNjcm9sbFRvKDAsIGRvY3VtZW50LmJvZHkuc2Nyb2xsSGVpZ2h0KTs='


def test_process_headers():
    '''It should add a Spb- prefix to header names'''
    output = process_headers({'Accept-Language': 'En-US'})
    assert output == {
        'User-Agent': 'ScrapingBee-Python/1.2.0',
        'Spb-Accept-Language': 'En-US',
    }


def test_process_cookies():
    '''It should format cookies to a string'''
    output = process_cookies({
        'name_1': 'value_1',
        'name_2': 'value_2',
    })
    assert output == 'name_1=value_1;name_2=value_2'


def test_process_extract_rules():
    '''It should format extract_rules to a stringified JSON'''
    output = process_json_stringify_param({
        'title': '.title'
    }, 'extract_rules')
    assert output == '{"title": ".title"}'


def test_process_js_scenario():
    '''It should format js_scenario to a stringified JSON'''
    output = process_json_stringify_param({
        'instructions': [
            {"click": "#buttonId"}
        ]
    }, 'js_scenario')
    assert output == '{"instructions": [{"click": "#buttonId"}]}'


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
        {'render_js': True, 'wait_for': '#foo'}
    )
    assert output == 'https://app.scrapingbee.com/api/v1/' \
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&render_js=True&wait_for=%23foo'
