lst=[1,2,3,4,5]
sq_lst=[]
for i in lst:
	sq_lst.append(i**2)
print(lst)
print(sq_lst)

#convert a list of string to upper case using map function
#input=hello,world


strings=['hello','world']
map=list(map(str.upper ,strings))
print(map)



#add 10 to each number[1,2,3]


#num=[1,2,3]
#res=list(map(lambda x :x +10,num))
#print(res)
lambda
#find the product of all the number in a list using reduce function
#input numers=[1,2,3,4]
#output 24

from functools import reduce
list=[1,2,3,4]
numbers=reduce(lambda x,y:x+y,list)
print(numbers)


#find the longest word in a listof stings using reduce function 
#input=words=['apple','banana','cat','elephant']

from functools import reduce
words=['apple','banana','cat','elephant']
word=reduce(lambda x,y:x if len(x)>len(y) else y,words)
print(word)

#concatinate a list of stings in single string using reduce function
#input [ wlcom,to,skyllx]
#sring[welcome to skyllx]

from functools import reduce
s=['welcome','to','skyllx']
concatinate_string=reduce(lambda a,b:a+b,s)
print(concatinate_string)

#given a list of numbers , filer out even numbers, sq them , and find there sum
#input[1,2,3,4,5,6]
#56
#s=[1,2,3,4,5,6]
#sq=filter(lambda i:i%2==0,s)
#print(sq)



#using lambda function filter(),and map () process list of dict to extract or transform a spacific values
#input:data_equal[{'name':'shivu','age':25},{'name':'mayur','age':24}{'name':sanddy,'age':26}]
#task: extract the names of the people older then 25 in upper case
#output:SANDDY

#dicts=[{'name':'shivu','age':24},{'name':'mayur','age':25},{'name':'sanndy','age':26}]
#dict=list(map(lambda i:i['name'].upper(),filter(lambda s:s['age']>25, dicts)))
#print(dict)

#find the factorial of a number using reduse () and lambda()
#input[5]

from functools import reduce
factorial=lambda n :reduce(lambda a,b:a*b,range(1,n+1))
print(factorial(5))
