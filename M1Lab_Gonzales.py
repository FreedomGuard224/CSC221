# -*- coding: utf-8 -*-
"""
CSC 221
M1 Lab
Gonzales Edmund
23 January 2019
"""
def main():
    """
    Bottles of beer song.
    """
    
    for beer in range(99,-1,-1):
        print(beer, "beers")

    beer = 99
    while beer != -1:
        print (beer, "beers")
        beer = beer -1
         
main()
