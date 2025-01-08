from functools import reduce
factorial=lambda n :reduce(lambda a,b:a*b,range(1,n+1))
print(factorial(5))


cube=(lambda i:i**3)
print(cube(3))


#everse_string=lambda s: s(::-1) 
#print(reverse_string('python'))

#revr=lambda x:x[::-1]
#print(rev(121)==121)

