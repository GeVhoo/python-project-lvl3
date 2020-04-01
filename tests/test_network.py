import pytest

from requests.exceptions import HTTPError

from page_loader.network import make_request
from page_loader.network import get_content_type

URL = 'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/index'
DIRECTORY = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files'
RESOURCE = {
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/style/style.css': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/style-style.css',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/python.png': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-python.png',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/requests.jpg': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-requests.jpg',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/bs.jpg': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-bs.jpg'  # noqa: E501
}


def test_make_request_exceptions():
    with pytest.raises(HTTPError) as error:
        make_request('https://httpbin.org/status/400')
    assert 'Client Error' in str(error)


def test_make_request():
    response = make_request('https://httpbin.org/status/200')
    assert 200 <= response.status_code < 500


def test_get_content_type():
    response = make_request('https://httpbin.org/image/jpeg')
    data, write_mod = get_content_type(response)
    assert write_mod == 'bw'
