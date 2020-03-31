from urllib.parse import urlparse
from urllib.parse import urlunparse
import re
import os


def url_normalization(url):
    url = url.rstrip('/')
    url = urlparse(url)
    if url[0] == '' and url[1] == '':
        scheme = 'https://'
        netloc = url[2]
        return f'{scheme}{netloc}'
    else:
        return urlunparse(url)


def get_html_file_name(url):
    url = urlparse(url)
    url_without_scheme = url[1] + url[2]
    name = re.sub(r'\W', '-', url_without_scheme)
    return f'{name}.html'


def get_folder_name(html_file_name):
    name = html_file_name.rstrip('.html')
    return f'{name}_files'


# Get local resources path to download
def get_resource_path(folder_path, value):
    value = value.lstrip('/')
    name, ext = os.path.splitext(value)
    file_name = re.sub(r'\W', '-', name) + ext
    return os.path.join(folder_path, file_name)
