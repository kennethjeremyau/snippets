#!/usr/bin/env python

import argparse

def main():
    description = 'argparse example'
    parser = argparse.ArgumentParser(description=description)
    # result is stored in 'args.arg'.
    parser.add_argument('-a', '--arg', help='an argument', required=True)
    # boolean result is stored in 'args.flag'.
    parser.add_argument('--flag', action='store_true', help='a flag')
    # integer result is stored in 'args.integer'.
    parser.add_argument('--int', default=0, dest='integer', type=int)
    # result is stored in 'args.choice'.
    parser.add_argument('--choice', choices=['one', 'two'], default='one')
    args = parser.parse_args()

if __name__ == '__main__':
    main()
