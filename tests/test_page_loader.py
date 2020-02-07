from page_loader import cli

FILE_NAME = 'hexlet-io-courses.html'
PATH = 'https://hexlet.io/courses'


def test_result():
    assert FILE_NAME == cli.get_file_name(PATH)
