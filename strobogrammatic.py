def check(n):
	num=n
	rev=0
	while n>0:
		rem=n%10
		n=n//10
		if rem in [2,3,4,5,7]:
			break
		if rem==6:
			rev=(rev*10)+9
		elif rem==9:
			rev=(rev*10)+6
		else:
			rev=(rev*10)+rem
	if rev==num:
		return True
	else:
		return False
n=int(input("enter the number of digits :"))
for i in range(10**(n-1),10**n):
	if check(i):
		print(i)