# name=input("Enter a name:")
# def my_name(hello):
#     print("my_name",hello)
# my_name(name)

# name=input("Enter a name:")
# def your_name(name):
#     print("your_name",name)
# your_name(name)


# def print_name(name):
#     name=input("Enter a name")
#     print("Your name:",name)
# print_name(name)

# print ("apple")
# print ("pinaple")
# print ("cap")
# print ("car")
# print ("tiger")
# print ("chair")
# print ("mango")
# print ("laptop")
# print ("tv")
# print ("phone")

# name=input("Enter a name: ")
# print(name)
# thing=input("Enter a thing: ")
# print(thing)
# animal_name=input("Enter a animal name: ")
# print(animal_name)
# subject=input("Enter a subject name: ")
# print(subject)
# bike=input("Enter a bike name: ")
# print(bike)
# car=input("Enter a car name: ")
# print(car)
# surname=input("Enter a surname: ")
# print(surname)
# place=input("Enter a name: ")
# print(place)
# gun=input("Enter a gun name: ")
# print(gun)
# sleeper=input("Enter a sleeper name: ")
# print(sleeper)

# def name():
#     user_input=input("Enter a name: ")
#     print("your Name Is ",user_input)
# name()

# def print_function():
#     user=int(input("Enter a number : "))
#     print("Number Is ",user)
# print_function()

# def python():
#     py=input("Enter a program name: ")
#     print("your Name Is ",py)
# python()

# def car():
#     cars=input("Enter a car name: ")
#     print("your Name Is ",cars)
# car()

# def bike():
#     bikes=input("Enter a bike name: ")
#     print("your Name Is ",bikes)
# bike()

# def things():
#     thing=input("Enter a name: ")
#     print("your Name Is ",thing)
# things()

# def company():
#     campanys=input("Enter a company name: ")
#     print("your Name Is ",campanys)
# company()

# def course():
#     course_name=input("Enter a course: ")
#     print("your Name Is ",course_name)
# course()

# def float_num():
#     f_num=input("Enter a number: ")
#     print("float num Is ",f_num)
# float_num()

# def language():
#     lang=input("Enter a language name: ")
#     print("your language Name Is ",lang)
# language()



# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()
# #
# def get_input():
#     user_input = input("Enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)
# #
# def main():
#     user_input = get_input()
#     print_input(user_input)
# main()

# def get_input():
#     user_input = input("Please enter something: ")
#     return user_input

# def print_input(user_input):
#     print("You entered:", user_input)

# user_input = get_input()
# print_input(user_input)

# import re
# s="""+91-8550086292(India)
# +6738762878726(usa)
# +909003738837(paK)
# +91-8476536627(India)"""
# print(re.findall(r"\+91-\d{10}",s))


# nums=[2,7,11,15]
# target=9
# print(two_sum(nums,target))


n=int(input("Enter the numbers of elements in list: "))
nums=[]
for i in range(n):  # range(4), i = 0, 1, 2, 3
    print("Enter ",i+1, "Element") # 1, 2, 3, 4
    a=int(input()) #2, 11, 15, 7
    nums.append(a) # nums = [2,11, 15, 7]
target=int(input("Enter the target element: ")) # 9
lst = [2,3,5,8]
target = 11

emtydict = {}
def two_sum(items, goal):

    for i, num in enumerate(items):  #i=0,num=2  #i=1, num=11  #i=2, num=15  #i=3, num=7    #[(0,2),(1,3),(2,5),(3,8)]
        trg_element = goal - num   # target=9  ,trg_dict=7        #target=9  ,trg_dict=-2 # trg_dict=-6 # trg_dict=2 
        if trg_element in emtydict:   # if 2 in {2: 0, 11:1, 15: 2} => true
            return [emtydict[trg_element], i]   
        emtydict[num] = i  # emtydict={2: 0, 3:1, 5: 2 , 8: 3}
        print(emtydict)
print(two_sum(nums, target))    
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return[]
n=int(input("Enter the numbers of elements in list: "))
print("Enter ",i+1, "Element")
target=int(input("Enter the target element: "))
print(twoSum(nums,target))
print("Printing...")
for key, value in emtydict.items():
    print(key,value)



# #details 1
# name1="vinay"
# age1=26
# mobile1=78909877887

# #details 2
# name2="shivu"
# age2=24
# mobile2=67898765678

# def printing_details(name, age, mobile):   # syntax : def function_name():
#     print(name, age, mobile)

# printing_details(name1,age1,mobile1)
# printing_details(name2,age2,mobile2)

# lst = [2,3,5,8]
# target = 11

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if i!=j and lst[i]+lst[j]==target:
#             print([i,j])

# write a python program to check if  a number is even or odd

# even_odd=int(input("Enter a number: "))
# if even_odd%2==0:
#     print("The given number is even")
# else:
#     print("The given number is odd")


# a=input("Enter a string: ")
# rev_string=a[::-1]
# print(rev_string)

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# def largest_num(a,b,c):
#     return max(a,b,c)
# print(largest_num(a,b,c))


# palindrome=input("Enter a string: ")
# name=palindrome[::-1]
# print(num)

# num=int(input("Enter number to find the Factorial... "))
# def fact(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num * fact(num-1)
# print("Factorial Number of",num,"is :",fact(num))

# def is_palindrome(input_string):
#     return input_string == input_string[::-1]
# input_str =input("Enter a something: ")
# if is_palindrome(input_str):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)