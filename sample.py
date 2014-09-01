#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rdf022


lcm = rdf022.get_lcm()
lcm.messages = ('IP address', rdf022.get_ip())
lcm.refresh()

#raw_input('Press enter to continue')

import time

def sparkle():
    while True:
        for i in range(lcm.brightness_depth):
            lcm.decrease_brightness()
            time.sleep(0.1)
        for i in range(lcm.brightness_depth):
            lcm.increase_brightness()
            time.sleep(0.1)

import threading
threading.Thread(target=sparkle).start()
