from page_loader.names_paths_urls import (url_normalization,
                                          get_host_name,
                                          get_html_file_name,
                                          get_folder_name,
                                          get_resource_path)

URL1 = 'https://ru.hexlet.io/courses'
URL2 = 'ru.hexlet.io/courses'
HOST1 = 'https://ru.hexlet.io'
HTML_FILE_NAME = 'ru-hexlet-io-courses.html'
FOLDER_NAME = 'ru-hexlet-io-courses_files'
RESOURCE = '/assets/application.css'
RESOURCE_PATH = 'ru-hexlet-io-courses_files/assets-application.css'


def test_url_normalization():
    assert url_normalization(URL1) == URL1
    assert url_normalization(URL2) == URL1


def test_get_host_name():
    assert get_host_name(URL1) == HOST1


def test_get_html_file_name():
    assert get_html_file_name(URL1) == HTML_FILE_NAME


def test_get_folder_name():
    html_file_name = get_html_file_name(URL1)
    assert get_folder_name(html_file_name) == FOLDER_NAME


def test_get_resource_path():
    assert get_resource_path(FOLDER_NAME, RESOURCE) == RESOURCE_PATH
