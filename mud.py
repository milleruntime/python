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
	events = []

	@staticmethod
	def newEvent(maxPower):
		eve = MyEvent(maxPower)
		Mud.events.append(eve)

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

def print_stats():
	print "Bases: " + str(Mud.bases)
	print "Ships: " + str(Mud.ships)
	print "Ore: " + str(Mud.ore)
	print "Bmat: " + str(Mud.bmat)
	print "Energy: " + str(Mud.energy)
	print "Events: " + str(Mud.events)

def display_timer():
	for i in range(0,5):
		print "."
		time.sleep(1)
	print "."
	
def get_event():
	Mud.newEvent(10)

def build():
	print "Called build"

def process():
	print "Called process"
	for i, val in enumerate(Mud.events):
		print(i, val)
	p = raw_input("What event(##) would you like to process? ")
	sel = int(p)
	Mud.events[sel].start()
	display_timer()
	Mud.ore += Mud.events[sel].process()
	del Mud.events[sel]
	print_stats()

def run():
	myInput = raw_input("Dude enter something (go, build, process, show): ")
	while myInput != 'exit' and myInput != 'bye' and myInput != 'quit':
		if myInput == 'process' or myInput == 'p':
			process()
		if myInput == 'show' or myInput == 's':
			print_stats()
		if myInput == 'build' or myInput == 'b':
			build()
		if myInput == 'go' or myInput == 'g':
			get_event()
		myInput = raw_input("Dude enter something (go, build, process, show): ")
	print "Seeeee ya"

# initialize stuff
check_params()
load_params()
run()
