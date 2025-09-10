string = "hello15hi15"


def add(value):
    sum = 0
    for char in value:
    
        if char.isdigit():
            sum += int(char)
       
    print(sum)

add(string)


