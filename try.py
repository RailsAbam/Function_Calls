
#Recursion
def Countdown(n): 
    if n <= 0: 
        print("BlastOff")
    else: 
        print(n) 
        Countdown(n-1)
Countdown(3)

def print_n(s, n): 
    if n <= 0: 
        return
    print(s) 
    print_n(s, n -1)
   
    
    
    