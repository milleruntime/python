# ship class


class Ship:
    def __init__(self, p_name, p_size):
        self.name = p_name
        self.shields = 100
        self.fuel = 0
        self.size = p_size
        self.capacity = p_size * 10
        self.cargo = 0

    def __str__(self):
        return self.name + "(" + str(self.size) + "): " + str(self.shields) + "%" + \
               " cargo: " + str(self.cargo) + "/" + str(self.capacity) + \
               " fuel: " + str(self.fuel)

    def refuel(self, f):
        self.fuel = f

    def go(self, distance):
        if self.fuel < distance:
            print("Not enough fuel!")
        else:
            self.fuel = self.fuel - distance
            print(str(self.name) + " flying through space")

    def dock_ship(self):
        self.fuel = 0

    @staticmethod
    def load(json_str):
        s = Ship(None, 0)
        s.name = json_str['name']
        s.shields = json_str['shields']
        s.fuel = json_str['fuel']
        s.size = json_str['size']
        s.capacity = json_str['capacity']
        s.cargo = json_str['cargo']
        return s
