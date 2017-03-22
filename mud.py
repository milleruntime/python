import string
import os
import sys
import random
import time

ore = 0
bmat = 0
energy = 0
bases = []
ships = []

def check_params():
	if len(sys.argv) < 5:
		print "Usage: " + str(sys.argv[0] + " <ore> <energy> <base1-base2> <ship1-ship2>"
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
	
def get_event(number)
	global bases, ships, ore, energy, bmat
	if number == 1:
		print "Stuff happens"

		

def build():

def process():	

def run()
	my_input = raw_input("Dude enter something (go, build, process, show): ")
	while myInput != 'exit' and myInput != 'bye' and myInput != 'quit':
		if myInput == 'process' or myInput == 'p':
			process()
		my_input = raw_input("Dude enter something (go, build, process, show): ")
	print "Seeeee ya"

# initialize stuff
check_params()
load_params()
run()
