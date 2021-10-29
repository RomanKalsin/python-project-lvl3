#!/usr/bin/env python3
from page_loader import download
import os
import tempfile
import requests_mock


def open_fixtures(path):
    with open(path) as file:
        return file.read


def fake_client(data):
    return data


def test_download_create_file(requests_mock):
    with tempfile.TemporaryDirectory(dir='tests') as temp_path:
        requests_mock.get('https://ru.hexlet.io/pages/recommended-books', text="test")
        download('https://ru.hexlet.io/pages/recommended-books', temp_path)
        assert os.path.isfile(os.path.join(temp_path, 'ru-hexlet-io-pages-recommended-books.html'))


def test_download_output(requests_mock):
    with tempfile.TemporaryDirectory(dir='tests') as temp_path:
        requests_mock.get('https://ru.hexlet.io/pages/recommended-books', text="test")
        ansver = os.path.join(os.getcwd(), 'ru-hexlet-io-pages-recommended-books.html')
        assert download('https://ru.hexlet.io/pages/recommended-books', temp_path) == ansver
