import sys
import json
from MyEvent import MyEvent
from Ship import Ship
from Action import Action
from termcolor import colored, cprint

# globals
HELP_FILE = "help.txt"
SAVE_FILE = ".save"


class Mud:

    def __init__(self):
        self.ore = 0
        self.met = 0
        self.gas = 0
        self.fuel = 0
        self.cry = 0
        self.bases = []
        self.ships = []
        self.space = []
        self.events = []

    def new_event(self, max_power):
        eve = MyEvent(max_power)
        self.events.append(eve)
        return eve


# returns the action class
# no longer used
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
    print(colored("      ---[ Welcome to Space Fleet ]---", "green"))
    print(colored("         |---       ~~~        ---| ", "green"))


def load_params(mud):
    """

    :type mud: Mud
    """
    bases = []
    ships = []
    space = []
    events = []
    try:
        with open(SAVE_FILE) as json_file:
            data = json.load(json_file)
    except OSError:
        print("Starting a new game!  Enter 'help' for commands.")
        return Action(mud)
    mud.ore = int(data['ore'])
    mud.met = int(data['met'])
    mud.cry = int(data['cry'])
    mud.gas = int(data['gas'])
    mud.fuel = int(data['fuel'])
    for b in data['bases']:
        bases.append(b)
    mud.bases = bases
    for s in data['ships']:
        ships.append(Ship.load(s))
    mud.ships = ships
    for s in data['space']:
        space.append(Ship.load(s))
    mud.space = space
    for e in data['events']:
        eve = MyEvent.load(e)
        events.append(eve)
    mud.events = events
    return Action(mud)


def save(mud):
    data = {'ore': mud.ore, 'met': mud.met, 'cry': mud.cry, 'gas': mud.gas, 'fuel': mud.fuel, 'bases': []}
    for b in mud.bases:
        data['bases'].append({b})
    data['ships'] = []
    for s in mud.ships:
        data['ships'].append(s.__dict__)
    data['space'] = []
    for s in mud.space:
        data['space'].append(s.__dict__)
    data['events'] = []
    for e in mud.events:
        data['events'].append(e.__dict__)
    with open(SAVE_FILE, 'w') as outfile:
        json.dump(data, outfile)


# split user input on space and call method on action object
def exec_command(user_input, act_obj):
    s = user_input.split(" ")
    command = s[0]
    method = getattr(Action, command)
    if len(s) > 1:
        arg = s[1]
        method(act_obj, arg)
    else:
        method(act_obj)


def run(action):
    """

    :type action: Action
    """
    prompt = 'Enter command: '
    u_input = input(prompt)
    while u_input != 'exit' and u_input != 'bye' and u_input != 'quit':
        try:
            exec_command(u_input, action)
        except AttributeError:
            print("Bad Command try again")
        u_input = input(prompt)
    print("Seeeee ya")


# initialize stuff
m = Mud()
new_action = load_params(m)
show_intro()
run(new_action)
save(m)
