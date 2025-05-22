# Countdown Timer
import time
import datetime

while True:
    userNum = input("\nHow much time would you like (press 'q' to quit): ").strip().lower()
    if userNum != 'q':
        while not userNum.isdigit():
            print("\nPlease enter a vaild number")
            userNum = input("\nHow much time would you like (press 'q' to quit): ").strip().lower()
        userNum = int(userNum)
        startTime = datetime.datetime.now()
        for timer in range(userNum, 0, -1):
            time.sleep(1)
            print(f"\n{timer}...")            
        print("\nTIME IS UP")
        endTime = datetime.datetime.now()

    
    else:
        break
        
print("\nBye\n")
print(endTime - startTime)