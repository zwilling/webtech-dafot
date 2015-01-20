#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)

channel.queue_bind(exchange='logs',
                   queue=result.method.queue)
queue_name = result.method.queue


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue=queue_name)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
