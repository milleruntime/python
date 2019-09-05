import sys
import json
from MyEvent import MyEvent
from Action import Action

# globals
HELP_FILE = "help.txt"
SAVE_FILE = ".save"


class Mud:

    def __init__(self):
        pass

    ore = 0
    bmat = 0
    energy = 0
    bases = []
    ships = []
    space = []
    events = []

    def new_event(self, max_power):
        eve = MyEvent(max_power)
        self.events.append(eve)
        eve.start()


# returns the action class
def check_params(mud):
    """

    :param mud: Mud
    :return: Action
    """
    if len(sys.argv) != 2:
        with open(HELP_FILE, 'r') as fin:
            print(fin.read())
        sys.exit()
    else:
        a = sys.argv[1]
        if a == 'load':
            act = load_params(mud)
        else:
            act = Action(mud)
    return act


def show_intro():
    print("           ---[ Welcome to Space ]---")
    print("              |---    ~~~     ---| ")


def load_params(mud):
    """

    :type mud: Mud
    """
    bases = []
    ships = []
    space = []
    events = []
    with open(SAVE_FILE) as json_file:
        data = json.load(json_file)

    mud.ore = int(data['ore'])
    mud.bmat = int(data['bmat'])
    mud.energy = int(data['energy'])
    for b in data['bases']:
        bases.append(b)
    mud.bases = bases
    for s in data['ships']:
        ships.append(str(s))
    mud.ships = ships
    for s in data['space']:
        space.append(str(s))
    mud.space = space
    for e in data['events']:
        print("Event: name= " + str(e['name']) + " num= " + str(e['number']))
        eve = MyEvent.load(e['number'], e['name'])
        events.append(eve)
    mud.events = events
    return Action(mud)


def save(mud):
    data = {}
    data['ore'] = mud.ore
    data['bmat'] = mud.bmat
    data['energy'] = mud.energy
    data['bases'] = []
    for b in mud.bases:
        data['bases'].append({b})
    data['ships'] = []
    for s in mud.ships:
        data['ships'].append(s)
    data['space'] = []
    for s in mud.space:
        data['space'].append(s)
    data['events'] = []
    for e in mud.events:
        data['events'].append(e.__dict__)
    with open(SAVE_FILE, 'w') as outfile:
        json.dump(data, outfile)


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


def run(action):
    """

    :type action: Action
    """
    prompt = 'go(g) - build(b) - dock(d) - show(s) - proc(p): '
    u_input = input(prompt)
    while u_input != 'exit' and u_input != 'bye' and u_input != 'quit':
        try:
            u_input = get_abbrev(u_input)
            method = getattr(Action, u_input)
            method(action)
        except AttributeError:
            print("Bad Command try again")
        u_input = input(prompt)
    print("Seeeee ya")


# initialize stuff
m = Mud()
new_action = check_params(m)
show_intro()
run(new_action)
save(m)
