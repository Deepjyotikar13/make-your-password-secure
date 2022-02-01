#this was the frist password coad of mine it will convert your sting into spacial carrecters
import random as d
import string
letter=string.digits
result = string.hexdigits  
spacial=["&","@","%","8$","#",")","(","*","5mn["]
lis=[]
lis.extend(letter)
lis.extend(spacial)
lis.extend(result)
d.shuffle(lis)

kl=lis
user=input("enter password::")
lisus=list(user)
jk=len(lisus)
halfjk=jk/2
gh=float(halfjk+1)
ingh=int(gh)
lis45=[]
for i in range(1,ingh+1):
	ra=d.randint(0,len(lisus)-1)
	lis45.append(ra)
	klpd=set(lis45)
	
op=list(klpd)

lis79=[]
strlis=""
for z in lisus:
	strlis+=z
lis09=[]
lis5=[]
for e in range(0,len(op)):
	pj=op[e]
	jlo=strlis.replace(lisus[pj],kl[e])
	strlis=jlo
print("secure password is::",jlo)