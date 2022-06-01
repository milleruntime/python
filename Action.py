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

    def dock(self, ship_name="none"):
        do_event(self.mud)
        if len(self.mud.space) > 0:
            if len(self.mud.space) == 1:
                sel = 0
            else:
                sel = find_name(self.mud.space, ship_name)
            if sel < 0:
                sel = prompt_index(self.mud.space, "dock")
            s = self.mud.space[sel]
            self.mud.fuel += s.fuel
            s.dock_ship()
            print("BEEP BEEP Docking " + str(s))
            self.mud.ships.append(self.mud.space.pop(sel))
        else:
            print("No ships in space")

    def build(self, build_type="ship"):
        do_event(self.mud)
        if build_type == "ship":
            if self.mud.bmat > 9:
                ship_name = input("Enter the name of your new ship: ")
                new_ship = Ship(ship_name, 1)
                self.mud.ships.append(new_ship)
                self.mud.bmat -= 10
                print("Congratulations!!!  You successfully built the ship " + new_ship.name)
                display_ship()
            else:
                print("You don't have enough building material")
        else:
            print("You want to build a base?!?")

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

    # if no user input, process all, otherwise process number passed in
    def refine(self, num=0):
        if self.mud.ore > 0:
            if int(num) == 0:
                ore_to_proc = int(self.mud.ore)
            else:
                ore_to_proc = int(num)
            if 0 < ore_to_proc <= self.mud.ore:
                new_fuel = ore_to_proc * 2
                self.mud.fuel += new_fuel
                show_progress(2)
                print('Refined ' + str(ore_to_proc) + ' raw ore into ' + str(new_fuel) + ' fuel.')
        else:
            print("Not enough ore to process. Only have " + str(self.mud.ore))

    def go(self, num=1):
        do_event(self.mud)
        for n in range(0, int(num)):
            if len(self.mud.space) > 0:
                for i, s in enumerate(self.mud.space):
                    s.go(1)
                    print(str(s.name) + " flying through space")
            else:
                print("No ships in space.")
                return
            # get a new event
            eve = self.mud.new_event(10)
            assert isinstance(eve, MyEvent)
            print("Discovered " + eve.name() + " event!")
            show_progress(3)

    def launch(self, ship_name="none"):
        ship_index = find_name(self.mud.ships, ship_name)
        if ship_index < 0:
            if len(self.mud.ships) == 1:
                ship_index = 0
            elif len(self.mud.ships) > 1:
                ship_index = prompt_index(self.mud.ships, "space")
            else:
                print("No ships yet so sending probe...")
                eve = self.mud.new_event(10)
                print("Discovered " + eve.name() + " event!")
                show_progress(1)
                return
        f = prompt_number("How much fuel do you take? " + str(self.mud.fuel) + ": ", self.mud.fuel)
        if int(f) > self.mud.fuel:
            print("Sorry you have " + str(self.mud.fuel) + " fuel.")
            return
        self.mud.ships[ship_index].refuel(int(f))
        self.mud.fuel = self.mud.fuel - int(f)
        print("Wooooooooosssssshh sending " + str(self.mud.ships[ship_index].name) + " to space!!")
        sel_ship = self.mud.ships.pop(ship_index)
        self.mud.space.append(sel_ship)

    def show(self, arg="none"):
        if arg == "none":
            print("Ore: " + str(self.mud.ore))
            print("Bmat: " + str(self.mud.bmat))
            print("Fuel: " + str(self.mud.fuel))
            print("Bases: " + str(self.mud.bases))
            print("Ships: ")
            for i, val in enumerate(self.mud.ships):
                print(" " + str(val))
            print("Space: ")
            for i, val in enumerate(self.mud.space):
                print(" " + str(val))
        else:
            ship_name = arg
            ship_index = find_name(self.mud.ships, ship_name)
            if ship_index > -1:
                my_ship = self.mud.ships[ship_index]
                print(str(my_ship))
            else:
                print("Sorry don't know that ship.")


def prompt_index(my_list, action_name):
    p_num = 0
    for i, val in enumerate(my_list):
        print(i, val)
    while True:
        p = input("Which (##) would you like to " + action_name + "? ")
        try:
            p_num = int(p)
            break
        except ValueError:
            print("Please input a number.")
            continue
    return p_num


def prompt_number(message, default_value=0):
    p_num = default_value
    while True:
        try:
            p = input(message)
            # take the default value when none is entered
            if not p and not default_value==0:
                break
            p_num = int(p)
            break
        except ValueError:
            print("Please input a number.")
            continue
    return p_num


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


# look for the name in the list and return index
def find_name(search_list, search_name):
    for i, val in enumerate(search_list):
        if search_name == val.name:
            return i
    return -1


def display_ship():
    print("    +--->")
    print("=??|()  -\\")
    print("   | -   $$>")
    print("=??|()  -/")
    print("    +--->")
