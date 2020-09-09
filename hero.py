from ability import Ability
from armor import Armor
from weapon import Weapon
import random


class Hero:

    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def defend(self, damage_amt):
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        net_damage = damage - self.defend(damage)
        self.current_health -= net_damage

    def is_alive(self):
        return self.current_health >= 0

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                hero1_ability = random.choice(self.abilities)
                hero2_ability = random.choice(opponent.abilities)
                self.take_damage(hero2_ability.attack())
                opponent.take_damage(hero1_ability.attack())

            if self.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} won!")
            else:
                self.add_death(1)
                opponent.add_kill(1)
                print(f"{opponent.name} won!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
