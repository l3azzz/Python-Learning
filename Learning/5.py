# python - functions


















# Video : 1 : Introoduction


# we use functions to simplify our code

# to create function we use def keyword 

def greet(): # instead we use : and put 4 spaces for indentation
    print("Hello")
    print("Good Morning")
    
#greet() # calling the function
#greet() # calling the function


def add(a,b):
    return a +b


z1 = add(2,3)# returned value is int  z1
#print(z1)


















# Video : 2 : Scopes

# what is scope ? global and local

a2 = "hello" # this is aa global scope available in entire program
def func11():
    a2 = "hi" # local variable
    print(a2)
    # in here a2 is local var local scope


    
















# Video : 3 : Arguments

def func333(x,y): # in here x and y are parameters
    return x + y

z333 = func333(2,3) # 2 and 3 are arguments and stored in z333  --positional argument
#print(z333)
z333 = func333(y=20, x=30) # or this is much btr bcuz we define we don't mess up  --keyword argument
#print(z333)

# don't put space before and after of argument =



    
















# Video : 4 : Defaul arguments

def add444(y,z=0): # here z has default value 0 optional and these default argument shuld be on the end
    return z + y  # even though we are passing arguments



    
















# Video : 5 : Args


# what is args

def hi5 (x,y,*args ):
    print(args)
    return "hello"

#print(hi5(2,5,10,10,20)) # see extra values are on args and args only accept  arguments


    
















# Video : 6 : Kwrgs

def hi6 (a,b,**kwargs): #kwargs mean keywords arguments
    print(kwargs)
    return "hi"

print(hi6(10,10,hi=11,hello=67)) # passes in dictionary and it accept keywords arguments 
