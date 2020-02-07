import argparse
import requests
import re

parser = argparse.ArgumentParser(description='Page Loader')
parser.add_argument('adress', type=str, help='input page address')
parser.add_argument('-o', '--output',
                    help='specify the path to download')


def run(args):
    adress = args.adress
    page_data = requests.get(adress).text
    file_name = get_file_name(adress)
    with open(file_name, 'w') as f:
        f.write(page_data)


def get_file_name(path):
    path = re.split(r'https://|http://', path)[1]
    path = re.sub(r'\W', '-', path)
    return f'{path}.html'
