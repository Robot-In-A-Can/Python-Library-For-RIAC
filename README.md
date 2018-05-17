# evelabs Python Library

This is a library to control your evelabs from the Python programming language. It is a modification of Ben Pirt's library for the Mirobot. It has a simple API which mirrors the basic movements that evelabs can do. Here's a sample program that runs through the API:

    from evelabs import evelabs
    
    # Connect to evelabs
    evelabs = evelabs()
    evelabs.autoConnect()

    # Put the pen down
    evelabs.pendown()

    # Move forward 100mm
    evelabs.forward(100)

    # Move back 100mm
    evelabs.back(100)

    # Turn left 45 degrees
    evelabs.left(45)

    # Turn right 45 degrees
    evelabs.right(45)

    # Lift the pen up
    evelabs.penup()

    # Disconnect from evelabs
    evelabs.disconnect()

    # Reads From Analog Pin # 0
    analogInput(0):

    # Digital read on pin 16
    digitalInput(16):

    # Turn GPIO 10 on
    gpioOn(10):

    # Turn GPIO 10 off
    gpioOff(self, pin):

There are a few different ways of connecting to evelabs:

Specify the IP address (192.168.4.1) or hostname manually:

    evelabs = evelabs('local.evelabs.io')

You can also use the discovery mechanism to auto connect which saves having to figure out where it is on your network. If you only have one evelabs on your network, you can just do this:

    evelabs = evelabs()
    evelabs.autoConnect()

If you have more than one you can either specify the ID of the evelabs to connect to that one:

    evelabs = evelabs()
    evelabs.autoConnect('evelabs-abcd')

Or you can use the interactive mode to select which one to connect to:

    evelabs = evelabs()
    evelabs.autoConnect(interactive=True)
    
    >>> Select the evelabs to connect to:
    >>>   1: evelabs-ad43
    >>>   2: evelabs-ea51
    >>> Select a number:
