#!/usr/bin/env python3


import requests
import re
import os


def download(url, path):
    url_with_out_http = re.search(r'(?<=:\/\/).+', url)[0]
    file_name = re.sub(r'\W', '-', url_with_out_http)
    file_name = file_name[:-1] if file_name[-1] == "-" else file_name
    file_name += ".html"
    file_name_with_path = os.path.join(path, file_name)
    with open(file_name_with_path, 'w', encoding='utf-8') as file:
        page = requests.get(url)
        file.write(page.text)
        file.close()
    return os.path.join(os.path.abspath(path), file_name)


def folder_create(file_paht):
    dir = os.path.splitext(file_paht)[0] + '_files'
    if not os.path.isdir(dir):
        os.mkdir(dir)
