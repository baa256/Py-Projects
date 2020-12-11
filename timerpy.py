import time

def countdown(t):

    while t:
        mins, secs = divmod(t,60)
        timer = ' {:02d}:{:02d} '.format(mins,secs)
        print(timer, end=  '\r')
        time.sleep(1)
        t -= 1

        print(' Counting Down ! ' )

        if t == 0 :
            print('Count Down Has Finished!' )
            
        

    
            


# input time in secs

t = input(" Enter the time in seconds :  " )

# function call

countdown(int(t))

    
        
        
