


#numbers=[1,2,3,4,5,6,7,8,9,10]
#is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1
#prime_numbers = list(filter(is_prime, numbers))
#print(prime_numbers)
num = int(input('Enter the number.'))
res = False
for i in range (2,num):
	if num%i ==0:
		res = True
print(res)