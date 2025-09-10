list = [5,10,20,5]

def add(items):
    total = 0
    for item in items:
        total += item
    
    print(total)

add(list)


# wrong correct

total = sum(list)