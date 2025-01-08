# print("welcome to SkyllX")

# name = input()
# print(name)

# for nameId in range(0,3):
#     name = input("Enter the name : ",) 
#     print("Name at",nameId+1," - ",name)
    # shivu

# list = ['Arun','Shivu',"Mahanthesh","Vishal"]
# print(list[4])
# for names in list :
#     print(names)

# Q: Using range() to iterate Over numbers
    # 1, 2, 3, 4, 5
    # range(firstIndex,lastIndex) -> firstIndex,....,lastIndex-1
    # range(0,5) -> 0, 1, 2, 3, 4
    # range(5,10)-> 5, 6, 7, 8 , 9
    # range(0,6) -> 0, 1,2,3,4,5
# for i in range(1,6) :
#     print(i)
# for i in range(0,5) :
#     print(i+1)

# Q: Iterate over a string
    # SkyllX -> S, k, y, l, l, X

#str="skyllx"
#for chars in str :
    #print(chars )

# Iterating with indexes
# names = ['Arun','Shivu',"Mahanthesh","Vishal"]
# 0 : Arun
# 1 : Shivu
# 2 : Mahanthesh
# 3 : Vishal
# # (enumerate)
# for index, name in enumerate(names) :
#     print(index,' : ',name)

# continue(skipping the iteration) & break(breaking the loop)
# for i in range(0,10) :
#     if(i == 0 or i == 3):
#         continue
#     if(i==7):
#         break
#     print(i)

# Nested for loop
# for i in range(2):
#     for j in range(3):
#         print("i = ",i," j = ",j)

#write a python program to print all the elements of a list, one by one 

# things=['fan','table','botel','book']
# for thing in things:
#     print(thing))

#create a program that prints numbers from 1 to 10 using a for loop
# for num in range(0,10):
#     print(num+1)
#given a string print each charecter of the string on a new line
# string='shivaprasad'
# for str in string:
#     print(str)
#write a program to calculate sum of all the numbers in a list using for loop
# sum=0
# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     sum=sum+num
# print(sum)
    

#use a for loop print a even numbers between 1,20
# even=()
# for num in range(1,21):
#     if num%2==0:
#         print(num)

# for num in range(1,21):
#     if num%2==1:
#         print(num)

# from shapely.geometry import Polygon
# import matplotlib.pyplot as plt
# import numpy as np
# coords = [(0,2), (1, 0), (1, 1), (0, 1)]
# polygon = Polygon(coords)
# x, y = polygon.exterior.xy
# fig, ax = plt.subplots()
# ax.plot(x, y, color='blue')
# ax.fill(x, y, alpha=0.5, fc='lightblue', ec='blue')
# plt.title('Polygon Example')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.show()

#sort a list of tuple based on second element 
#input[(1,3),(4,1),(2,2)]
#output[(4,1),(2,2),(1,3)]

# sort_list=[(1,3),(4,1),(2,2)]
# sorted_lst=sorted(sort_list,key=lambda x:x[-1])
# print(sorted_lst)

#creat a lambda()to find a maximum of 2 numbers
#input(5,10,50)
#output(50)

# max=(lambda a,b,c: a if a>b else c)
# print(max(2,4,55))

# write a  program to remove a duplicate in list while maintaining the order
# input: list[1,2,3,4,4]
# output[1,2,3,4]

# lst = [1, 2, 3, 4, 4]
# duplst=[]
# for i in lst:
#     if i not in duplst:
#         duplst.append(i)
# print(duplst)        

# def duplicate(lst):
#     return list(dict.fromkeys(lst))
# print(duplicate(lst))

#write a program to find all numbers between 1 and 1000 that divisible by 7 but not multiply of 5 

# def find_numbers():
#     for i in range(1, 1001):
#         if i % 7 == 0 and i % 5 != 0:

# print(list(filter(lambda i : i%7==0 and i%5!=0 ,range(1,1001))))

# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()


# def sub():
#     a=10
#     b=20
#     c=a-b
#     print(c)
# sub()

# def mul():
#     a=10
#     b=20
#     c=a*b
#     print(c)
# mul()

# def div():
#     a=10
#     b=2
#     c=a/b
#     print(c)
# div()

# rev=input("Enter the string :")
# rev=rev[::-1]
# print(rev)

str=input("Enter the string :")
for chars in str :
    print(chars )