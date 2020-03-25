import tempfile
import os
from page_loader import cli

URL = 'https://ru.hexlet.io/courses'
HTML_FILE_NAME = 'ru-hexlet-io-courses.html'
RESOURCE = 'ru-hexlet-io-courses_files/cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min.js'  # noqa: E501


def test_run():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = tmpdirname
        args = cli.parser.parse_args([URL, '-o', str(tmpdir)])
        cli.run(args)
        html_file_path = os.path.join(str(tmpdir), HTML_FILE_NAME)
        with open(html_file_path) as f:
            html_file = f.read()
            resource_path = os.path.join(str(tmpdir), RESOURCE)
            assert resource_path in html_file
