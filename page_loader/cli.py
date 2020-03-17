import argparse
from bs4 import BeautifulSoup
from page_loader.loader import (load, load_local_resource)
from page_loader.logger import get_logger
from page_loader.getter import (get_base_variables,
                                get_folder,
                                get_response,
                                get_local_resource)

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
    url = args.url
    path = args.output
    logging_level = args.level
    # Turn on the logger
    logger = get_logger(logging_level)
    logger.info(f'Start downloading {url}')
    # Get base url (scheme + netloc), names for html file and resource folder
    base_url, html_file_name, folder_name = get_base_variables(url)
    # Get download path if folder is specified
    if path is None:
        path_for_html_file = html_file_name
        path_for_folder = folder_name
    else:
        path_for_html_file = path + '/' + html_file_name
        path_for_folder = path + '/' + folder_name
    # Create folder for local resources
    get_folder(path_for_folder)
    # Parsing url
    data = get_response(url).text
    soup = BeautifulSoup(data, 'html.parser')
    # Get local resources from url
    local_resource, count_of_resource = get_local_resource(soup)
    # Downloading resources and change links in html file
    load_local_resource(local_resource, count_of_resource,
                        path_for_folder, base_url)
    # Downloading html file
    load(path_for_html_file, soup.prettify())
    logger.info('Download complite!')
