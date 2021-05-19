# define the  function code to print one blank line
def new_line():
    print('.')

# define the function code to print 3 blank lines
def three_lines():
    new_line()
    new_line()
    new_line()

# define the function code to print 9 blank lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# define the funciton code that will print 25 blank lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# use this code to print nine lines to console
print("Printing nine lines")
nine_lines()
# use this code to Print 25 lines to console
print("Calling clearScreen()")
clear_screen()


                                 # References
# In Python what is the “main section which calls the functions”? (2019, February 19). Stack Overflow.
# https://stackoverflow.com/questions/54763824/in-python-what-is-the-main-section-which-calls-the-functions
