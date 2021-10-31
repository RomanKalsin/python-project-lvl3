#!/usr/bin/env python3


from page_loader.arg_parser import arg_parser
from page_loader import download, folder_create


def main():
    args = arg_parser()
    path_dir = args.output
    url = args.url
    html_name = download(url, path_dir)
    folder_create(html_name)
    print(html_name)


if __name__ == "__main__":
    main()
