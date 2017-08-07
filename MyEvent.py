import string
import os
import sys
import random


class MyEvent:
	event_types = ['Cosmic','Alien','Apocolyptic', 'Discovery']

	number = 0
	name = ''

	def __init__(self, num):
		self.number = random.randint(1,num)
		
	def start(self):
		self.name = MyEvent.event_types[random.randint(0,len(MyEvent.event_types)-1)]
		print self.name + " event occured with power " + str(self.number)

	def __str__(self):
    		return self.name +" "+ str(self.number)

	def __repr__(self):
    		return self.__str__()
