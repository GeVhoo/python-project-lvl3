import tempfile
import os
from page_loader import cli

URL = 'https://gevhoo.github.io/python-project-lvl3/tests/fixtures/index'
HTML_FILE_NAME = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index.html'  # noqa: E501
RESOURCE1 = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/style-style.css'  # noqa: E501
RESOURCE2 = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-python.png'  # noqa: E501
RESOURCE3 = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-requests.jpg'  # noqa: E501
RESOURCE4 = 'gevhoo-github-io-python-project-lvl3-tests-fixtures-index_files/image-bs.jpg'  # noqa: E501


def test_run():
    with tempfile.TemporaryDirectory() as tmpdir:
        args = cli.parser.parse_args([URL, '-o', str(tmpdir)])
        cli.run(args)
        html_file_path = os.path.join(str(tmpdir), HTML_FILE_NAME)
        with open(html_file_path) as f:
            html_file = f.read()
            assert os.path.join(str(tmpdir), RESOURCE1) in html_file
            assert os.path.join(str(tmpdir), RESOURCE2) in html_file
            assert os.path.join(str(tmpdir), RESOURCE3) in html_file
            assert os.path.join(str(tmpdir), RESOURCE4) in html_file
