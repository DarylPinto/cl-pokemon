from random import randint
from math import ceil
from time import sleep
from move import Move
from copy import deepcopy

class Pokemon:
  def __init__(self, name, hp, attack_power, element, moves):
    self.name = name
    self.hp = hp
    self.attack_power = attack_power
    self.element = element
    self.has_fainted = False
    self.moves = [deepcopy(move) for move in moves]
  
  def attack(self, enemy, move):

    print('')

    #Fail to execute attack if pokemon has fainted, doesn't know the move, or doesn't have enough PP
    if self.has_fainted:
      print("%s tried to attack, but didn't have the will!" % (self.name))
      return False
    if move not in self.moves:
      print("%s tried to use %s, but it doesn't know how!" % (self.name, move.name))
      return False
    if(move.pp <= 0):
      print("%s has used %s too many times. It has no more power!" % (self.name, move.name))
      move = Move("Struggle", 1, 10, "normal")

    #Announce move has been used
    print("%s used %s!" % (self.name, move.name))
    sleep(1)

    #Reduce pp
    move.pp -= 1

    #5% chance to miss
    if randint(1, 100) <= 5:
      print("But it missed!")
      sleep(0.5)
      return  False

    #Calculate damage
    damage = ceil((move.damage + self.attack_power) / 3)

    #Do extra damage if move type is the same as pokemon type
    if self.element == move.element:
      damage *= 1.5

    #5% chance to crit
    if randint(1, 100) >= 95:
      print("Critical Hit!")
      damage *= 2
      sleep(0.5)

    #Enemy takes damage
    enemy.hp = enemy.hp - damage

    #Announce enemy's status
    if(enemy.hp <= 0):
      enemy.has_fainted = True
      print("\n==================")
      print("%s fainted!" % enemy.name)
      print("==================")
    else:
      print("%s is now at %dHP!" % (enemy.name, enemy.hp))
