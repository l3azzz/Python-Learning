# Modules and Packages














# video : 1: Load Module

# to add daytime module
# we use import to import module 
import datetime
import math

# if we wanna import a single thing froma  module we from math import sqrt
#print(datetime.date.today())
#print(math.sqrt(16)) # it will give square root of 16
#  for mathematic operation we use math module 

# most used is random choise 









# video : 2 : Math Function


x2 = -10

# i wanna find absolute of x2
#print(abs(x2)) # it will give 10
# like that there are more functions in math module we don't get there now











# video : 3 : Random Module


# very important module used for random things
import random

x3 = random.random()
#print(x3) # it will give random value between 0 to 1

q3 = random.uniform(1,10)
#print(q3) # it will give random value between 1 to 10

w3 = random.randint(1,10)
#print(w3) # it will give random integer value between 1 to 10

list3 = ["apple","banana","mango","grapes"]
#e3 = random.choice(list3) # it will give random value from the list
#
t3 = random.randrange(1,10,2) # it will give random odd value between 1 to 10
#print(t3)

u3 = random.shuffle(list3) # it will shuffle the list
#print(list3)

b3 = random.sample(list3,2) # it will give 2 random value from the list
#print(b3)








# video : 4 : PIP

# third party moudle we can install using pip
# pip is package manager for python

# pip install Django      OR      pip install Django==3.0.5

#  we can see all pkges by pip r.txt creates all pakcarage req file

# pip is a pkg manager in pip we can install , uninstall , upgrade pkgs
# to uninstall pip uninstall pkgname
# to upgrade pip install --upgrade pkgname
# to see all installed pkgs pip list
# to see all outdated pkgs pip list --outdated
# to see details of a pkg pip show pkgname
# to see all pkgs in a file pip freeze > requirements.txt
# to install all pkgs in a file pip install -r requirements.txt
# to uninstall all pkgs in a file pip uninstall -r requirements.txt
# to see all commands pip --help
# to see all commands of a pkg pip show pkgname --help













# video : 5 : Tabnine Plugin


# ______ it was a great tool but discontinued now to the alternative

