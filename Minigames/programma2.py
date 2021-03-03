#Ikki sonni EKUB, EKUKini topish

while True:
	a=int(input('1-sonni kiriting:'))	
	b=int(input('2-sonni kiriting:'))
	a1=a+1
	b1=b+1
	list=[]
	
	if a1>b1:
		for i in range(1,b1):
			if (a%i==0) and (b%i==0):
				list.append(i)
	elif a1<b1:
		for i in range(1,a1):
			if (a%i==0) and (b%i==0):
				list.append(i)
	else:
		list.append(a)
	
	c=max(list)	
	d=int(a*b/c)
	print('EKUB(' + str(a) + ' , ' + str(b) + ')=' + str(c))
	print('EKUK(' + str(a) + ' , ' + str(b) + ')=' + str(d))