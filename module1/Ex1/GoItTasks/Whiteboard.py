"""
Почнемо з простого завдання - поєдинку один на один. Вам потрібно створити клас Warrior, 
екземпляри якого матимуть 2 параметри – health (дорівнює 50 балам) і attack (дорівнює 5 балам), 
а також 1 властивість – is_alive, яка може бути True (якщо здоров’я воїна > 0). ) або False (в іншому випадку). 
Крім того, ви повинні створити другий тип одиниць – Knight, який має бути підкласом Warrior, але мати підвищену атаку – 7. 
Також вам потрібно створити функцію fight(), яка ініціюватиме двобій між 2 бійцями та визначатиме найсильніший з них. 
Поєдинок відбувається за таким принципом:
Кожного ходу перший воїн буде вдаряти по другому, і цей другий втрачатиме своє здоров'я в тій самій величині, 
що і атака першого воїна. 
Після цього, якщо він ще живий, другий воїн зробить те ж саме з першим.
Поєдинок закінчується смертю одного з них. 
Якщо перший воїн ще живий (і, отже, іншого більше немає), функція має повернути True, False в іншому випадку.
"""
from collections import UserList

class Warrior:
    def __init__(self, health=50, attack=5) -> None:
        self.health = health
        self.attack = attack
    
    @property
    def is_alive(self):
        return self.health > 0 


class Knight(Warrior):
    def __init__(self, health=50, attack=7) -> None:
        super().__init__(health=health, attack=attack)


class Army(UserList):
    def add_units(self, warriors_type:Warrior, amount:int):
        for _ in range(amount):
            self.data.append(warriors_type()) # создаём 20 экземпляров класса


    @property
    def is_exist(self):
        return bool(self.data) > 0 


class Battle:

    def fight(self, first_army:Army, second_army:Army):
        while first_army.is_exist and second_army.is_exist:
            if fight(first_army[0], second_army[0]):
                second_army.pop(0)
            else:
                first_army.pop(0)
        return first_army.is_exist



        




def fight(fighter1:Warrior, fighter2:Warrior):
    while fighter1.is_alive and fighter2.is_alive:
        fighter2.health -= fighter1.attack
        if fighter2.is_alive:
            fighter1.health -= fighter2.attack
    return fighter1.is_alive



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    battle.fight(army_1, army_2)
#battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")