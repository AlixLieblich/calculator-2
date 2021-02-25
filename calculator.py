"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("Enter a calculation >  ")
    tokens = user_input.split(' ')
    if tokens[0] == 'q':
        print("Goodbye!")
        break
    elif tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))    
    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '/':
        print(divide(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == 'square':
        print(square(float(tokens[1])))
    elif tokens[0] == 'power':
        print(power(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))
    elif tokens[0] == 'mod':
        print(mod(float(tokens[1]), float(tokens[2])))
    else:
        print("""
        Allowed operators are: +, -, *, /, square, power, cube, mod. 

        Enter in the format: '* 4 5' 

        If you are done, enter q.
        """)

    