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
            if len(Mud.space) == 1:
                print "BEEP BEEP Docking " + str(Mud.space[0])
                Mud.ships.append(Mud.space.pop(0))
                return
            if len(Mud.space) > 0:
                sel = prompt_index(Mud.space, "dock")
                Mud.ships.append(Mud.space.pop(sel))
                self.show()
            else:
                print "No ships in space"


	def build(self):
                if Mud.bmat > 9:
	            p = raw_input("Enter the name of your new ship: ")
                    Mud.ships.append(p)
                    Mud.bmat -= 10
                else:
                    print "You don't have enough building material"

        def proc(self):
            self.process()

	def process(self):
		if len(Mud.events) > 0:
			sel = prompt_index(Mud.events, "process")
	       		Mud.events[sel].start()
		 	Mud.ore += Mud.events.pop(sel).process()
			print 'You now have ' + str(Mud.ore) + ' ore.'
		else:
			print "No events to process"
		if Mud.ore >= 10:
			o = raw_input("Would you like to process 10 ore into building material? ")
			if o == 'y' or o == 'yes':
				print 'Processing raw ore into building material...'
				Mud.ore = Mud.ore - 10
				Mud.bmat += random.randint(1,3)

	def go(self):
                if len(Mud.ships) == 1:
                        print "Wooooooooosssssshh sending " + str(Mud.ships[0]) + " to space!!"
                        Mud.space.append(Mud.ships.pop(0))
        	if len(Mud.ships) > 1:
                	sel = prompt_index(Mud.ships, "space")
                        print "Wooooooooosssssshh sending " + str(Mud.ships[sel]) + " to space!!"
	                Mud.space.append(Mud.ships.pop(sel))
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
