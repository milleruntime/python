import sys
import random
import json
from MyEvent import MyEvent

# globals
HELP_FILE = "help.txt"
SAVE_FILE = ".save"


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
            print("BEEP BEEP Docking " + str(Mud.space[0]))
            Mud.ships.append(Mud.space.pop(0))
            return
        if len(Mud.space) > 0:
            sel = prompt_index(Mud.space, "dock")
            Mud.ships.append(Mud.space.pop(sel))
            self.show()
        else:
            print("No ships in space")

    def build(self):
        if Mud.bmat > 9:
            p = input("Enter the name of your new ship: ")
            Mud.ships.append(p)
            Mud.bmat -= 10
        else:
            print("You don't have enough building material")

    def proc(self):
        self.process()

    def process(self):
        if len(Mud.events) > 0:
            sel = prompt_index(Mud.events, "process")
            Mud.events[sel].start()
            Mud.ore += Mud.events.pop(sel).process()
            print('You now have ' + str(Mud.ore) + ' ore.')
        else:
            print("No events to process")
        if Mud.ore >= 10:
            o = input("How much ore would you like to process into building material? ")
            if 0 < int(o) <= Mud.ore:
                procs = int(o) / 10
                print('Processing ' + str(procs * 10) + ' raw ore into building material...')
                for i in range(0, int(procs)):
                    Mud.ore = Mud.ore - 10
                    Mud.bmat += random.randint(1, 3)

    def go(self):
        if len(Mud.ships) == 1:
            print("Wooooooooosssssshh sending " + str(Mud.ships[0]) + " to space!!")
            Mud.space.append(Mud.ships.pop(0))
        if len(Mud.ships) > 1:
            sel = prompt_index(Mud.ships, "space")
            print("Wooooooooosssssshh sending " + str(Mud.ships[sel]) + " to space!!")
            Mud.space.append(Mud.ships.pop(sel))
        if random.randint(1, 3) == 3:
            print("A space event is occurring!!")
            Mud.newEvent(10)
        else:
            print("Nothing interesting happening")

    def show(self):
        print("Bases: " + str(Mud.bases))
        print("Ships: " + str(Mud.ships))
        print("Ore: " + str(Mud.ore))
        print("Bmat: " + str(Mud.bmat))
        print("Energy: " + str(Mud.energy))
        print("Events: " + str(Mud.events))
        print("Space: " + str(Mud.space))


def check_params():
    if len(sys.argv) != 2:
        with open(HELP_FILE, 'r') as fin:
            print(fin.read())
        sys.exit()
    else:
        action = sys.argv[1]
        if action == 'load':
            load_params()
    return


def show_intro():
    print("           ---[ Welcome to Space ]---")
    print("              |---    ~~~     ---| ")


def load_params():
    bases = []
    ships = []
    space = []
    events = []
    with open(SAVE_FILE) as json_file:
        data = json.load(json_file)

    Mud.ore = int(data['ore'])
    Mud.bmat = int(data['bmat'])
    Mud.energy = int(data['energy'])
    for b in data['bases']:
        bases.append(b)
    Mud.bases = bases
    for s in data['ships']:
        ships.append(str(s))
    Mud.ships = ships
    for s in data['space']:
        space.append(str(s))
    Mud.space = space
    for e in data['events']:
        print("Event: name= " + str(e['name']) + " num= " + str(e['number']))
        eve = MyEvent.load(e['number'], e['name'])
        events.append(eve)
    Mud.events = events


def save():
    data = {}
    data['ore'] = Mud.ore
    data['bmat'] = Mud.bmat
    data['energy'] = Mud.energy
    data['bases'] = []
    for b in Mud.bases:
        data['bases'].append({b})
    data['ships'] = []
    for s in Mud.ships:
        data['ships'].append(s)
    data['space'] = []
    for s in Mud.space:
        data['space'].append(s)
    data['events'] = []
    for e in Mud.events:
        data['events'].append(e.__dict__)
    with open(SAVE_FILE, 'w') as outfile:
        json.dump(data, outfile)


def prompt_index(mylist, actionName):
    for i, val in enumerate(mylist):
        print(i, val)
    p = input("Which (##) would you like to " + actionName + "? ")
    return int(p)


def get_abbrev(myinput):
    if myinput.startswith('g'):
        return 'go'
    if myinput.startswith('b'):
        return 'build'
    if myinput.startswith('d'):
        return 'dock'
    if myinput.startswith('s'):
        return 'show'
    if myinput.startswith('p'):
        return 'proc'
    return myinput


def run():
    prompt = 'go(g) - build(b) - dock(d) - show(s) - proc(p): '
    u_input = input(prompt)
    while u_input != 'exit' and u_input != 'bye' and u_input != 'quit':
        try:
            u_input = get_abbrev(u_input)
            method = getattr(Actions, u_input)
            method(Actions())
        except AttributeError:
            print("Bad Command try again")
        u_input = input(prompt)
    print("Seeeee ya")


# initialize stuff
check_params()
show_intro()
run()
save()
