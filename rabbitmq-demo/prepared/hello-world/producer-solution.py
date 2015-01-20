#!/usr/bin/env python

###########
# PRODUCER
###########

import sys


# read message from argument
message = ' '.join(sys.argv[1:]) or "Hello World!"


# send message with RabbitMQ:

import pika # RabbitMQ client-lib

# connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# open channel
channel = connection.channel()

# create queue
channel.queue_declare(queue="queue-name")

# send
channel.basic_publish(exchange="", routing_key="queue-name", body=message)
print " Sent %r" % (message)


