#changes made
import random as r 
userDict = {}
			 
def genPwd(name ):
	status = userChk(name)
	if(status == 1):
		password = randChars(4)+ randNumbers(8) + randChars(4)
		print "Password of  "+name+" is : "+ password 
		userDict[name] = password
	else :
		print "Error "
def userChk( name ):
	usersList = userDict.keys()
	if(name in usersList):
		print " User " +name+" already exist "
		return 0
	else:
		return 1 
def randChars(length):
	chars = []
	pwdStr = ""
	for i in range(1,length//2 +1):
		a = r.randint(67,90)
		b = r.randint(97,122)
		chars.append(chr(a))
		chars.extend(list(chr(b)))
	r.shuffle(chars)
	for char in chars:
		pwdStr =pwdStr+char
	return pwdStr
def randNumbers(length):
	nums = []
	pwdNum = ""
	for i in range(1,length):
		n = r.randint(0,9)
		nums .append(str(n))
		r.shuffle(nums)
	for num in nums:
		pwdNum =pwdNum+num
	return pwdNum

genPwd("khan")
genPwd("Shiva")
genPwd("Ravi")