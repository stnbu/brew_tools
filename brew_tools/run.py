# -*- coding: utf-8 -*-

import argparse
from main import BrewTools

def get_parser():
    parser = argparse.ArgumentParser(description='Manage name-mangeled GNU commands provided by brew (e.g. "gsed").')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u',
        '--unconditional-link',
        metavar='tool_name',
        nargs='+',
        help='List of GNU tools to include even if they are not present in [/usr]/bin',
        required=False)

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('-c', '--create', dest='create', action='store_true')
    mode.add_argument('-d', '--delete', dest='delete', action='store_true')
    return parser

def run():

    args = get_parser().parse_args()
    brew_tools = BrewTools(unconditional_link=args.unconditional_link)
    if args.create:
        brew_tools.create()
    elif args.delete:
        brew_tools.delete()

if __name__ == '__main__':
    run()
