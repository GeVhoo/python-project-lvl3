import logging
from progress.bar import Bar
from page_loader import utils
from page_loader.names_paths_urls import get_resource_path

logger = logging.getLogger()


# Writing data to disk
def save(path, data, write_mod='w'):
    try:
        with open(path, write_mod) as f:
            f.write(data)
    except PermissionError:
        logger.error(f'Permission denied: {path}')
        raise


# Save resources and change links in html file
def save_local_resource(local_resource, folder_path):
    logger.info('Start downloading local resources')
    with Bar('Processing', max=len(local_resource)) as bar:
        for item in local_resource:
            resource_url = item[0]
            resource_path = item[1]
            tag = item[2]
            attribute = item[3]
            logger.debug(f'Start downloading: {resource_url}')
            response = utils.make_request(resource_url, url_type='resource')
            data, write_mod = utils.get_content_type(response)
            file_path = get_resource_path(folder_path, resource_path)
            save(file_path, data, write_mod)
            tag[attribute] = file_path
            logger.debug(f'File downloaded to: {file_path}')
            bar.next()
