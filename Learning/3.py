






# ----------------
# VIDEO 1 :  INTROUDCUTON to data types

# python support various data types 

# string           "hello"
# numberic :-      init, float, complex, bool  ------- 1, 2.2 , 2b 3b, true/false
# list             []
# tuple            a pair of data types ---we wil learn more 
# set              same as list but without indexes
# dictionary       key value pair's like data storing
# none             none same as null in js
        






# ----------------
# VIDEO 2 :  String

# string are in char or numb or anything in qquates like "" ''
# "123" '123' 'hello' "hello"

# in brief string is called str
# to check if it is string just type(check waht)
        






# ----------------
# VIDEO 3 :  Escape Sequences

# to add special char in string we use escape sequences 

x = "Hello \"world" # adds quates double \"
print(x)

y = "hello w\borld" # backspace deltes \b
print(y)

z = "hello w\norld" # \n means new line
print(z)

w = "hello \t world" # what if wanna want a tab space \t
print(w)

q = "hello \\ world" # want a slash then \\
print(q)


        






# ----------------
# VIDEO 4 :  Multi Line String


# to print a apragraph in multiple line
ox = """

 Hello world
hi my name is
basith """
print(ox)



        






# ----------------
# VIDEO 5 : Basic String Method

msg = "Hello World "

print("_________________________")
print("Basic String Method")

print(msg.upper()) #prints in upper case
print(msg.title()) #prints first letter in upper case
print(msg.capitalize()) #prints first letter of first word in upper case
print(msg.lower()) #prints in lower case
print(msg.strip()) #removes extra spaces
print(msg.replace("H", "J")) #replaces H with J
print(msg.lstrip()) #removes spaces from left
print(msg.rstrip()) #removes spaces from right



        






# ----------------
# VIDEO 6 : Split and Join

mystr = "Hello World welcome to python programming"
greet = "i am basith"

print("_________________________")
print("Split and Join")
print(mystr.split(" ")) #splits the string from space and makes it a list
print(greet.split("a")) #splits the string from a and makes it a list

print("Join")
print(" ".join(greet)) #joins the string with space
print("-".join(greet)) #joins the string with -


        






# ----------------
# VIDEO 7 : Search in a string

# hwo to search in a string

hi = "balls apple cat dog elephant"

print("balls" in hi)
print("balloon" in hi)
print(hi.startswith("balls"))
print(hi.find("cat")) #gives index of cat
print(hi.count("a")) #counts number of a in the string

        






# ----------------
# VIDEO 8 : Numerical Types


# integer means 10, 20, 32 , like that
# float means 10.5, 20.3, like that
# complex means 2b, 3b, like that
        






# ----------------
# VIDEO 9 : Integer Arithemetic Basic Operator

x = 10
y = 20
print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) # division
print(x // y) # floor division
print(x % y) # modulus
print(x ** y) # exponentiation

print("abd" + "def") # string addition



        






# ----------------
# VIDEO 10 : Writing complex expression
x = 10
y = 15
z = 20
# print(a = x + (y*z)) 

print(2 ** 4 )

# multiplication division remainded ..









# ----------------
# VIDEO 11 : Type Casting

# converting means type casting

number1 = "125"
number2 = 125

print(number2 + int(number1)) # converts number2 to int and adds
        










# ----------------
# VIDEO 12 : Comparison Operators


a = 10
b = 20
print("Comparison Operators===================================")
# print(a = b) # equal to
print(a == b) # equal to equal
print(a != b) # not equal to
print(a > b) # greater than
print(a < b) # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

# print(a is b) # is
# print(a is not b) # is not
# print(a in b) # in
# print(a not in b) # not in


fruit1 = "apple"
fruit2 = "banana"
print("a" in fruit1) # in
print("a" not in fruit1) # not in
print("ba" in fruit2) # in
print("ba" not in fruit2) # in














# ----------------
# VIDEO 13 : String Formatting
sentence = "I have  apples and bananas"
name = "basith"
year = 2024
class_ = "12th"
division = "A"

print(f"my name is {name} and i am studing in {year}") # f string


#or


print("my name is %s i'm studyin in %s %s " % (name, class_, division))

print(11/3) # 3.6666666666666665
# this has too many char
#  so 
print('%.3f' % (11/3)) # 3.667



blah = "my name is {1} and i am studing in {2} {3}".format(name, class_, division)

# by this we can give custom order









# ----------------
# VIDEO 14 : Variables


# data storing is done using variables 

hello = "hello world"
# in var python case sensitive
# don't start with number
# can't use special char except _
# can't use keywords like if, else, for, while, class, etc
# var must be meaningful
# var can't have space











# ----------------
# VIDEO 15 : Object in Python


string = "hello"
new_string = "hi"










# eg:-



# In Python, all values are stored in objects. You can think that an object is
# like a box that contains information about some value and also stores some
# additional data such as its identity.

# --------------------------------------------------------------------------

# Initially, a variable 'string' points to an object in memory.
# This object has a unique ID and holds the value "hello".

#             id: 4336233024
#            +---------------+
# string --> |    "hello"    |
#            +---------------+


# Now, we assign the 'string' variable to 'new_string'.
# new_string = string

# Both variables now point to the exact same object in memory.
# No new object is created. They share the same ID and value.

#                        id: 4336233024
#                       +---------------+
#      string --------> |    "hello"    |
#                       +---------------+
# new_string ---------> /

# --------------------------------------------------------------------------













# ----------------
# VIDEO 16 : Logical Operation with boolean



# booleans value are either true or false 
qw = True
er = False
# boolean value must start with capital letter

# and
# or
# not

