import string
import os
import sys
import random
import time
from MyEvent import MyEvent

ore = 0
bmat = 0
energy = 0
bases = []
ships = []

def check_params():
	if len(sys.argv) < 5:
		print "Usage: " + str(sys.argv[0]) + " <ore> <energy> <base1-base2> <ship1-ship2>"
		sys.exit()
	return

def load_params():
	global bases, ships, ore, energy, bmat
	ore = int(sys.argv[1])
	energy = int(sys.argv[2])
	basestr = str(sys.argv[3])
	bases = basestr.split("-")
	shipstr = str(sys.argv[4])
	ships = shipstr.split("-")

def print_stats():
	global bases, ships, ore, energy, bmat
	print "Bases: " + str(bases)
	print "Ships: " + str(ships)
	print "Ore: " + str(ore)
	print "Bmat: " + str(bmat)
	print "Energy: " + str(energy)
	
def get_event():
	global bases, ships, ore, energy, bmat
	eve = MyEvent(1)
	eve.start()

def build():
	print "Called build"

def process():	
	print "Called process"

def run():
	global bases, ships, ore, energy, bmat
	global myInput
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
