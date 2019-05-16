import random

from notes.OOP.rpg.attributes import *
from notes.OOP.rpg.characters import Character

class Guru(Agile, Wisdom, Character):
    def skills(self):
        return self.patience and bool(random.randint(0, 1))

class Student(Level_head, Patience, Pure_heart):
    def skills(self):
        return self.level_head and bool(random.randint(0, 1))