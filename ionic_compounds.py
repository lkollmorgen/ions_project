#! /bin/env python

import math
import numpy as np
import pandas as pd
import csv
import random
import argparse
import logging as log
from pprint import pprint

import pdb  # to use the debugger, python -mpdb filename.py input
            # n to skip and run next line

def valid_ion_check():
    we_good = False
    while True:
        i_compound = input().lower()
    #splits input into 2 elements by space-bar
        atom_1, atom_2 = i_compound.split(' ')

    #begin setting cation and anion pair
        #identify the elements as cations or anions
        if atom_1 in anions.keys():
            print("got the anion first but ok")
            v_cation = atom_2
            v_anion = atom_1
        else:   #sets cation and anion for next round of error checking
            v_cation = atom_1
            v_anion = atom_2

    #Thorough error check
        #if not on anion list, raise: please enter 'cation' 'anion'
        # if (cations.__contains__(v_cation) == False):
        if v_cation not in cations:
            print("Sorry, please enter a common cation:")    
        # elif (anions.__contains__(v_anion) == False):
        elif v_anion not in anions:
            print("Sorry, please enter a common anion:")
        #if not 2 different elements, raise: please enter 'cation' 'anion'
        elif v_cation == v_anion:
            print("Sorry, please enter two different ions:")
        else:
            break
    return v_cation, v_anion

def generate_compound(cat, an):
    if False:
        #finds index for elmental symbol in cations/anions arrays
        cat_pos = np.where(cations == cat)
        an_pos = np.where(anions == an)

        #sets pre-processed cation and anion charges
        cat_charge = str(cation_charges[cat_pos])
        an_charge = str(anion_charges[an_pos])

        #processes array value by removing brackets and quotes
        cat_charge = cat_charge.strip("[]")
        an_charge = an_charge.strip("[]")

        cat_charge = int(cat_charge.strip("''"))
        an_charge = int(an_charge.strip("''"))

    cat_charge = cations[cat]
    an_charge = anions[an]

    cat = cat.capitalize()
    an = an.capitalize()

    #determines if the charges can be simplified
    if cat_charge == an_charge:
       cat_charge = cat_charge // cat_charge
       an_charge = an_charge // an_charge

    #determines final ordering of compound. Swaps cation and anion charge
    if cat_charge > 1 and an_charge > 1:
        g_compound = cat + str(an_charge) + an + str(cat_charge)

    elif cat_charge > 1 and an_charge == 1:
        g_compound = cat + an + str(cat_charge)

    elif cat_charge == 0 and an_charge > 1:
        g_compound = cat + str(an_charge)+ an

    else:
        g_compound = cat + an 
    
    return g_compound

#def generate_random_elements():

def get_ion_info():
    #generate numpy arrays from imported csv
    with open('ion_charges_sheet - Sheet1.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    #seperate first column into elements and second into charges
        #seperate positive charges into a subcategory (cation) and
        #negative charges into a subcategory (anion)

    with open('ion_charges_sheet - Sheet1.csv', 'r') as f:
        lines = f.readlines()

    cats = {}
    ans = {}
    for line in lines[1:]:
        line = line.strip()
        #print( f'line = [{line}]' )
        cation, cation_charge, anion, anion_charge = line.split(',')
        if cation_charge:
            cats[cation] = int(cation_charge)
        if anion_charge:
            ans[anion] = int(anion_charge)

    # pprint( 'cations: ' )
    # pprint( cats )
    # pprint( 'anions ' )
    # pprint( ans )

    return cats, ans

    # ions_array = np.array(data)
    # return np.split(ions_array, 4, axis=1)

if __name__ == "__main__":

    """
    parser = argparse.ArgumentParser()
    parser.add_argument( 'ion', nargs='*', default=None, help='Supply one metal and one non-metal ion' )
    parser.add_argument( '--test', action='store_true', default=False )

    args = parser.parse_args()
    if test:
        pass
    else:
        if len(args.ion) != 2:
            raise "You done effed up"
        print( f'args = "{args}' )
        """

    log.basicConfig( format='%(levelname)s: %(message)s', level=log.DEBUG )

    # cations, cation_charges, anions, anion_charges = get_ion_info()
    cations, anions = get_ion_info()

    #print: welcome, would you like to create an ionic compound or test yourself?
    print("Hello! Welcome to Compound Creator! Would you like to create an ionic compound or test yourself?")
        #if create an ionic compound, then print: enter both atomic symbols separate by a space
        #i = input()
        #test if i =="i.*"
    if input() == "ionic compound" or "ionic compounds" or "ionic": 
        print("Awesome! Enter both atomic symbols separated by a space (i.e. na cl)")
        
        cation, anion = valid_ion_check()
        print(f"The compound composed of the entered elements is ", end="")
        print(f"{generate_compound(cation, anion)}")
        exit()

    if input() == "test yourself" or "Test yourself" or "Test":
        
        print ("What is the binary ionic compound comprised of the following elements?: ")
        
        #if test yourself, print: write the molecular formula for the following compound
        #(not case sensitive) I.e. mgbr2
            #generate one random cation and one random anion, seperated by a space
                #error cases:
                #np.choose(array, choices, out)
                    #if only one element entered print: please enter molecular formula
                    #if press enter, repeat prompt
            #if incorrect, print: not quite! the molecular formula for {atom1} and {atom2} is {answer}
            #if correct, print: you got it!
    