#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rdf022


lcm = rdf022.get_lcm()
lcm.messages = ('IP address', rdf022.get_ip())
lcm.refresh()
