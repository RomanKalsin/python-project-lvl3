#!/usr/bin/env python3


from bs4 import BeautifulSoup
from page_loader import create_file_name, get_file_ext
from page_loader import normalize_link, folder_create
from requests import get


def download_image(html_page_path):
    with open(html_page_path, 'r', encoding='utf-8') as html_text:
        soup = BeautifulSoup(html_text.read(), 'html.parser')
    img_folder_path = folder_create(html_page_path)
    for img in soup.find_all('img'):
        src = normalize_link(img['src'])
        split_src = get_file_ext(src)
        file_name = create_file_name(split_src[0]) + split_src[1]
        full_path = f'{img_folder_path}/{file_name}'
        with open(full_path, 'wb') as image:
            data = get(src)
            image.write(data.content)
