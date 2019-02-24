#!/usr/bin/env python
import pika
import random
import time
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

worker = 'Producer: '


def generate(channel_, key):
    number = random.randint(-100, 100)
    LOG.info(worker + 'sending %d' % number)
    channel_.basic_publish(exchange='',
                          routing_key=key,
                          body=str(number))


if __name__ == '__main__':
    time.sleep(5)

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('rabbitmq',
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    queue_name = 'random_generator'
    channel.queue_declare(queue=queue_name)

    num = 10
    LOG.info(worker + 'Starting producing %d random numbers.\n Precc Ctrl+C to stop.' % num)
    for i in range(num):
        delay = random.randint(0, 5)
        time.sleep(delay)
        generate(channel, queue_name)

    connection.close()
