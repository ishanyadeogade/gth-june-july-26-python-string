
# WAP to convert user given string into capitalize form 


user_string = input("Enter a string : ")
new_string=""
i=1

ascii_val = ord(user_string[0])

if(ascii_val>=96 and ascii_val<=125):
    new_string+=chr(ascii_val-32)
    
while i < len(user_string) :
    ascii_val = ord(user_string[i])
    ascii_val_2 = ord(user_string[i-1])  
    if( (ascii_val>=96 and ascii_val<=125) and not (ascii_val_2>=96 and ascii_val_2<=125) ): # (not) check wheather previous value is alphabet 
 
            new_string+= chr(ascii_val-32)
    else :
        new_string+=user_string[i]
        
    i+=1

print(new_string)
    
    
"""

Enter a string : hello!!how-are_you ! after long time !!!
Hello!!How-Are_You ! After Long Time !!!

"""


"""


# WAP to convert user given string into capitalize form 


user_string = input("Enter a string : ")
new_string=""
i=1

ascii_val = ord(user_string[0])

if(ascii_val>=96 and ascii_val<=125):
    new_string+=chr(ascii_val-32)
    
while i < len(user_string) :
    if user_string[i]==' ':
        i+=1
        ascii_val = ord(user_string[i])
        if(ascii_val>=96 and ascii_val<=125):
            new_string=new_string + " " + chr(ascii_val-32)
    else :
        new_string+=user_string[i]
        
    i+=1
    


print(new_string)
    



"""


