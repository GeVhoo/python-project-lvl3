from urllib.parse import urlparse
import re
import os


# Get base url (scheme + netloc), names for html file and resource folder.
def get_base_variables(url):
    url = urlparse(url)

    base_url = url[0] + '://' + url[1]

    url_without_scheme = url[1] + url[2]
    name = re.sub(r'\W', '-', url_without_scheme)

    html_file_name = f'{name}.html'
    folder_name = f'{name}_files'
    return base_url, html_file_name, folder_name


def get_folder(path_for_folder):
    if not os.path.exists(path_for_folder):
        os.makedirs(path_for_folder)
    return os.path.abspath(path_for_folder)


def get_resource_url(base_url, resource_path):
    if urlparse(resource_path)[1] == '':
        if os.path.splitext(resource_path)[1]:
            return base_url + resource_path
    else:
        return None


def get_content_type(resource_url_response):
    header = resource_url_response.headers
    if header['Content-Type'].startswith('text'):
        data = resource_url_response.text
        write_mod = 'w'
    else:
        data = resource_url_response.content
        write_mod = 'bw'
    return data, write_mod


def get_resource_path(path_for_resourses, value):
    name, ext = os.path.splitext(value[1:])
    file_name = re.sub(r'\W', '-', name) + ext
    return path_for_resourses + '/' + file_name
