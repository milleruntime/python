import string
import os
import sys

class MyEvent:

	number = 0
	name = ''

	def __init__(self, num):
		self.number = num
		
	def start(self):
		print "Lets GOOOOO " + str(self.number)

