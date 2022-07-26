##defining a function


def is_same(t):
    for number in t:  ##storing the data in number and iterating the values
        if number != t[0]:  ##checking the number 1 position
            return False
    return True


print(is_same((45, 45, 45, 45)))
