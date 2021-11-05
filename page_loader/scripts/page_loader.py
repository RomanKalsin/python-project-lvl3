#!/usr/bin/env python3


from page_loader.arg_parser import arg_parser
from page_loader import download
from page_loader.download_image import download_image


def main():
    args = arg_parser()
    path_dir = args.output
    url = args.url
    html_name = download(url, path_dir)
    download_image(html_name)
    print(html_name)


if __name__ == "__main__":
    main()
