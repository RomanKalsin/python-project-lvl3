#!/usr/bin/env python3


from page_loader.arg_parser import arg_parser


def main():
    args = arg_parser()
    path_dir = args.output
    url = args.url
    print('path_dir: {}, url: {}'.format(path_dir, url))


if __name__ == "__main__":
    main()
