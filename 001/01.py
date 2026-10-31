
s="  hello, Python  "
print(s)
print(s[1])
print(s[6:13])

# upper function
s1=s.upper()
print(s)
print(s1)

# lower() function
s1=s.lower()
print(s1)

# title function

s1=s.title()
print(s1)

# strip function

s1=s.strip()
print(s1)

# replace function

print(s.replace("ll","l"))

# find   gives starting index of the substring if found else -1

print(s.find("Python"))

# count() give the number of occurences of the substring in the string 

print(s.count("l"))
print(s.count("ll"))

# startwith() function checks if the string starts with the given substring and returnsn the boolean value True or False 

print(s.startswith("Python"))

# endswith() function checks if the string ends with the given substring and returns the boolean value True or False 

print(s.endswith("Python  "))

# split() function splits the string into a list of words based on the given separator (default is whitespace)

print(s.split())
print(s.split(","))

# join() function joins the elements of a list into a single string using the given separator 

print("-".join(s))
print("-".join(s.split(",")))

# concat +  concatenates two or more strings into a single string 

print("Java"+"Python")

# repeatation of string : * repeats the string a given number of times 

print("Java-Python"*3)

"""

  hello, Python  
 
o, Pyth
  hello, Python  
  HELLO, PYTHON  
  hello, python  
  Hello, Python  
hello, Python
  helo, Python  
9
2
1
False
True
['hello,', 'Python']
['  hello', ' Python  ']
 - -h-e-l-l-o-,- -P-y-t-h-o-n- - 
  hello- Python  
JavaPython
Java-PythonJava-PythonJava-Python

"""