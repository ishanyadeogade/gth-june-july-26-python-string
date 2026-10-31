
# WAP to take input string from user and check whether the string is palindrome or not


user_string = input("Enter a string : ")
l=0
r=len(user_string)-1
flag=True

while l<r:
    if user_string[l]!=user_string[r]:
        flag=False 
        break 
    l+=1
    r-=1

if(flag):
    print("Palindrome")
else : 
    print("Not Palindrome")
        
"""


Enter a string : abcdcba
Palindrome

Enter a string : abcdfcba
Not Palindrome

"""