#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Sim.population import Person

personnes = []

i = 0
while i < 10:
	personnes.append(Person())
	personnes[i].displayInfos()
	print()
	i += 1
