def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print("Printing 9 lines")
nine_lines()

print("Printing 25 lines")
clear_screen()
