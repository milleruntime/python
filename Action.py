# Actions class
import random


class Action:
    mud = []

    def __init__(self, mud):
        self.mud = mud

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

    def proc(self):
        self.process()

    def process(self):
        if len(self.mud.events) > 0:
            sel = prompt_index(self.mud.events, "process")
            self.mud.events[sel].start()
            self.mud.ore += self.mud.events.pop(sel).process()
            print('You now have ' + str(self.mud.ore) + ' ore.')
        else:
            print("No events to process")
        if self.mud.ore >= 10:
            o = input("How much ore would you like to process into building material? ")
            if 0 < int(o) <= self.mud.ore:
                procs = int(o) / 10
                print('Processing ' + str(procs * 10) + ' raw ore into building material...')
                for i in range(0, int(procs)):
                    self.mud.ore = self.mud.ore - 10
                    self.mud.bmat += random.randint(1, 3)

    def go(self):
        if len(self.mud.ships) == 1:
            print("Wooooooooosssssshh sending " + str(self.mud.ships[0]) + " to space!!")
            self.mud.space.append(self.mud.ships.pop(0))
        if len(self.mud.ships) > 1:
            sel = prompt_index(self.mud.ships, "space")
            print("Wooooooooosssssshh sending " + str(self.mud.ships[sel]) + " to space!!")
            self.mud.space.append(self.mud.ships.pop(sel))
        if random.randint(1, 3) == 3:
            print("A space event is occurring!!")
            self.mud.new_event(10)
        else:
            print("Nothing interesting happening")

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