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

logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)


def run(args):
    url = args.url
    path = args.output
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

    # Запустить цикл
    for tag, attr in RESOURCES.items():
        tag_list = soup.find_all(tag)
        for item in tag_list:
            value = item.get(attr)
            resource_url = getter.get_resource_url(base_url, value)
            if resource_url:
                response = requests.get(resource_url)
                data, write_mod = getter.get_content_type(response)
                file_path = getter.get_resource_path(path_for_resourses, value)

                with open(file_path, write_mod) as f:
                    f.write(data)
                item[attr] = file_path

    with open(path_for_html_file, 'w') as f:
        f.write(soup.prettify())
    logging.info('Download complite!')
