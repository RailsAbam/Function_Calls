def new_line():  #The function new_line will print 1 period
    print('.')

def three_lines():  #The function three_lines will print new_line 3 times(3 periods)
    new_line()
    new_line()
    new_line()
    
def nine_lines():  #The function nine_lines will print three_lines 3 times (9 periods)
    three_lines()
    three_lines()
    three_lines()
    

def clear_screen(): 
    print("Here are 9 lines.") #This line is where the program will start its execution. 
    nine_lines()   #I want to let you know how many lines im printing with a string 
    print("Here are 25 more lines.")
    nine_lines()
    nine_lines()          #I added the lines together so they equate to 25 = 9 + 9 + 3 + 3 + 1
    three_lines()
    three_lines()
    new_line()


clear_screen() #This is where I call the function to begin


