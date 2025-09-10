list = [11,5,17,18,23,50]

def remove(items):
    for item in items:
        if item % 2  == 0:
            list.remove(item)
        else:
            pass
    print(list)


remove(list)