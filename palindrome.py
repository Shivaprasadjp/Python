num=input("enter the number:")
if num==num[::-1]:
	print(f"{num} is a palindrome.")
else:
	print(f"{num} is not a palindrome.")