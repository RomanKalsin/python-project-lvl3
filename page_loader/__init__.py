#!/usr/bin/env python3


import requests
import re
import os


def download(url, path):
    file_name = create_file_name(url)
    file_name += ".html"
    file_name_with_path = os.path.join(path, file_name)
    with open(file_name_with_path, 'w', encoding='utf-8') as file:
        page = requests.get(url)
        file.write(page.text)
        file.close()
    return os.path.join(os.path.abspath(path), file_name)


def create_file_name(url):
    url_with_out_http = re.search(r'(?<=:\/\/).+', url)[0]
    file_name = re.sub(r'\W', '-', url_with_out_http)
    file_name = file_name[:-1] if file_name[-1] == "-" else file_name
    return file_name


def get_file_ext(url):
    path, ext = os.path.splitext(url)
    if ext:
        return path, ext
    else:
        return path, ''


def folder_create(file_paht):
    dir = os.path.splitext(file_paht)[0] + '_files'
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return dir


def normalize_link(link):
    if link[1] == '/':
        return f'https:{link}'
    elif link[0] == '/':
        return f'https:/{link}'
    else:
        return link


def replace_to_local_src():
    pass
