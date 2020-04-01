import logging
import re
import os

from progress.bar import Bar
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urljoin

from page_loader.network import make_request
from page_loader.network import get_content_type

RESOURCES = {
    'link': 'href',
    'script': 'src',
    'img': 'src',
    }

logger = logging.getLogger()


def url_normalization(url):
    url = url.rstrip('/')
    url = urlparse(url)
    if url.scheme == '' and url.netloc == '':
        return f'https://{url.path}'
    else:
        return urlunparse(url)


def get_html_file_name(url):
    url = urlparse(url)
    url_without_scheme = url.netloc + url.path
    name = re.sub(r'\W', '-', url_without_scheme)
    return f'{name}.html'


def get_folder_name(html_file_name):
    name = html_file_name.rstrip('.html')
    return f'{name}_files'


# Create folder for local resources
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except PermissionError:
        logger.error(f'Permission denied: {directory}')
        raise
    else:
        logger.info(f'Created folder: {directory}')


# Get local resources path to download
def get_resource_path(directory, value):
    value = value.lstrip('/')
    name, ext = os.path.splitext(value)
    file_name = re.sub(r'\W', '-', name) + ext
    return os.path.join(directory, file_name)


# Get a dictionary with all local resources and replace links in html file
def find_local_resources(html_data, url, directory):
    local_resource = {}
    for tag, attribute in RESOURCES.items():
        tag_list = html_data.find_all(tag)
        for element in tag_list:
            resource_path = element.get(attribute)
            if urlparse(resource_path)[1] == '':
                if os.path.splitext(resource_path)[1]:
                    resource_url = urljoin(url, resource_path)
                    file_path = get_resource_path(directory, resource_path)
                    local_resource[resource_url] = file_path
                    element[attribute] = file_path

    if len(local_resource) > 0:
        logger.info(f'{len(local_resource)} local resources found to download')
    else:
        logger.info('No local resources to download')
    return local_resource


# Writing data to disk
def save(path, data, write_mod='w'):
    try:
        with open(path, write_mod) as f:
            f.write(data)
    except PermissionError:
        logger.error(f'Permission denied: {path}')
        raise


# Save local resources to disk
def save_local_resource(local_resource):
    logger.info('Start loading local resources')
    with Bar('Processing', max=len(local_resource)) as bar:
        for resource_url, file_path in local_resource.items():
            logger.debug(f'Loading: {resource_url}')
            response = make_request(resource_url, url_type='resource')
            data, write_mod = get_content_type(response)
            save(file_path, data, write_mod)
            logger.debug(f'File downloaded to: {file_path}')
            bar.next()
