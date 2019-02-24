#!/usr/bin/env python
import pika
import time
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

worker = 'Consumer: '


def callback(ch, method, properties, body):
    LOG.info(worker + "received:\t%s" % body)


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

    channel.basic_consume(callback,
                          queue=queue_name)

    LOG.info(worker + 'Waiting for messages. To exit press Ctrl+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

    LOG.info(worker + 'closing connection...')
    connection.close()
