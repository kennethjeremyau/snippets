#!/usr/bin/env python

import argparse

def main():
    description = 'argparse example'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-a', '--a', help='an argument', required=True)
    parser.parse_args()

if __name__ == '__main__':
    main()
