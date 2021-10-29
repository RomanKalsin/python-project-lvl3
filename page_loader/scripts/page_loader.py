#!/usr/bin/env python3


from page_loader.arg_parser import arg_parser
from page_loader import download


def main():
    args = arg_parser()
    path_dir = args.output
    url = args.url
    print(download(url, path_dir))


if __name__ == "__main__":
    main()
