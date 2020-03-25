import argparse
from bs4 import BeautifulSoup
import os
from page_loader.names_paths_urls import (url_normalization,
                                          get_host_name,
                                          get_html_file_name,
                                          get_folder_name)
from page_loader.save import (save,
                              save_local_resource)
from page_loader.logger import run_logger
from page_loader.utils import (create_folder,
                               make_request,
                               find_local_resources)

parser = argparse.ArgumentParser(description='Page Loader')
parser.add_argument('url', type=str, help='input page url')
parser.add_argument('-o', '--output',
                    type=str,
                    default=None,
                    help='specify the directory to download')
parser.add_argument('-l', '--level',
                    default='info',
                    choices=['info', 'debug'],
                    help='specify logging level: "info", "debug"')


# Download url from the network with local resources
def run(args):
    url = url_normalization(args.url)
    path = args.output
    logging_level = args.level
    # Turn on the logger
    logger = run_logger(logging_level)
    logger.info(f'Start downloading {url}')

    host_name = get_host_name(url)
    html_file_name = get_html_file_name(url)
    folder_name = get_folder_name(html_file_name)
    # Get path if folder is specified
    if path is None:
        path = ''
    html_file_path = os.path.join(path, html_file_name)
    folder_path = os.path.join(path, folder_name)
    # Create folder for local resources
    create_folder(folder_path)
    # Get data from HTML
    response = make_request(url).text
    html_data = BeautifulSoup(response, 'html.parser')
    # Get local resources from html data
    local_resource = find_local_resources(html_data, host_name)
    # Downloading resources and change links in html file
    save_local_resource(local_resource, folder_path)
    # Downloading html file
    save(html_file_path, html_data.prettify())
    logger.info('Download complite!')
