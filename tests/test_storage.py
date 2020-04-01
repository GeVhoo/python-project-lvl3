import pytest
import tempfile
import os

from bs4 import BeautifulSoup

from page_loader.storage import url_normalization
from page_loader.storage import get_html_file_name
from page_loader.storage import get_folder_name
from page_loader.storage import create_folder
from page_loader.storage import get_resource_path
from page_loader.storage import save
from page_loader.storage import find_local_resources

HELLO = 'Hello World!'

URL1 = 'https://ru.hexlet.io/courses'
URL2 = 'ru.hexlet.io/courses'
URL3 = 'ru.hexlet.io/courses/'
URL4 = 'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/index'
HTML_FILE_NAME = 'ru-hexlet-io-courses.html'
HTML_FILE_NAME2 = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index.html'  # noqa: E501
FOLDER_NAME = 'ru-hexlet-io-courses_files'
FOLDER_NAME2 = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files'  # noqa: E501
RESOURCE = '/assets/application.css'
RESOURCE_PATH = 'ru-hexlet-io-courses_files/assets-application.css'

RESOURCES = {
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/style/style.css': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/style-style.css',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/python.png': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-python.png',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/requests.jpg': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-requests.jpg',  # noqa: E501
    'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/image/bs.jpg': 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-bs.jpg'  # noqa: E501
}


def test_url_normalization():
    assert url_normalization(URL1) == URL1
    assert url_normalization(URL2) == URL1
    assert url_normalization(URL3) == URL1
    assert url_normalization(URL4) == URL4


def test_get_html_file_name():
    assert get_html_file_name(URL1) == HTML_FILE_NAME
    assert get_html_file_name(URL4) == HTML_FILE_NAME2


def test_get_folder_name():
    html_file_name = get_html_file_name(URL1)
    html_file_name2 = get_html_file_name(URL4)
    assert get_folder_name(html_file_name) == FOLDER_NAME
    assert get_folder_name(html_file_name2) == FOLDER_NAME2


def test_create_folder_exceptions():
    with pytest.raises(PermissionError) as error:
        create_folder('/new')
    assert 'Permission denied' in str(error)


def test_get_resource_path():
    assert get_resource_path(FOLDER_NAME, RESOURCE) == RESOURCE_PATH


def test_save():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_name = os.path.join(str(tmpdir), 'new.jpg')
        with open('./tests/fixtures/image/bs.jpg', 'rb') as ef:
            expected_file = ef.read()
            save(file_name, expected_file, write_mod='wb')
            with open(file_name, 'rb') as nf:
                new_file = nf.read()
                assert new_file == expected_file


def test_save_exceptions():
    with pytest.raises(PermissionError) as error:
        save('/new.html', HELLO)
    assert 'Permission denied' in str(error)


def test_find_local_resource():
    with open('./tests/fixtures/index.html') as f:
        html_doc = f.read()
    html_data = BeautifulSoup(html_doc, 'html.parser')
    assert find_local_resources(html_data, URL4, FOLDER_NAME2) == RESOURCES
