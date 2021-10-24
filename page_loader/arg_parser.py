#!/usr/bin/env python3


import argparse
import os


def arg_parser():
    desc_prog = 'Hexlet tutorial project, web page loader.'
    parse = argparse.ArgumentParser(description=desc_prog)
    home_dir = os.getcwd()
    text_help = 'Specify the directory where the page is saved'
    parse.add_argument('-o', '--output', default=home_dir,
                       metavar='OUTPUT', help=text_help)
    text_help_url = 'Specify the URL of the loaded page'
    parse.add_argument('URL', help=text_help_url)
    return parse.parse_args()
