import logging
import requests


def make_request(url, *, mandatory=False):
    logger = logging.getLogger()
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as e:
        if mandatory is False:
            logger.debug(f'Resource not downloaded: {url}',
                         f' HTTP error occurred: {e}')
        else:
            logger.error(f'HTTP error occurred: {e}')
            raise
    return response


# Get content type (text or not) and write mod
def get_content_type(resource_url_response):
    header = resource_url_response.headers
    if header['Content-Type'].startswith('text'):
        resource = (resource_url_response.text, 'w')
    else:
        resource = (resource_url_response.content, 'bw')
    return resource
