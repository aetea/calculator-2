"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
while True:
    # read input
    print("Please enter an operator and two numbers")
    user_input = input("> ")

    # check if user asked to quit
    if "q" in user_input:
        print("Okay, you are exiting!")
        break

    # otherwise, keep going... #

    # tokenise input
    operator, num1, num2 = user_input.split(" ") 
    num1 = int(num1)
    num2 = int(num2)

    # run various operators
    if operator == "add": 
        print (add(num1, num2))

#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'add':
#                   call the power function with the other two tokens
#             if the first token is 'subtract':
#                   call the power function with the other two tokens
#             if the first token is 'multiply':
#                   call the power function with the other two tokens
#             if the first token is 'divide':
#                   call the power function with the other two tokens
#             if the first token is 'cube':
#                   call the power function with the other two tokens
#             if the first token is 'power':
#                   call the power function with the other two tokens
#             if the first token is 'mod':
#                   call the power function with the other two tokens
#             if the first token is none of these:
#                   return error message
