from page_loader import getter

PATH = 'https://hexlet.io/courses'
HTML_FILE_NAME = 'hexlet-io-courses.html'
FOLDER_NAME = 'hexlet-io-courses_files'
BASE_URL = 'https://hexlet.io'
BASE = BASE_URL, HTML_FILE_NAME, FOLDER_NAME


def test_result():
    assert BASE == getter.get_base_variables(PATH)
