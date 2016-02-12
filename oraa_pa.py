def numToWords():
	temp_num = raw_input('Enter number: ')
	
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
		
		if pos == 4 and (x[pos-1]!='0' or x[pos-2]!='0' or x[pos-3]!='0') and length>3:
			str_form = str_form+'thousand '

		if x[pos]=='0':
			if pos == 6 and length == 1:
				str_form = str_form + 'zero'
		
		elif pos != 2 and pos != 5:				#yung walng -ty or -teen

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
					
		pos = pos+1

	print str_form	

	return


def wordsToNum(word):
	word = word.split()
	gen_num = 0		#total value
	temp = 0		#current integer
	mill_num=0
	hund_thou = 0
	hund = 0
	wLen = len(word)
	flag=0		# is equal to 1 if there should be no more thousands
	
	i=0

	while i < wLen:
		
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
		elif word[i] == 'million':
			mill_num= temp*1000000
			temp=0
		elif word[i] == 'hundred':
			temp= temp*100
		elif word[i] == 'thousand':
			hund_thou = hund*1000
			hund=0
			temp=0
		hund = temp; 
		i+=1	
	
	gen_num= mill_num+hund_thou+hund
	print gen_num
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



