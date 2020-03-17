from page_loader import getter

URL = 'https://hexlet.io/courses'
HTML_FILE_NAME = 'hexlet-io-courses.html'
FOLDER_NAME = 'hexlet-io-courses_files'
BASE_URL = 'https://hexlet.io'
RESOURCE_TRUE = '/assets/application.css'
RESOURCE_FALSE = 'https://mc.yandex.ru/metrika/tag.js'
RESOURCE_URL = 'https://hexlet.io/assets/application.css'
PATH = '/home/tests'
RESOURCE_PATH = '/home/tests/assets-application.css'
BASE = BASE_URL, HTML_FILE_NAME, FOLDER_NAME


def test_base_variables():
    assert BASE == getter.get_base_variables(URL)


def test_resource_path():
    assert RESOURCE_PATH == getter.get_resource_path(PATH, RESOURCE_TRUE)
