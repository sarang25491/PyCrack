# -*- coding: utf-8 -*-
from pygenere import Caesar

def crack():                                                       
	print "Please enter the ciphered text :"
	ciphered_text = Caesar(raw_input())
	print "We'll crack the Caesar cipher by testing a few shifts." 
	for shift in range(-10, 10):
		print "   Shitf: %s gives '%s'" % (shift, ciphered_text.decipher(shift))  
	print "Was attack successful ? (Y/N)"
	input = raw_input()
	if input == "Y":
		print "Exiting..."
	elif input == "N":
		print "Do you want to try custom tests ? (Y/N)"
		input = raw_input()
		if input == "Y":
			is_stopping = False
			while not is_stopping:
				print "Value to try (type Q to stop):"
				input = raw_input()
				if input == "Q":
					is_stopping = True
				else:                                                                       
					shift = int(input)
					print "   Shitf: %s gives '%s'" % (shift, ciphered_text.decipher(shift))
					
				
		
		