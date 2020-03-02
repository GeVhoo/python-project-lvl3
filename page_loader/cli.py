import argparse
import requests
from bs4 import BeautifulSoup
from page_loader.constants import RESOURCES
from page_loader import getter
import logging

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


def run(args):
    url = args.url
    path = args.output
    logging_level = args.level
    if logging_level == 'info':
        logging_level = 'INFO'
    elif logging_level == 'debug':
        logging_level = 'DEBUG'
    logging.basicConfig(format='[%(levelname)s]: %(message)s',
                        level=logging_level)

    logging.info(f'Start downloading {url}')

    base_url, html_file_name, folder_name = getter.get_base_variables(url)

    if path is None:
        path_for_html_file = html_file_name
        path_for_folder = folder_name
    else:
        path_for_html_file = path + '/' + html_file_name
        path_for_folder = path + '/' + folder_name

    path_for_resourses = getter.get_folder(path_for_folder)

    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')

    logging.info('Start downloading local resources')
    index = 0
    for tag, attr in RESOURCES.items():
        tag_list = soup.find_all(tag)
        for item in tag_list:
            value = item.get(attr)
            resource_url = getter.get_resource_url(base_url, value)
            if resource_url:
                logging.debug(f'Start downloading: {value}')
                response = requests.get(resource_url)
                data, write_mod = getter.get_content_type(response)
                file_path = getter.get_resource_path(path_for_resourses, value)
                index += 1

                with open(file_path, write_mod) as f:
                    f.write(data)
                item[attr] = file_path
                logging.debug(f'File downloaded to: {file_path}')
    if index == 0:
        message = 'No local resources to download'
    else:
        message = f'{index} local resources were loaded'
    logging.info(message)

    with open(path_for_html_file, 'w') as f:
        f.write(soup.prettify())
    logging.info('Download complite!')
