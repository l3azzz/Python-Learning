# --collections-- untag code to run














# Video : 1 : Introduction To List 

# what is collection : sometimes we need to get  a data related to that more easily
# so we use list 

list_1 = [1,2,3,4,5]
list_1_string = ["hello","world"]
#print(list_1 , list_1_string)

# but
aaa = list("Hello") # the string is iterable that's why h , e , l , l , o
#print(aaa)


# bbb = list(500) we'll get error it isn't iterable bcuz it's an integer
# print(bbb)















# Video : 2 : Index


# list is ordered using position(index)
# it usually start from 0       list[0]


list_2 = [1,2,3,4,5,6,7,8,9]
#print(list_2[3])

# error like out-of-range
# if -1 then it goes from last to first















# Video : 3 : Slicing


# we can up some list 

list_3 = [1,2,3,4,5,6,7,8,9,10]
#print(list_3[2:5]) # start on index 2 and displays until i reaches index 5
#print(list_3[2:1000])
#print(list_3[2:5:2]) #| start | end | step |













# Video : 4 : List Operation - Adding new elements

list_4 = [1,2,3,4,5,6,7,8,9,10]
list_4a = [11,12,13,14,15]

# adding element
list_4.append(11)
#print(list_4)  # Now prints the updated list

# merging 
list_4.extend(list_4a)
#print(list_4)  # Now prints the merged list















# Video : 5 : list Operation - Removing elements

list_5 = [1,2,3,4,5,6,7,8,9,10]
list_5a = [11,12,13,14,15]

list_5.remove(10) #deletes using content
del list_5[4] # deletes using index
removed_elm = list_5.pop()  # del last eleement and stores in var aslo we can use index in it
#print(list_5)
















# Video : 6 : list Operation - insert and find items

l6 = [1,2,3,4,5,6,1,7,8,9,10,1]

l6.insert(2,100) # add 100 to second index
#print(l6)

#print(5 in l6)

z6 = l6.index(1,5,8) #find index of 1 between 5 and seven 

#print(z6)


















# Video : 7 : Nested List 


# what is nested list
# a list iin a list in a list in a list like that

a7 = [1,2,3,4,5]
b7 = [6,7,8,9,10]
c7 = [11,12,13,14,15]

a7.append(b7)
#print(a7)
# c7[5][3] 5 il 3


















# Video : 8 : Creating Dictionary

# object = dictionary 

student = {
    "name" :"Basith",
    "class" : 8,
    "division" :"A",
}

#print(student["class"]) # print something in that
student["marks"] = [10,20] # adding new key with data as list
#print(student)

# key should never be repeated



















# Video : 9 : Dictionary Operations - adding and retrieving data

student1 = {
    "name" : "basith" ,
    "class" : 8
}

# let create dictionary

dict8 = {'mark': [10,20,222]}
student1.update(dict8)
#print(student1)
#  t o retrieve we use get 



















# Video : 10 : dictionary operations - removing items

student10 = {
    "name" : "basith" ,
    "class" : 8,
    "division" : "A"
}


deleted10 = student10.pop("name") # by this we can remove anything by it's key
# to remove with the last one
student10.popitem()
# we can also use delete as needed
# we can fully empty by using .clear() even copied also deletes it resets
#print(student10)




















# Video : 11 : Tuple

# same as list but can't alter and immuable  after created then we can't update like constants
# how does it look :)

tuple1 = ("Cat", "Dog") # bracket is the symbol of tuple commas msut
#print(type(tuple1))

# we can use tuple function to creae tuple for eg tuple("hello",)



















# Video : 12 : Tuple Operators

tuple2 = (1,2,3)
tuple2a = (4,5,6)
print(tuple2 + tuple2a)
print(tuple2 * 3)
print(tuple2.index(1))
print(tuple2.count(1))


names = ("a", "b")
student11 = {}
student11[names] = "hello"
print(student11)

