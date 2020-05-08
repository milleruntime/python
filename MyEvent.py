import random
from termcolor import colored

event_types = ['Cosmic', colored('Alien', 'blue'), colored('Tragic', 'red'), 'Scientific']
short_names = ['Cos', colored('Ali', 'blue'), colored('Tra', 'red'), 'Sci']


class MyEvent:
    started = False
    number = 0
    name = ''
    short_name = ''

    def __init__(self, num):
        event_index = random.randint(0, len(event_types) - 1)
        self.name = event_types[event_index]
        self.number = get_power(self.name, num)
        self.short_name = short_names[event_index]

    @staticmethod
    def load(json_str):
        eve = MyEvent(1)
        eve.number = json_str['number']
        eve.name = json_str['name']
        return eve

    def start(self):
        started = True
        print("~~ " + self.name + " event occurred with power " + str(self.number) + " ~~")

    def __str__(self):
        return self.short_name + "(" + str(self.number) + ")"

    def __repr__(self):
        return self.__str__()

    def process(self):
        return self.number


def get_power(event, max_power):
    num = random.randint(1, max_power)
    # make 2 event (tragic) negative
    if event == event_types[2]:
        num = -num
    # make 1 event (alien) double
    if event == event_types[1]:
        num = num * 2
    return num
