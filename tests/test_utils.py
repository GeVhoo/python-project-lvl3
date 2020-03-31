import pytest
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from page_loader.utils import (create_folder,
                               make_request,
                               find_local_resources,
                               get_content_type)

URL = 'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/index'
RESOURCE_LIST = [
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/style/style.css',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/python.png',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/requests.jpg',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/bs.jpg'  # noqa: E501
]


def test_make_request_exceptions():
    with pytest.raises(HTTPError) as error:
        make_request('https://httpbin.org/status/400')
    assert 'Client Error' in str(error)


def test_make_request():
    response = make_request('https://httpbin.org/status/200')
    assert 200 <= response.status_code < 500


def test_create_folder_exceptions():
    with pytest.raises(PermissionError) as error:
        create_folder('/new')
    assert 'Permission denied' in str(error)


def test_get_contetn_type():
    response = make_request('https://httpbin.org/image/jpeg')
    data, write_mod = get_content_type(response)
    assert write_mod == 'bw'


def test_find_local_resource():
    with open('./tests/fixtures/index.html') as f:
        html_doc = f.read()
    html_data = BeautifulSoup(html_doc, 'html.parser')
    local_resources = find_local_resources(html_data, URL)
    assert local_resources[0][0] == RESOURCE_LIST[0]
    assert local_resources[1][0] == RESOURCE_LIST[1]
    assert local_resources[2][0] == RESOURCE_LIST[2]
    assert local_resources[3][0] == RESOURCE_LIST[3]
