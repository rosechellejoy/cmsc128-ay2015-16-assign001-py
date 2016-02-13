import sys

"""
	numToWords() accepts an input number and outputs its equivalent in words
	temp_num : input by the user
"""
def numToWords(temp_num):		
	if len(temp_num)>7:						#if number inputed is greater than 7 digits: invalid
		print 'Invalid: input can only have at most 7 digits'
		return
	str_num = ''			#word equivalent of temp_num
	length = len(temp_num)	#input length
	pos =0					#current position
	j=0		

	str_form = ''
	for i in range(6, -1, -1):			#places input value in an array of 7 elements(for each digit)
		if i>length-1:					#if current length is less than current max number of digits
			str_num=str_num+'0'			
		else:
			while j!=length:			#while input is not fully transferred to str_num 
				str_num=str_num+temp_num[j]	
				j=j+1
				
	  		
	x=str_num			#holds input in its 7 digit representation
	while pos < 7 :		
		
		if pos == 4 and (x[pos-1]!='0' or x[pos-2]!='0' or x[pos-3]!='0') and length>3:	
			str_form = str_form+'thousand '				#if at 4th pos and 3 previous digits are not == 0

		if x[pos]=='0':									#if number is 0
			if pos == 6 and length == 1:
				str_form = str_form + 'zero'
		
		elif pos != 2 and pos != 5:				#ones digit

			if x[pos]=='1':	
				str_form = str_form+'one '
			elif x[pos]=='2': 
				str_form=str_form+'two '
			elif x[pos]=='3': 
				str_form=str_form+'three '
			elif x[pos] =='4': 
				str_form=str_form+'four '
			elif x[pos]=='5': 
				str_form=str_form+'five '
			elif x[pos]=='6': 
				str_form=str_form+'six '
			elif x[pos]=='7': 
				str_form=str_form+'seven '
			elif x[pos]=='8': 
				str_form=str_form+'eight '
			elif x[pos]=='9': 
				str_form=str_form+'nine '

			if pos == 0:
				str_form = str_form+'million '
			elif pos == 1 or pos == 4:
				str_form = str_form+'hundred '

			
		else:									#tens digit
			if pos == 2 or pos == 5:
				if x[pos]== '1':
					pos=pos+1
					if x[pos]== '0': 
						str_form = str_form+'ten '
					elif x[pos]== '1': 
						str_form = str_form+'eleven '
					elif x[pos]== '2':
						str_form = str_form+'twelve '
					elif x[pos]== '3':
						str_form = str_form+'thirteen '
					elif x[pos]== '4':
						str_form = str_form+'fourteen '
					elif x[pos]== '5':
						str_form = str_form+'fifteen '
					elif x[pos]== '6':
						str_form = str_form+'sixteen '
					elif x[pos]== '7':
						str_form = str_form+'seventeen '
					elif x[pos]== '8':
						str_form = str_form+'eighteen '
					elif x[pos]== '9':
						str_form = str_form+'nineteen '
					
				elif x[pos]== '2':
					str_form = str_form+'twenty '
				elif x[pos]== '3':
					str_form = str_form+'thirty '
				elif x[pos]== '4':
					str_form = str_form+'forty '
				elif x[pos]== '5':
					str_form = str_form+'fifty '
				elif x[pos]== '6':
					str_form = str_form+'sixty '
				elif x[pos]== '7':
					str_form = str_form+'seventy '
				elif x[pos]== '8':
					str_form = str_form+'eighty '
				elif x[pos]== '9':
					str_form = str_form+'ninety '

				if pos == 2 or pos == 5:
					pos= pos+1
					if x[pos]=='1': 					#single digit after tens
						str_form = str_form+'one '
					elif x[pos]=='2': 
						str_form=str_form+'two '
					elif x[pos]=='3': 
						str_form=str_form+'three '
					elif x[pos] =='4': 
						str_form=str_form+'four '
					elif x[pos]=='5': 
						str_form=str_form+'five '
					elif x[pos]=='6': 
						str_form=str_form+'six '
					elif x[pos]=='7': 
						str_form=str_form+'seven '
					elif x[pos]=='8': 
						str_form=str_form+'eight '
					elif x[pos]=='9': 
						str_form=str_form+'nine '
					
		pos = pos+1				#increment pos

	print str_form				#print word representation

	return

