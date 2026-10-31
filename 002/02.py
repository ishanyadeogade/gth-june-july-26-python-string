
# WAP to input string from keyboard and convert lower case string to upper case without using upper() function 

string_value = input("Enter a string: ")
i = 0 
result_string = ""
while i<len(string_value):
    ch = string_value[i]
    ch_ascii = ord(ch)
    
    if ch_ascii>=65 and ch_ascii<=90:
        ch_ascii=ch_ascii+32
        result_string+=chr(ch_ascii)
    else :
        result_string+=ch
        
    i+=1
print(result_string)

"""

D:\Workspace\workspace-vsc\gth-june-july-26-python-string\002>python 02.py
Enter a string: NaIm
naim

"""
    
    