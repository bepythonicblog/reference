#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:53:08 2021

@author: mac
"""
from collections import namedtuple as nd
from random import choice

Card = nd('Card',['r','s'])

class FrenchDeck:
    r = [str(n) for n in range(2,11)] + list('JQKA')
    s = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.cards = [Card(r,s) for r in self.r for s in self.s]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self,index):
        return self.cards[index]

    def __setitem__(self,index,value):
        self.cards[index] = value
        return self.cards

    def __str__(self):
        cards = [str(c) for c in self.cards]
        return cards

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.r.index(card.r)
    return rank_value * len(suit_values) + suit_values[card.s]

def main():
    cards = FrenchDeck()
    c1 = choice(cards)
    for c in sorted(cards,key=spades_high):
        print(c)
if __name__ == "__main__":
    main()