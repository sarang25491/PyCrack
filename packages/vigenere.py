# -*- coding: utf-8 -*-
from pygenere import *
 
def crack():          
	__min_range = 1
	__max_range = 50                                             
	print "Please enter the ciphered text :"
	ciphertext = raw_input()                     
	print "Min range for codeword (leave empty for default)"
	min_val = raw_input()                     
	if min_val:
		__min_range = int(min_val)    
	print "Max range for codeword (leave empty for default)"
	max_val = raw_input()                     
	if max_val:
		__max_range = int(max_val)                                
	print "We'll crack the Vigenere automatically."
	vig_crack = VigCrack(ciphertext)    
	# correcting length                    
	__min_range = min(len(ciphertext), __min_range)
	__max_range = min(len(ciphertext), __max_range) 
	print "Final range for codeword is [%s,%s])" % (__min_range, __max_range)
	print "Found message is : %s" % (vig_crack.crack_message(__min_range, __max_range))
	print "Found codeword is : %s" % (vig_crack.crack_codeword(__min_range, __max_range))  
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
					
				
		
