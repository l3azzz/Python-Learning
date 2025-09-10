# control flow statement 

    
















# Video : 1 & 2 & 3 : simple if & else statement & elif statement

x1 = False 
def fun123():

    if  x1 == True : # this means if true OR if x1 == True AND if not x1 true alleal
        print("true aanu") # space is essential
                        # 1 tab = 4 spaces
                           # also nesting is possible

    elif x1 == False: # else if in python is elif  same as if
        print("False aanu")
    else:
        print("Ariyilla")
          # if we don't want else now and just write else and skip it 
          # we want to use pass keyword

#fun123()













# video : 4 : While loop

# if a condition is satified then execute a block of code again and again until the condition is false



def func4 ():
    number4 = 0
    while number4 < 10: 
         number4 += 1
         print(number4)
# this is risky it runs without limit if not defined it may break your system
#func4()



















# video : 5 : For Loop

student = ["basith","ashik","arif","sajid"]
def func5 (items):
    for item in items:
        print(item)

#func5(student)

# to acces differnet types of data structures we use for loop
# list , tuple , set , dictionary , string













# video : 6 : RAnge function


def func6 ():
   # range(10) # it equal to [0,1,2,3,4,5,6,7,8,9] a list with 10 elm
    for number in range(1,17): # it starts from 0 to 16 in numbers
        print(number)

        # if out var don't have use then
        # for _ in range(5): # it will run 5 times
            # print("hello")
#func6()



















# video : 7 : nested loops

names = ["basith","ashik","arif","sajid"]
def func7 (names):
    for name in names:
        for char in name:
            print(char)
        print("\n")
#func7(names)

# it means loop in a loop in a loop.......................















# video : 8 : Loop control statement


def func8 ():
    pets = ["dog","cat","rabbit","goldfish","fish","bird"]
    for pet in pets:
        print(pet)
        if pet == "rabbit":
            continue #continue without including current one
        elif pet == "fish":
            break   # ends the code there
#func8()









# video : 9 : Operation with dictionary

# dictionary = object in javascript

student = {
    "name" : "basith",
    "age" : 21,
    "courses" : ["python","javascript"]
}


#for item in student.keys() :
  #  print(item) # it will print only keys

#for item in student.keys() :
    #print(student[item]) # it will print only values


#for key,value in student.items() :
   # print(key, value)
    
