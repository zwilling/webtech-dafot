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

# receive message with RabbitMQ:

import pika # RabbitMQ client-lib

# connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# open channel
channel = connection.channel()

# create queue
channel.queue_declare(queue="queue-name")

# register for messages
channel.basic_consume(callback, queue="queue-name", no_ack=True)

# start listening
print " Waiting for tasks"
channel.start_consuming()
