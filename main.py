#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

from Sim.person import Person

bob = Person()
bob.infection("Virus Presets/Covid.json")
bob.displayInfos()

