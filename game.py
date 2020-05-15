import random 

class Person:
    number = 0
    def __init__(self, number_comand):
        self.number = number_comand
        Person.number += 1
        self.number = Person.number


class Hero(Person):
    def __init__(self, number_comand):
        super(Hero, self).__init__(number_comand)
        self.level = 0
        self.comand_list = []

    def level_up(self):
        self.level += 1


    def add_soldier(self, soldier):
        self.comand_list.append(soldier)

    def len_comand(self):
        return len(self.comand_list)

class Soldier(Person):
    
    def going_for_a_hero(self, hero):
        return "Уникальный номер солдата : {}, Уникальный номер героя: {} ".format(self.number, hero.number)


hero1 = Hero(1)
hero2 = Hero(2)
count = 1

while count < 10:
    number_comand = random.randrange(1, 3)
    if number_comand == 1:
        hero1.add_soldier(Soldier(number_comand))
    else:
        hero2.add_soldier(Soldier(number_comand))
    
    count += 1
print(f'Comand-1: {hero1.len_comand()}, Comand-2: {hero2.len_comand()}')

if str(hero1.len_comand) > str(hero2.len_comand):
    hero1.level_up()
else:
    hero2.level_up()

print(hero1.comand_list[0].going_for_a_hero(hero1))

