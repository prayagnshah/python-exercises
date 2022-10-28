# Sum of Integers Up To n (integersums.py)

# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

# The function should return 0 if a non-integer is passed in.



def add_it_up(num):

    ##Using try except so that we can also run the error condition as given in above question
    try:
        res = sum(range(num + 1))
    except TypeError:
        res = 0
    return res


add_it_up(int(input('Enter any number:')))

