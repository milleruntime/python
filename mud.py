import string
import os
import sys
import random
import time
from MyEvent import MyEvent

class Mud:
	ore = 0
	bmat = 0
	energy = 0
	bases = []
	ships = []
	space = []
	events = []

	@staticmethod
	def newEvent(maxPower):
		eve = MyEvent(maxPower)
		Mud.events.append(eve)
		eve.start()

class Actions:
	def dock(self):
        	print "called dock"    

	def build(self):
	        print "Called build"

	def process(self):
		if len(Mud.events) > 0:
			sel = prompt_index(Mud.events, "process")
	       		Mud.events[sel].start()
		 	Mud.ore += Mud.events.pop(sel).process()
			print 'You now have ' + str(Mud.ore) + ' ore.'
			if Mud.ore >= 10:
				o = raw_input("Would you like to process 10 ore into building material? ")
				if o == 'y' or o == 'yes':
					print 'Processing raw ore into building material...'
					Mud.ore = Mud.ore - 10
					Mud.bmat += random.randint(1,3)
		else:
			print "No events to process"
		self.show()

	def go(self):
        	if len(Mud.ships) > 0:
                	sel = prompt_index(Mud.ships, "space")
	                Mud.space.append(Mud.ships.pop(sel))
			self.show()
	        if random.randint(1,3) == 3:
        	        print "A space event is occurring!!"
                	Mud.newEvent(10)
        	else:
                	print "Nothing interesting happening"

	def show(self):
		print "Bases: " + str(Mud.bases)
		print "Ships: " + str(Mud.ships)
		print "Ore: " + str(Mud.ore)
		print "Bmat: " + str(Mud.bmat)
		print "Energy: " + str(Mud.energy)
		print "Events: " + str(Mud.events)
		print "Space: " + str(Mud.space)

def check_params():
	if len(sys.argv) < 5:
		print "Usage: " + str(sys.argv[0]) + " <ore> <energy> <base1-base2> <ship1-ship2>"
		sys.exit()
	return

def load_params():
	Mud.ore = int(sys.argv[1])
	Mud.energy = int(sys.argv[2])
	basestr = str(sys.argv[3])
	Mud.bases = basestr.split("-")
	shipstr = str(sys.argv[4])
	Mud.ships = shipstr.split("-")


def display_timer():
	for i in range(0,5):
		print "."
		time.sleep(1)
	print "."

def prompt_index(mylist, actionName):
	for i, val in enumerate(mylist):
		print(i, val)
	p = raw_input("Which (##) would you like to " + actionName + "? ")
	return int(p)
	

def run():
	prompt = "Dude enter something (go, build, dock, show): "
	myInput = raw_input(prompt)
	while myInput != 'exit' and myInput != 'bye' and myInput != 'quit':
		method = getattr(Actions, myInput)
		method(Actions())
		myInput = raw_input(prompt)
	print "Seeeee ya"

# initialize stuff
check_params()
load_params()
run()
