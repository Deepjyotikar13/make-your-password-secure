#this code will change every characters and convert into spacial or letters or degit
import random as d
import string
def otomatic_password(name):
	lowercase_letters=string.ascii_lowercase
	uppercase_letters=string.ascii_uppercase
	digit_s=string.digits
	spacial=["&","@","%","8$","#",")","(","*","5mn["]
	allcar=[lowercase_letters,uppercase_letters,spacial,digit_s]
	allcar2=[]
	#this loop will make a list of big alphabates and small alphabates spacial carecter 
	for i in range(0,len(allcar)):
		for t in range(0,len(allcar[i])):
			indexoflis=allcar[i]
			allcar2.append(indexoflis[t])
	d.shuffle(allcar2)#shuffeled the  list
	lis=list(name)
	for jk in range(0,len(lis)):
		randomletter=d.randint(0,len(allcar2)-1)
		lis[jk]=allcar2[randomletter]#change the letters in to spacial carrecters
	password_your=""
	for q in lis:
		password_your+=q
	return password_your
		
user=otomatic_password("deepjyoti")
print(user)