#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

from src.person import Person

bob = Person()
bob.infection(0.04, "Virus Presets/Covid.json")
bob.displayInfos()

