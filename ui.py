#!/usr/bin/python
# -*- coding: utf-8 -*-     
from packages import caesar, vigenere
from packages.pygenere import *

CIPHERS = {
	1: 'Caesar',
	2: 'Vigenere'
}             
CIPHERS_CLASS = {
   	1: caesar.crack,
	2: vigenere.crack,
}
if __name__ == '__main__':
	is_stopping = False  
	while not is_stopping:
		print """
---------------------------------------------------
Here we are 
---------------------------------------------------   
Press Q to quit.
Available cyphers :
"""                             
   	 	for key, cipher in CIPHERS.items():
			print "    %s) %s" % (key, cipher)
		print "Choose which one to test"
		cipher_item = raw_input()  
		if cipher_item == "Q":
			is_stopping=True
			print "Stopping..." 
		else:  
			print "You chose to test %s algorithm" % CIPHERS[int(cipher_item)]
			CIPHERS_CLASS[int(cipher_item)]()
	
	