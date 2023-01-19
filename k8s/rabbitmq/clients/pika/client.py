#!/usr/local/bin/python3

import argparse
import pika

HOST = 'rabbitmq-example'
QUEUE = 'q'
USERNAME = 'admin'
PASSWORD = 'admin'

def main():
    commands= {
        'create-queue': create_queue,
        'delete-queue': delete_queue,
        'purge-queue': purge_queue,
        'usage': usage,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    args = parser.parse_args()

    commands.get(args.command, commands.get('usage'))()

def new_connection():
    credentials = pika.PlainCredentials(USERNAME, PASSWORD)
    parameters = pika.ConnectionParameters(host=HOST, credentials=credentials)
    return pika.BlockingConnection(parameters)

    credentials = pika.PlainCredentials(USERNAME, PASSWORD)
    return pika.BlockingConnection(
        host=HOST,
        credentials=credentials,
    )

def create_queue():
    conn = new_connection()
    channel = conn.channel()
    channel.queue_declare(queue=QUEUE)
    conn.close()

def delete_queue():
    conn = new_connection()
    channel = conn.channel()
    channel.queue_delete(QUEUE)
    conn.close()

def purge_queue():
    conn = new_connection()
    channel = conn.channel()
    channel.queue_purge(QUEUE)
    conn.close()

def usage():
    raise Exception('Unknown command')

if __name__ == '__main__':
    main()