"""
	wordsToNum() accepts word(s) then prints its numerical equivalent
	word - string input 
"""
def wordsToNum(word):
	word = word.split()		#word- list of words from word 
	gen_num = 0		#total value
	temp = 0		#current integer
	mill_num=0		#total million value of word
	hund_thou = 0	#total hundred thousand value of word
	hund = 0		#total hundred value of word
	wLen = len(word)# number of words in word
	flag=0		# is equal to 1 if there should be no more thousands
	
	i=0

	while i < wLen:					#iterates through each word in word(list)
		
		if word[i] == 'one':
			temp+=1
		elif word[i] == 'two':
			temp+=2
		elif word[i] == 'three':
			temp+=3
		elif word[i] == 'four':
			temp+=4
		elif word[i] == 'five':
			temp+=5
		elif word[i] == 'six':
			temp+=6
		elif word[i] == 'seven':
			temp+=7
		elif word[i] == 'eight':
			temp+=8
		elif word[i] == 'nine':
			temp+=9
		elif word[i] == 'ten':
			temp += 10
		elif word[i] == 'eleven':
			temp += 11
		elif word[i] == 'twelve':
			temp += 12
		elif word[i] == 'thirteen':
			temp += 13
		elif word[i] == 'fourteen':
			temp += 14
		elif word[i] == 'fifteen':
			temp += 15
		elif word[i] == 'sixteen':
			temp += 16
		elif word[i] == 'seventeen':
			temp += 17
		elif word[i] == 'eighteen':
			temp += 18
		elif word[i] == 'nineteen':
			temp += 19
		elif word[i] == 'twenty':
			temp += 20
		elif word[i] == 'thirty':
			temp += 30
		elif word[i] == 'forty':
			temp += 40
		elif word[i] == 'fifty':
			temp += 50
		elif word[i] == 'sixty':
			temp += 60
		elif word[i] == 'seventy':
			temp += 70
		elif word[i] == 'eighty':
			temp += 80
		elif word[i] == 'ninety':
			temp += 90	
		elif word[i] == 'million':		#multiply previous number(temp) to 1000000
			mill_num= temp*1000000		#place in mill_num
			temp=0					
		elif word[i] == 'hundred':		#multiply value in temp to 100
			temp= temp*100
		elif word[i] == 'thousand':		#multiply hund to 1000 then place in hund_thou 
			hund_thou = hund*1000
			hund=0						
			temp=0
		hund = temp; 					
		i+=1		#increment i then next iteration
	
	gen_num= mill_num+hund_thou+hund 	#gen_num= accumulated value of millions, hundred thousands, and hundreds
	print gen_num						#print total number
	return

"""
	wordsToCurrency() accepts two inputs then generates string in number form with given currency
	word - number in words inputed by the user
	cur- currency given by the user
"""
def wordsToCurrency(word, cur):
	if cur=='USD' or cur=='JPY' or cur == 'PHP':	#checks if currency given is valid
		sys.stdout.write(cur)						#print currency
		wordsToNum(word)							#print word in its numerical value
	else:					
		print 'Invalid!'

	return

"""
	numberDelimitered() accepts three inputs then prints the number with a delimiter in the position given by the user
	temp - number
	delimiter - delimiter given by the user
	jumps - # of jumps from the right
"""	
def numberDelimitered(temp, delimiter, jumps):
	temp= str(temp)			#typecast temp to a string
	rev=''					#will hold temp in reverse
	i=0	
	if len(temp) > 7:
		print 'Invalid!: exceeded max no. of digits'
		return

	for i in range(0, len(temp)):			#reverse number input
		rev=temp[i]+rev
	
	temp=''	
	for i in range(0, len(rev)):			#iterates through all digits in rev
		if jumps== i:						#if i == jumps
			temp= delimiter+temp 			#concatenate delimiter with temp
			
		temp= rev[i]+temp 					#concatenate rev[i] with temp

	print temp
	return

"""
	prints menu and lets the user choose feature to be used
"""
print 'MENU'
print '[1] Number to Word'
print '[2] Word to Number'
print '[3] Word to Currency'
print '[4] Number Delimitered '
ch = input('choice: ')


if(ch==1):			#number to words
	temp_num = raw_input('Enter number: ')
	numToWords(temp_num);

elif(ch==2):		#word to number
	word= raw_input("Enter input: ")
	wordsToNum(word); 

elif(ch==3):		#number to currency
	word= raw_input("Enter number in words: ")
	cur= raw_input("Enter currency: ")

	wordsToCurrency(word, cur)

elif(ch==4):		#number delimitered
	temp = raw_input('Enter number: ')
	delimiter = raw_input('Enter delimiter: ')
	jumps = input('Enter # of jumps: ')
	numberDelimitered(temp, delimiter, jumps);

else:
	print 'Invalid!'