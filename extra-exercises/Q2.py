# Write a python program that takes as an input, two numbers.
# The program only accepts numbers that are greater than 0.
# The program adds the two numbers. It asks the user to guess the result of the addition.
# If their guess is correct a message is printed (your answer is correct), otherwise it prints (your answer is incorrect).
# Then the program asks the user if they want to continue the app with a new question (use a loop for this).
# The loop ruminates when the user answers (no).
# The program also prints the number of questions have been asked in the attempts.


count = 0


def sum_answer():

    global count
    count += 1

    # Asking the user to enter number 1
    num_1 = int(input("Enter the first number: "))
    # Asking the user to enter number 2
    num_2 = int(input('Enter the second number: '))

    # Asking the user to enter the answer
    answer = int(input("What is the answer? "))

    # Using if-else statement to check whether the answer of the user is right or wrong

    if answer == num_1 + num_2:
        print("Your answer is correct.")

    else:
        print("Your answer is incorrect.")

    # Asking user if they want to try again

    ask = str(input("Do you want to try again (yes/no): "))

    # if the user say yes then we can run the loop again

    if ask == 'yes':
        print(sum_answer())

    return ('The number of attempts is:', count)


sum_1 = print(sum_answer())  # Calling the function
