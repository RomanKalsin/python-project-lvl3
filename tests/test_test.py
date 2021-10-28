#!/usr/bin/env python3
from page_loader import download
import os
import tempfile


def facke_client(url):
    pass


def test_download_create_file():
    with tempfile.TemporaryDirectory(dir='tests') as temp_path:
        download('https://ru.hexlet.io/pages/recommended-books', temp_path, facke_client)
        assert os.path.isfile(os.path.join(temp_path, 'ru-hexlet-io-pages-recommended-books.html'))


def test_download_output():
    with tempfile.TemporaryDirectory(dir='tests') as temp_path:
        ansver = os.path.join(temp_path, 'ru-hexlet-io-pages-recommended-books.html')
        assert download('https://ru.hexlet.io/pages/recommended-books', temp_path, facke_client) == ansver
