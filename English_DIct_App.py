# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:23:33 2022

@author: erohs
"""

import json
def main_menu():
    print('Main Menu \n1.Add a New Word \n2.Find the meaning \n3.Update a word \n4.Exit')
    
with open('words.txt','w') as D:
    dict_words = {}
    json.dump(dict_words,D)
    
main_menu()

while True:
    n = int(input('Enter the numerical value of your choice :'))
    if n ==1:
        with open('words.txt','w') as D:
            word = input('Enter a word : ')
            meaning = input('Enter the meaning of the word'+word+' :' )
            dict_words[word] = meaning
            json.dump(dict_words,D)
            
    elif n == 2:
        with open('words.txt','r+') as D:
            content = json.load(D)
            word = input('Enter the word to find its meaning = ')
            if word in dict_words:
                print('The meaning of the word = ',dict_words.get(word))
            else:
                print('The word is not present in the dictionary')
            json.dump(dict_words,D)
            
    elif n == 3:
        with open('words.txt','w') as D:
            word1 = input('Enter the word to update it = ')
            word1_meaning = input('Enter the meaning of the word = ')
            dict_words[word1]=word1_meaning
            json.dump(dict_words,D)
            
    elif n == 4:
        print('You have decided to exit the dictionary application')
        break
        
    else:
        main_menu()