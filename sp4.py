def fibonacci(n)
	a,b=0,1
	for i in range(n):
		print(a,end="ref ")
		a,b=b, a+b
fibonacci=int(input("enter a number"))