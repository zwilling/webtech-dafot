#!/usr/bin/env python

###########
# Consumer
###########

import sys
import time


# callback for received messages
def callback(ch, method, properties, body):
    print " Received %r" % (body,)

# TODO: receive message
