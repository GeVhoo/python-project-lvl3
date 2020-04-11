import pytest

from requests.exceptions import HTTPError

from page_loader.network import make_request
from page_loader.network import get_content_type


def test_make_request_exceptions():
    with pytest.raises(HTTPError) as error:
        make_request('https://httpbin.org/status/400', mandatory=True)
    assert 'Client Error' in str(error)


def test_make_request():
    response = make_request('https://httpbin.org/status/200')
    assert 200 <= response.status_code < 500


def test_get_content_type():
    response = make_request('https://httpbin.org/image/jpeg')
    data, write_mod = get_content_type(response)
    assert write_mod == 'bw'
