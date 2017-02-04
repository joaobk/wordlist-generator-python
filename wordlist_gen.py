#!/usr/bin/python
#coding: utf-8
import os

os.system("cls||clear")
print('''    _                   _     _    
   (_) ___   __ _  ___ | |__ | | __
   | |/ _ \ / _` |/ _ \| '_ \| |/ /
   | | (_) | (_| | (_) | |_) |   < 
  _/ |\___/ \__,_|\___/|_.__/|_|\_\
 |__/

### Faster number wordlist generator
### Coded by JoaoBK - Python 2.7                         
	''')

i = 0

first = raw_input("[+] First value: ")
second = raw_input("[+] Second value: ")
f = open('wordlist.txt', 'w')
for line in range(int(first), int(second)):
    f.write("%s\n" %line)
    i += 1
f.close()
print("\n[+] Wordlist created suceffuly! [ %i passwords! ] \n[+] Coded by JoaoBK\n[+] Made in Python 2.7 \n\n[...] Mirror: wordlist.txt" %i)