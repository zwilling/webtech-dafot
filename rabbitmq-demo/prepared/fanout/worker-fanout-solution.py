#!/usr/bin/env python

###########################
# WORKER
# Processes received tasks
###########################

import sys
import time


# callback for received messages
def callback(ch, method, properties, body):
    print " Received %r" % (body)
    # simulate processing all dots
    time.sleep( body.count('.') )
    print " Done"
    # send ack
    ch.basic_ack(delivery_tag = method.delivery_tag)

# receive message with RabbitMQ:

import pika # RabbitMQ client-lib

# connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# open channel
channel = connection.channel()

# create queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# bind queue to exchange
channel.queue_bind(exchange="exchange-name", queue=queue_name)

# fetch only one message
channel.basic_qos(prefetch_count=1)

# register for messages
channel.basic_consume(callback, queue=queue_name)

# start listening
print " Waiting for tasks"
channel.start_consuming()
