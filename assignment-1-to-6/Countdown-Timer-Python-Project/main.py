"""
Countdown Timer Python Project with while loop


"""
import time

def countdown(seconds):
    while seconds:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        seconds -= 1 # Decrement the seconds
    print("Time's up!")
    return

seconds = int(input("Enter the number of seconds: "))
countdown(int(seconds))
        

    
