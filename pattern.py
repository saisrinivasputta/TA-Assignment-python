# question 1
def pattern():
    
    ASCIIVALUE=65
    for i in range(0, 5):  
        for j in range(0, i + 1):  
           
           character = chr(ASCIIVALUE)  #chr()function returns the character that rep. unicode.
           print(character, end=" ")  
           ASCIIVALUE += 1  
        print() # to print in the new line 


def pattern2():
    n=5 
    
    k = 2*n - 2  # k represents number of spaces
 
    
    for i in range(0, n):   # n number of rows
     
        
        for j in range(0, k):
            print("",end=" ")
     
        
        k = k - 2 # decreasing space after every loop 
     
        
        for j in range(0, i+1):
         
            
            print("* ", end="") # printing *
     
        
        print("\r") # ending line
pattern2()

pattern()
