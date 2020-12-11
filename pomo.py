import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

t_now = dt.datetime.now()     # datetime obj
t_pom = 25 * 60  #25 mins pomodoro time   , int, secs
t_delta = dt.timedelta(0, t_pom) # time diff in minutes   , datetime ob  
t_fut = t_now + t_delta  #future time, ending pomodoro , datetime obj 
delta_sec = 5 * 60 # break time, after pomodoro  , int,sec
t_fin = t_now + dt.timedelta(0 , t_pom + delta_sec)  # after break, time restart


#GUI part

#hide main window from tkinter. only need message box

root = tkinter.Tk()
root.withdraw()

messagebox.showinfo("PomoDoro Started! " , "\n It is now "
                    + t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins. " )


#initiliza pomodoro counters
total_pomodoros =  0
breaks = 0


#Main loop

while True:
    #pomo time
    if t_now < t_fut:
        print('pomodoro')
    # it is not past working pomodoro, within the break.
    elif t_fut <= t_now <= t_fin:
        # check if it's  first time here, if so ring a bell 
        print('in break')
        if breaks == 0:
            print('if break')

            for i in range(5):
                winsound.Beep((i+ 100), 700)
            print('Break time!')
            breaks += 1

#  pomo finished. reset breaks
    
    else:
        print('finished')
        # pomo finished. reset breaks
        breaks = 0
        # annoy! > let user know that break is over
        for i in range(10):
            winsound.Beep((i+100) , 500 )
        # ask if user wants to start again.

        usr_ans = messagebox.askyesno(" Restart ? " )
        total_pomodoro += 1
        if usr_ans == True:
            # user wants to restart pomo
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta( 0 , t_pom)
            t_fin = t_now + dt.timedelta( 0, t_pom + delta_sec)
            continue
        elif usr_ans == False:
            # user doesnt want more.
            messagebox.showinfo('Pomodoro Finished!' , '\nYou completed" + str(total_pomodoros) + pomodoros today!")
            break

        #check every 20 seconds and update current time
        print('sleeping')
        time.sleep(20)
        t_now = dt.datetime.now()
        timenow = t_now.strftime("%H:%M")

        
            
            
