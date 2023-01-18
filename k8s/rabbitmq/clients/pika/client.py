#!/usr/local/bin/python3

import argparse
import pika

def main():
    commands= {
        'create-queue': create_queue,
        'usage': usage,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    args = parser.parse_args()

    commands.get(args.command, commands.get('usage'))()

def create_queue():
    print('function1')

def usage():
    raise Exception('Unknown command')

if __name__ == '__main__':
    main()
