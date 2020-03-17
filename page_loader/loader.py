import logging
from progress.bar import Bar
from page_loader import getter

logger = logging.getLogger()


# Writing data to disk
def load(path, data, write_mod='w'):
    try:
        with open(path, write_mod) as f:
            if write_mod == 'wb':
                for chunk in data.iter_content(8192):
                    f.write(chunk)
            else:
                f.write(data)
    except PermissionError:
        logger.error(f'Permission denied: {path}')
        raise


# Downloading resources and change links in html file
def load_local_resource(local_resource,
                        count_of_resource,
                        path_for_folder,
                        base_url):
    logger.info('Start downloading local resources')
    with Bar('Processing', max=count_of_resource) as bar:
        for key, value in local_resource.items():
            resource_url = getter.get_resource_url(base_url, key)
            logger.debug(f'Start downloading: {resource_url}')
            response = getter.get_response(resource_url, url_type='resource')
            data, write_mod = getter.get_content_type(response)
            file_path = getter.get_resource_path(path_for_folder, key)
            load(file_path, data, write_mod)
            value['tag'][value['type']] = file_path
            logger.debug(f'File downloaded to: {file_path}')
            bar.next()
