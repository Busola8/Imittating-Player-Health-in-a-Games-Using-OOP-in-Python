# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:02:38 2023

@author: deji
"""
'''
Add an instance variable "hp" (hit points) to the Player class and initialize it to 100.
Add a method "take_damage" to the Player class that takes in an integer "damage" and reduces the player's hit points by that amount.
Print out the player's name and remaining hit points after the player takes 20 points of damage.
'''
class Player:
    def __init__(self,firstname):
        self.firstname = firstname
        self.hp = 100
        
      
    def take_damage(self,damage):
        self.damage = damage
        self.hp -= self.damage
        
ken = Player(firstname= 'ken',hp = 100)

print(ken.firstname)
print(ken.take_damage(20))
print(ken.hp)
    