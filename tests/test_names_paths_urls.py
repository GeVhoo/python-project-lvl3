from page_loader.names_paths_urls import (url_normalization,
                                          get_html_file_name,
                                          get_folder_name,
                                          get_resource_path)

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


def test_get_resource_path():
    assert get_resource_path(FOLDER_NAME, RESOURCE) == RESOURCE_PATH
