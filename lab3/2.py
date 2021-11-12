from json import load
from datetime import date


class Pizza:
    def __init__(self):
        self.name = date.today().weekday()  # chek today weekday
        with open("2_1.json", "r") as f: # json file with recipes of pizza
            self.ingredient = load(f)[self.name]

    @property
    def name(self):
        return self.__name

    @property
    def ingredient(self):
        return self.__ingredient

    @name.setter
    def name(self, name):
        if not isinstance(name, int):
            raise TypeError("Bad enter")
        self.__name = name

    @ingredient.setter
    def ingredient(self, ingredient):
        if not isinstance(ingredient, dict):
            raise TypeError("Bad enter")
        self.__ingredient = ingredient

    def __str__(self):
        with open("2_2.json", "r") as f: # json file with name of pizza
            k = '|  ' + load(f)[self.name] + '\n'
        k += '-' * 25 + '\n'
        with open("2_3.json", "r") as f: # json file with ingredients
            t = load(f)
        print()
        for i in self.ingredient:
            k += '|  ' + t[int(i)] + '  -  ' + str(self.ingredient[i]) + '\n'
        return k

    def add_ingredient(self, ing, number):
        if not isinstance(ing, str) or not isinstance(number, int):
            raise TypeError("Bad enter")
        with open("2_3.json", "r") as f: # json file with ingredients
            if not ing.isdigit() or not (0 <= int(ing) < len(load(f))):  # check for an enter ingredient is in list
                raise ValueError("Not number")
        if self.ingredient.get(ing):
            self.ingredient.update({ing: number + self.ingredient.get(ing)})  # update recipe of pizza for client
        else:
            self.ingredient.update({ing: number})


def show_ingredients():
    with open("2_3.json", "r") as f:     # json file with ingredients
        t = load(f)
    k = '|  Ingredients\n' + '-' * 25 + ' \n'
    for i in range(len(t)):
        k += str(i) + '  -  ' + t[i] + ' \n'
    return k


try:
    p = Pizza()

    while True:
        print('Your pizza:\n' + str(p))
        t = input('Want to add something? If no - enter 0\n')
        if t == '0':
            break
        else:
            print(show_ingredients())
            p.add_ingredient(input('What did you want?\n'), int(input('How much?\n')))

except (TypeError, ValueError) as er:
    print('error\n' + str(er))
