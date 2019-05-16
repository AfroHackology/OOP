#Now update Hand in hands.py. I'm going to use code
# similar to Hand.roll(2) and I want to get back an
# instance of Hand with two D20s rolled in it. I should
# then be able to call .total on the instance to get the
# total of the two dice.
#I'll leave the implementation of all of that up to you.
# I don't care how you do it, I only care that it works.
from notes.OOP.challenges.RPGRoller.dice import *
class Hand(list):
    @property
    def total(self):
        return sum(self)
# get back an instance of Hand with two D20s rolled in it

    # call total on the instance for total of 2 dice



