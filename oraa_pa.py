def numToWords():
	num = input('Enter number: ')
	temp_num = str(num)
	str_num = ''
	length = len(temp_num)
	pos =0
	j=0

	str_form = ''
	for i in range(6, -1, -1):
		if i>length-1:
			str_num=str_num+'0'
		else:
			while j!=length:
				str_num=str_num+temp_num[j]
				j=j+1
				
	  		
	x=str_num
	while pos < 7 :
		#if x[pos] != '0': 
		if x[pos]=='0':
			if pos == 6 and length == 1:
				str_form = str_form + 'zero'
		
		elif pos != 2 and pos != 5:				#yung walng -ty or -teen
			if pos == 4 and (x[pos-1]!=0 or x[pos-2]!=0 or x[pos-3]!=0) and length>3:
				str_form = str_form+'thousand '

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

			
		else:									#yung may ty or -teen
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

			#if pos == 3 and length >=3:
			#	str_form=str_form+'thousand '
					
		pos = pos+1

	print str_form	

	return


def wordsToNum(word):
	word = word.split()
	for i in word:
		print i
	return
def wordsToCurrency():
	return
def numberDelimitered():
	return


print 'MENU'
print '[1] Number to Word'
print '[2] Word to Number'
print '[3] Word to Currency'
print '[4] Number Delimitered '
print '[0] Exit '
ch = input('choice: ')


if(ch==1):
	 numToWords();
elif(ch==2):
	word= raw_input("Enter input: ")
	wordsToNum(word); 
elif(ch==3):
	wordsToCurrency();
elif(ch==4):
	numberDelimitered();
else:
	print 'Invalid!'



