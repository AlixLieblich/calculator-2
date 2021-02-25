"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("Enter a calculation >  ")
    tokens = user_input.split(' ')
    operator = tokens[0]
    if tokens[0] == 'q':
        print("Goodbye!")
        break
    if len(tokens) < 2:
        print("Not enough inputs.")
    if len(tokens) == 2 or len(tokens) == 3:
        num1 = float(tokens[1])
    if len(tokens) == 3:
        num2 = float(tokens[2])
    if len(tokens) > 3:
        print("Too many inputs.")



    if operator == '+':
        print(add(num1, num2))
    elif operator == '-':
        print(subtract(num1, num2))    
    elif operator == '*':
        print(multiply(num1, num2))
    elif operator == '/':
        print(divide(num1, num2))
    elif operator == 'square':
        if len(tokens) > 2:
            print("Too many inputs.")
        else:
            print(square(num1))
    elif operator == 'power':
        print(power(num1, num2))
    elif operator == 'cube':
        if len(tokens) > 2:
            print("Too many inputs.")
        else:
            print(cube(num1))
    elif operator == 'mod':
        print(mod(num1, num2))
    else:
        print("""
        Allowed operators are: +, -, *, /, square, power, cube, mod. 

        Enter in the format: '* 4 5' 

        If you are done, enter q.
        """)

    