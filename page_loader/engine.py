import logging
import os
from bs4 import BeautifulSoup

from page_loader import storage
from page_loader.network import make_request


logger = logging.getLogger()


# Download url from the network with local resources
def run(url, path):
    logger.info(f'Start loading {url}')

    html_file_name = storage.get_html_file_name(url)
    folder_name = storage.get_folder_name(html_file_name)
    html_file_path = os.path.join(path, html_file_name)
    directory = os.path.join(path, folder_name)

    # Create folder for local resources
    storage.create_folder(directory)

    # Get data from HTML
    response = make_request(url, mandatory=True).text
    html_data = BeautifulSoup(response, 'html.parser')

    # Get local resources and change links in html file
    local_resource = storage.find_local_resources(html_data, url, directory)

    # Save html file
    storage.save(html_file_path, html_data.prettify())
    logger.info(f'HTML file downloaded to: {html_file_path}')

    # Save local resources
    storage.save_local_resource(local_resource)
    logger.info('Download complite!')
