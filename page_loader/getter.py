from urllib.parse import urlparse
import re
import os
import logging
import requests
from page_loader.constants import RESOURCES

logger = logging.getLogger()


def get_response(url, url_type='html'):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as e:
        if url_type == 'resource':
            logger.debug(f'Resource not downloaded: {url}',
                         f' HTTP error occurred: {e}')
        else:
            logger.error(f'HTTP error occurred: {e}')
            raise
    return response


# Get base url (scheme + netloc), names for html file and resource folder
def get_base_variables(url):
    url = urlparse(url)

    base_url = url[0] + '://' + url[1]

    url_without_scheme = url[1] + url[2]
    name = re.sub(r'\W', '-', url_without_scheme)

    html_file_name = f'{name}.html'
    folder_name = f'{name}_files'
    return base_url, html_file_name, folder_name


# Create folder for local resources
def get_folder(path_for_folder):
    try:
        if not os.path.exists(path_for_folder):
            os.makedirs(path_for_folder)
    except FileExistsError:
        logger.error(f'This folder already exists: {path_for_folder}')
    except PermissionError:
        logger.error(f'Permission denied: {path_for_folder}')
        raise


# Get local resources url to download
def get_resource_url(base_url, resource_path):
    return base_url + resource_path


# Get content type (text or not) and write mod
def get_content_type(resource_url_response):
    header = resource_url_response.headers
    if header['Content-Type'].startswith('text'):
        data = resource_url_response.text
        write_mod = 'w'
    else:
        data = resource_url_response.content
        write_mod = 'bw'
    return data, write_mod


# Get local resources path to download
def get_resource_path(path_for_resourses, value):
    name, ext = os.path.splitext(value[1:])
    file_name = re.sub(r'\W', '-', name) + ext
    return path_for_resourses + '/' + file_name


# Get a dictionary with all local resources to download
def get_local_resource(soup):
    local_resource = {}
    for tag, attr in RESOURCES.items():
        tag_list = soup.find_all(tag)
        for item in tag_list:
            resource_path = item.get(attr)
            if urlparse(resource_path)[1] == '':
                if os.path.splitext(resource_path)[1]:
                    local_resource[resource_path] = {
                        'tag': item,
                        'type': attr
                    }
    count_of_resource = len(local_resource)
    if count_of_resource > 0:
        message = f'{count_of_resource} local resources found to download'
    else:
        message = 'No local resources to download'
    logger.info(message)
    return local_resource, count_of_resource
