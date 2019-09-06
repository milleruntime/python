# Actions class
import random
import time


class Action:
    mud = []

    def __init__(self, mud):
        self.mud = mud

    def help(self):
        print("Available commands: ")
        for x in dir(self):
            if not str(x).startswith('__') and x != 'mud':
                print(x)

    def dock(self):
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
        if self.mud.bmat > 9:
            p = input("Enter the name of your new ship: ")
            self.mud.ships.append(p)
            self.mud.bmat -= 10
        else:
            print("You don't have enough building material")

    def proc(self, num=1):
        self.process(num)

    def process(self, num=1):
        for n in range(0, int(num)):
            if len(self.mud.events) > 0:
                # index = prompt_index(self.mud.events, "process")
                # always process first one
                index = 0
                self.mud.events[index].start()
                self.mud.ore += self.mud.events.pop(index).process()
                print('You now have ' + str(self.mud.ore) + ' ore.')
            else:
                print("No events to process")
            if self.mud.ore >= 10:
                o = input("Enter # of ore to process into building material (or Enter for ALL): ")
                if not o:
                    ore_to_proc = int(self.mud.ore)
                else:
                    ore_to_proc = int(o)
                if 0 < ore_to_proc <= self.mud.ore:
                    procs = ore_to_proc / 10
                    new_bmat = 0
                    for i in range(0, int(procs)):
                        self.mud.ore = self.mud.ore - 10
                        new_bmat += random.randint(1, 6)
                    self.mud.bmat += new_bmat
                    show_progress(2)
                    print('Processed ' + str(procs * 10) + ' raw ore into ' + str(new_bmat) + ' building material.')

    def go(self, num=1):
        for n in range(0, int(num)):
            if len(self.mud.ships) == 1:
                print("Wooooooooosssssshh sending " + str(self.mud.ships[0]) + " to space!!")
                self.mud.space.append(self.mud.ships.pop(0))
            if len(self.mud.ships) > 1:
                sel = prompt_index(self.mud.ships, "space")
                print("Wooooooooosssssshh sending " + str(self.mud.ships[sel]) + " to space!!")
                self.mud.space.append(self.mud.ships.pop(sel))
            if random.randint(1, 6) > 2:
                eve = self.mud.new_event(10)
                print("Discovered " + eve.name + " event!")
            else:
                print("Nothing interesting happening")
            show_progress(3)

    def show(self):
        print("Bases: " + str(self.mud.bases))
        print("Ships: " + str(self.mud.ships))
        print("Ore: " + str(self.mud.ore))
        print("Bmat: " + str(self.mud.bmat))
        print("Energy: " + str(self.mud.energy))
        print("Events: " + str(self.mud.events))
        print("Space: " + str(self.mud.space))


def prompt_index(my_list, action_name):
    for i, val in enumerate(my_list):
        print(i, val)
    p = input("Which (##) would you like to " + action_name + "? ")
    return int(p)


def show_progress(seconds):
    for c in range(0, seconds):
        print(".", end='', flush=True)
        time.sleep(1)
    print()
