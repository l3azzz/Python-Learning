# OBJECT ORIENTED PROGRAMMING 














# video 1 : class


# to define class 
class MyClass: # in class there are properties and metods
    first_name = "Basith"
    last_name = "A S"
    student_class = 1
    division = "C"

    def full_name(self) : # in js it was this in python this was self
        return f"{self.first_name} {self.last_name}"


# u know class is a blueprint and can be duplicated /


student1 = MyClass()
#print(student1.first_name)

# we discused the skeleton right 




















# video 2 : Class Instances



# constructor = def __init__(self):

class MyClass2: 
    def __init__(self, first_name, last_name, student_class, division):  # we created instance
        self.first_name = first_name
        self.last_name = last_name
        self.student_class = student_class
        self.division = division

    def full_name(self) :
        return f"{self.first_name} {self.last_name}"


newClass = MyClass2("basith","a s", 10, "CCC")
#print(newClass.full_name())













# video 3 : class VS instance

# instance can be created again agin with differnet keys 
# but classes can't


















# video 4 : Inheritance 


class Animal1:
    def __init__(self,name):
        self.name = name
    # def full_name(self):
    #     return f'{self.name} {"hello world"}'


class Dog1(Animal1):
    pass

dog = Dog1("lab")

#print(dog.name)











# video 5 : method overriding


class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def full_name(self):
        return f'{self.name} {self.breed}'

class Dog(Animal):
    def full_name(self):
        return "Hello"
    

dog = Dog("Luke", "lab")


# we can use super().blabl to call the first parwent of the thign his is extending