# Create a Car class that has the following characteristics:
#    It has a gas_level attribute.
#    It has a constructor (__init__ method) that takes a float representing the initial gas level
#    and sets the gas level of the car to this value.
#    It has an add_gas method that takes a single float value and adds this amount to the current
#    value of the gas_level attribute.
#    It has a fill_up method that sets the car’s gas level up to 13.0 by adding the amount of gas
#    necessary to reach this level. It will return a float of the amount of gas that had to be added to the car to get the gas level up to 13.0. However, if the car’s gas level was greater than or equal to 13.0 to begin with, then it doesn’t need to add anything and it simply returns a 0.

import math


class Car:

    def __init__(self, i):
        self.gas_level = float(i)

    def add_gas(self):
        gas_need = 13 - self.gas_level
        self.gas_level = self.gas_level + gas_need
        return gas_need

    def fill_up(self):
        if self.gas_level >= 13:
            return 0
        else:
            fill = self.add_gas()
            if fill - math.floor(fill) == 0.0:
                return int(fill)
            else:
                return ('%.1f' % (fill))

    def __str__(self):
        return ('Gas level is at ' + str(self.gas_level))


def main():
    # print(Car(10).fill_up())
    # print(Car(20).fill_up())
    # print(Car(5.5).fill_up())
    print(Car(12.5).fill_up())
    # print(Car(13).fill_up())


if __name__ == '__main__':
    main()
