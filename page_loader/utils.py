from urllib.parse import urlparse
import os
import logging
import requests
from page_loader.constants import RESOURCES

logger = logging.getLogger()


def make_request(url, url_type='html'):
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


# Create folder for local resources
def create_folder(path_for_folder):
    try:
        if not os.path.exists(path_for_folder):
            os.makedirs(path_for_folder)
    except PermissionError:
        logger.error(f'Permission denied: {path_for_folder}')
        raise


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


# Get a list with all local resources to download
def find_local_resources(html_data, host_name):
    local_resource = []
    for tag, attr in RESOURCES.items():
        tag_list = html_data.find_all(tag)
        for item in tag_list:
            resource_path = item.get(attr)
            if urlparse(resource_path)[1] == '':
                if os.path.splitext(resource_path)[1]:
                    resource_url = host_name + resource_path
                    resource_data = (resource_url,
                                     resource_path,
                                     item,
                                     attr)
                    local_resource.append(resource_data)
    if len(local_resource) > 0:
        logger.info(f'{len(local_resource)} local resources found to download')
    else:
        logger.info('No local resources to download')
    return local_resource
