#!/usr/bin/env python

import argparse
import csv
import multiprocessing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='number of workers', default=10,
        dest='num_workers', type=int)
    args = parser.parse_args()

    workers = []
    for i in range(0, args.num_workers):
        worker = multiprocessing.Process(
            target=start_worker,
            args=(i,)
        )
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()


def start_worker(id):
    with open('output.txt'.format(id), 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['Output for worker {}.'.format(id)])


if __name__ == '__main__':
    main()
