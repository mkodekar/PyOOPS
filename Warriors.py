"""
Bob vs builder 
Bob attacks builder and deals 9 damage
builder is down to 10 health
builder attack Bob and deals 7 damager
Bob is down with 7 health
Bob attacks sam and deals 19 damage
Builder is down with -9 health
Builder has died and Bo is victorious
Game over
"""

import random
import math


class Warrior:
    def __init__(self, name, health=0, attackpower=0, healthreduction=0):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.healthReduction = healthreduction

    def attack(self):
        attackpower = self.attackpower * (random.random() + .5)
        return attackpower

    def healthReduce(self):
        healthreduction = self.healthReduction * (random.random() + .5)
        return healthreduction


class StartGame:
    def startBattle(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == 'Game Over':
                print('Game Over')
                break
            if self.getAttackResult(warrior2, warrior1) == 'Game Over':
                print('Game Over')
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        attackAmountA = warriorA.attack()
        attackAmountB = warriorB.attack()

        dammageB = math.ceil(attackAmountA - attackAmountB)
        warriorB.health = warriorB.health - dammageB

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, dammageB))

        if warriorB.health <= 0:
            print("{} is victorious".format(warriorA.name))
            return 'Game Over'
        else:
            return 'Fight again'


def main():
    print('Warriors game')
    bob = Warrior('Bob', 50, 20, 10)
    builder = Warrior('Builder', 50, 20, 10)

    battle = StartGame()
    battle.startBattle(bob, builder)

if __name__ == '__main__':
    main()
