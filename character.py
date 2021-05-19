"""
character.py
Author: Derek N
"""

import json


class Character:

    def __init__(self, name, level, health, strength, agility, intellect, wisdom, spirit):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.wisdom = wisdom
        self.spirit = spirit

    def get_stats(self):
        return (
        self.name,
        self.level,
        self.health,
        self.strength,
        self.agility,
        self.intellect,
        self.wisdom,
        self.spirit)

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health

    def get_strength(self):
        return self.strength

    def get_agility(self):
        return self.agility

    def get_intellect(self):
        return self.intellect

    def get_wisdom(self):
        return self.wisdom

    def get_spirit(self):
        return self.spirit


hero = Character("Luke", 1, 10, 3, 3, 3, 3, 3)

dict_hero = vars(hero)

with open("Save_file.txt", 'w') as save_file:
    save_file.write(json.dumps(dict_hero))



# file =open("Save_File", "w")
# print(vars(hero))
