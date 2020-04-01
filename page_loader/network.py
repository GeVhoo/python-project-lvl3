import logging
import requests

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
