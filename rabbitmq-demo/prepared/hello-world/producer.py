#!/usr/bin/env python

###########
# PRODUCER
###########

import sys


# read message from argument
message = ' '.join(sys.argv[1:]) or "Hello World!"
print " Read %r" % (message)

# TODO: send message
