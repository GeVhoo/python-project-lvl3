import argparse

parser = argparse.ArgumentParser(description='Page Loader')
parser.add_argument('url', type=str, help='input page url')
parser.add_argument('-o', '--output',
                    default='',
                    type=str,
                    help='specify the directory to download')
parser.add_argument('-l', '--level',
                    default='info',
                    type=str,
                    choices=['info', 'debug'],
                    help='specify logging level: "info", "debug"')
