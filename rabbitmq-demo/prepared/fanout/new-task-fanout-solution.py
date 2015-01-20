#!/usr/bin/env python

#####################################
# PRODUCER
# Creates new tasks for the workers
#####################################

import sys


# read message from argument
message = ' '.join(sys.argv[1:]) or "Hello World!"


# send message with RabbitMQ:

import pika # RabbitMQ client-lib

# connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# open channel
channel = connection.channel()

# create exchange
channel.exchange_declare(exchange="exchange-name", type="fanout")

# send
channel.basic_publish(exchange="exchange-name", routing_key="", body=message)
print " Sent %r" % (message)
