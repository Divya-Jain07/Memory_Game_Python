import random
import math
NUM_PAIRS = 3

def main():
    truth=shuffle_list()
    #print(truth)
    length=len(truth)
    display=[]
    for i in range(length):
        display.append("*")
    #print(display)
    flag=False#to keep track of when all the values are unfolded
    n=len(display)
    while(True):
        display=turn(display,truth,n)
        if display==0:
            break
        if not('*' in display):
            flag=True
            break
    if flag:
        print(display)
        print("Congratulations! You won!")
        
   
#Method to keep track of each turn....
def turn(display,truth,n):
    print(display)
    a=inputs(n,display)
    b=inputs(n,display)
    while(a==b):
        print("You entered the same index twice. Try again.")
        b=inputs(n,display)

    display=check(a,b,truth,display)
    clear_terminal()
    return display
    
    
#To take inputs and also make sure the indices criteria
def inputs(n,display):
    flag=True
    while flag:
        a=input("Enter an index: ")
        flag,a=condition(a,n,display)
    return a
        
    
#to check the index eligibility
def condition(index,n,display):
    try:
        index=int(index)
    except:
        print("Not a number. Try again.")
    # if not(index.isdigit()):
    #     print("Not a number. Try again.")
    else:
        if not(index>=0 and index<=n-1):
            print("Invalid Index. Try again.")            
        elif not(display[index]=='*'):
            print("This number has already been matched. Try again.")
        else:
            return False,index
    return True,index

#to check whether the index given matches in shuffle list if not display the individual value        
def check(a,b,truth,display):
    if(truth[a]==truth[b]):
        display[a]=truth[a]
        display[b]=truth[b]
        print("Match!")
    else:
        print("Value at index",a,"is",truth[a])
        print("Value at index",b,"is",truth[b])
        print("No match. Try again.")
        blank=input("Press Enter to continue...")
        
    return display
        
    
#To create the list for given pairs and then shuffle it      
def shuffle_list():
    truth_list=[]
    key=0
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)
    #print(truth_list)
    random.shuffle(truth_list)
    #print(truth_list)
    return truth_list
    
#to clear the terminal by adding 20 new lines
def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
