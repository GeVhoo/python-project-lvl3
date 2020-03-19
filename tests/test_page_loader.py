import tempfile
import os
import pytest
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from page_loader import getter
from page_loader import loader
from page_loader import cli
from tests.fixtures.const import (URL,
                                  FOLDER_NAME,
                                  HTML_FILE_NAME,
                                  BASE,
                                  RESOURCE_TRUE,
                                  PATH,
                                  RESOURCE_PATH,
                                  HTML_DOC)


def get_temp_folder():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return tmpdirname


tmpdir = get_temp_folder()


def test_get_response_exceptions():
    with pytest.raises(HTTPError) as error:
        getter.get_response('http://example.com/404')
    assert 'Client Error' in str(error)


def test_get_response():
    response = getter.get_response(URL)
    assert 200 <= response.status_code < 400


def test_base_variables():
    assert BASE == getter.get_base_variables(URL)


def test_resource_path():
    assert RESOURCE_PATH == getter.get_resource_path(PATH, RESOURCE_TRUE)


def test_get_folder(tmpdir):
    # temp_folder = get_temp_folder()
    path = tmpdir + '/' + FOLDER_NAME
    getter.get_folder(path)
    assert os.path.exists(path) is True


def test_get_folder_exceptions():
    with pytest.raises(PermissionError) as error:
        getter.get_folder('/new')
    assert 'Permission denied' in str(error)


def test_get_contetn_type():
    response = getter.get_response('https://example.com')
    data, write_mod = getter.get_content_type(response)
    assert write_mod == 'w'


def test_get_local_resource():
    soup = BeautifulSoup(HTML_DOC, 'html.parser')
    local_resource, count_of_resource = getter.get_local_resource(soup)
    assert count_of_resource == 3


def test_load(tmpdir):
    file_name = tmpdir + '/new.jpg'
    with open('./tests/fixtures/bs.jpg', 'rb') as f:
        data = f.read()
        loader.load(file_name, data, write_mod='wb')
        f.close()
    assert os.path.exists(file_name) is True


def test_cli(tmpdir):
    args = cli.parser.parse_args([URL, '-o', str(tmpdir)])
    cli.run(args)
    folder_path = str(tmpdir) + '/' + FOLDER_NAME
    html_path = str(tmpdir) + '/' + HTML_FILE_NAME
    assert os.path.exists(folder_path) is True
    assert os.path.exists(html_path) is True
