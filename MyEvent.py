import random
from termcolor import colored


class MyEvent:
    event_types = ['Cosmic', colored('Alien', 'blue'), colored('Tragic', 'red'), 'Scientific']

    def __init__(self, max_pow, index=None, number=None):
        if index is None:
            self.event_index = random.randint(0, len(self.event_types) - 1)
            self.max_power = max_pow
            self.power = MyEvent.get_power(self.event_index, max_pow)
        else:
            self.event_index = index
            self.max_power = max_pow
            self.power = number

    @staticmethod
    def get_power(index, max_power):
        num = random.randint(1, max_power)
        # make 2 event (tragic) negative
        if index == 2:
            num = -num
        # make 1 event (alien) double
        if index == 1:
            num = num * 2
        return num

    @staticmethod
    def load(json_str):
        index = json_str['event_index']
        max_pow = json_str['max_power']
        number = json_str['power']
        eve = MyEvent(max_pow, index, number)
        return eve

    def name(self):
        return self.event_types[self.event_index]

    def start(self):
        print("~~ " + self.name() + " event occurred with power " + str(self.power) + " ~~")

    def __str__(self):
        return self.name() + "(" + str(self.power) + ")"

    def __repr__(self):
        return self.__str__()

    def process(self):
        return self.power
