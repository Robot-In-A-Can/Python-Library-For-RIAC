#!/usr/bin/env python

from evelabs import evelabs
import sys, time

# this is an optional error handler for the evelabs.
def on_error(x, msg, timeout, bot):
  print('ERROR:')
  print(x)
  print(msg)
  print(timeout)
  print(bot)
  sys.exit()
  evelabs.disconnect()

# choose the evelabs to connect to
if len(sys.argv) > 1:
  host = sys.argv[1]
else:
  host = '192.168.4.1'

# connect to evelabs - there are a few different ways of doing this

# Use the host we specified on the command line
#evelabs = evelabs(host, debug=True)

# Create a evelabs instance
evelabs = evelabs(debug=True)
# Autoconnect to a evelabs on our network (there can be only one)
evelabs.autoConnect()

# Get a menu so we can select which evelabs to connect to
#evelabs.autoConnect(interactive=True)

# Specify the id of the evelabs we want to connect to
#evelabs.autoConnect(id='evelabs-abcd')

print("evelabs version: %s" % evelabs.version)

# set up error handling
evelabs.errorNotify(on_error)

evelabs.forward(100)
evelabs.right(90)
evelabs.back(100)
evelabs.penup()

while True:
  evelabs.gpioOn(10)
  sleep(1)
  evelabs.gpioOff(10)
  sleep(1)
