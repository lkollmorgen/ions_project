
import math
import csv
import random
import argparse
from pprint import pprint

import pdb  # to use the debugger, python -mpdb filename.py input
            # n to skip and run next line

class CompoundCreator:
    def __init__(self):
        # define cation and anion dictionary
        self.cations, self.anions = self.get_ion_info()
        # optional command line parser
        self.parser = argparse.ArgumentParser(description='Generate an ionic compound from input ions')
        self.parser.add_argument('ion1', type=str,nargs='?')
        self.parser.add_argument('ion2', type=str,nargs='?')
        self.cmd_args = self.check_parse()
        
        if not self.cmd_args:
            print("Hello! Welcome to Compound Creator!")
            print("Enter both atomic symbols separated by a space (i.e. na cl)")
            print("To see a complete list of cations and anions for compound creation,",end='')
            print("type 'ion_list()' now")
        
        self.valid_ion_check()   
        self.compound = self.generate_compound(self.cat, self.an)
        self.print_compound()

    def ion_list(self):
        print('Cations: ',self.cations)
        print('Anions: ',self.anions)

# note if cmnd arguments were passed to generate a compound 
    def check_parse(self):
        self.args = self.parser.parse_args()
        if self.args.ion1 == None:
            return False
        return True

    def get_ion_info(self):
        with open('io_charges_sheet.csv', 'r') as f:
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

        return cats, ans

    def valid_ion_check(self):
        while True:
            #check if atoms were passed through arg parse. Then set to false to
            # fall into error-checking loop
            if self.cmd_args:
                atom_1, atom_2 = self.args.ion1,self.args.ion2
                self.cmd_args = False
            else: 
                atoms = input().lower()
                while ' ' not in atoms:
                    if atoms == 'ion_list()':
                        print('fetching list')
                        self.ion_list()
                        atoms=input().lower()
                    else:
                        print('please input more than 1 atom')
                        atoms = input().lower()
                atom_1, atom_2  = atoms.split()
            
        
        #begin setting cation and anion pair
            #identify the elements as cations or anions
            if atom_1 in self.anions.keys():
                print("got the anion first but ok")
                v_cation = atom_2
                v_anion = atom_1
            else:   #sets cation and anion for next round of error checking
                v_cation = atom_1
                v_anion = atom_2
            #Thorough error check

            #if not on anion list, raise: please enter 'cation' 'anion'
            if v_cation not in self.cations:
                print("Sorry, please enter a common cation. To see list, type 'ion_list()':")
            elif v_anion not in self.anions:
                print("Sorry, please enter a common anion. To see list, type 'ion_list()':")
            #if not 2 different elements, raise: please enter 'cation' 'anion'
            elif v_cation == v_anion:
                print("Sorry, please enter two different ions. To see list, type 'ion_list()':")
            else:
                self.cat, self.an = v_cation, v_anion
                break

    def generate_compound(self,cat, an):
        '''
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
        '''

        cat_charge = self.cations[cat]
        an_charge = self.anions[an]

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
    
    def print_compound(self):
        print(f"The compound composed of the entered elements is ", end="")
        print(f"{self.compound}")
    