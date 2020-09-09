from ability import Ability
import random


class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)
