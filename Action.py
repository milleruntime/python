# Actions class
import random
import time
from Ship import Ship
from MyEvent import MyEvent

class Action:
    def __init__(self, mud):
        self.mud = mud

    def help(self):
        print("Available commands: ")
        for x in dir(self):
            if not str(x).startswith('__') and x != 'mud':
                print(x)

    def dock(self):
        do_event(self.mud)
        if len(self.mud.space) == 1:
            print("BEEP BEEP Docking " + str(self.mud.space[0]))
            self.mud.ships.append(self.mud.space.pop(0))
            return
        if len(self.mud.space) > 0:
            sel = prompt_index(self.mud.space, "dock")
            self.mud.ships.append(self.mud.space.pop(sel))
            self.show()
        else:
            print("No ships in space")

    def build(self):
        do_event(self.mud)
        if self.mud.bmat > 9:
            ship_name = input("Enter the name of your new ship: ")
            new_ship = Ship(ship_name, 1)
            self.mud.ships.append(new_ship)
            self.mud.bmat -= 10
            print("Congratulations!!!  You successfully built the ship " + new_ship.name)
            display_ship()
        else:
            print("You don't have enough building material")

    def proc(self, num=0):
        self.process(num)

    # if no user input, process all, otherwise process number passed in
    def process(self, num=0):
        do_event(self.mud)
        if self.mud.ore >= 10:
            if int(num) == 0:
                ore_to_proc = int(self.mud.ore)
            else:
                ore_to_proc = int(num)
            if 0 < ore_to_proc <= self.mud.ore:
                procs = ore_to_proc / 10
                new_bmat = 0
                for i in range(0, int(procs)):
                    self.mud.ore = self.mud.ore - 10
                    new_bmat += random.randint(1, 6)
                self.mud.bmat += new_bmat
                show_progress(2)
                print('Processed ' + str(procs * 10) + ' raw ore into ' + str(new_bmat) + ' building material.')
        else:
            print("Not enough ore to process. Only have " + str(self.mud.ore))

    def go(self, num=1):
        do_event(self.mud)
        for n in range(0, int(num)):
            if len(self.mud.space) > 0:
                for i, s in enumerate(self.mud.space):
                    print(str(s) + " flying through space")
            else:
                if len(self.mud.ships) == 1:
                    ship_index = 0
                elif len(self.mud.ships) > 1:
                    ship_index = prompt_index(self.mud.ships, "space")
                else:
                    print("No ships yet so sending probe...")
                    eve = self.mud.new_event(10)
                    print("Discovered " + eve.name + " event!")
                    show_progress(1)
                    continue
                print("Wooooooooosssssshh sending " + str(self.mud.ships[ship_index].name) + " to space!!")
                sel_ship = self.mud.ships.pop(ship_index)
                self.mud.space.append(sel_ship)
            # get a new event
            eve = self.mud.new_event(10)
            assert isinstance(eve, MyEvent)
            print("Discovered " + eve.name() + " event!")
            show_progress(3)

    def show(self, arg="none"):
        if arg == "none":
            print("Ore: " + str(self.mud.ore))
            print("Bmat: " + str(self.mud.bmat))
            print("Energy: " + str(self.mud.energy))
            print("Bases: " + str(self.mud.bases))
            print("Ships: ")
            for i, val in enumerate(self.mud.ships):
                print(" " + str(val))
            print("Space: ")
            for i, val in enumerate(self.mud.space):
                print(" " + str(val))
        elif arg in self.mud.ships:
            ship = Ship(arg, 1)
            print("Show ship... " + str(ship))
        elif arg in self.mud.bases:
            print("Showing base " + str(arg))


def prompt_index(my_list, action_name):
    for i, val in enumerate(my_list):
        print(i, val)
    p = input("Which (##) would you like to " + action_name + "? ")
    return int(p)


def do_event(mud):
    if len(mud.events) > 0:
        # index = prompt_index(self.mud.events, "process")
        # always process first one
        index = 0
        mud.events[index].start()
        mud.ore += mud.events.pop(index).process()
        if mud.ore < 0:
            mud.ore = 0
        print('You now have ' + str(mud.ore) + ' ore.')


def show_progress(seconds):
    for c in range(0, seconds):
        print(".", end='', flush=True)
        time.sleep(1)
    print()


def display_ship():
    print("    +--->")
    print("=??|()  -\\")
    print("   | -   $$>")
    print("=??|()  -/")
    print("    +--->")