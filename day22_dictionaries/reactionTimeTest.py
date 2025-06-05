# Reaction Time Test
# Now the user can enter during sleep
# time, i might fix it later via import msvcrt
import time
import random

print("\n-Welcome to the Reaction Time Test 🧪")
time.sleep (2)

print("\n-The rules are you have to press enter right once you see\n\n 'NOW' and I will track your reaction time.")
time.sleep(2)


while True:
    userOption = input("\nAre you ready (Y/N): ").strip().lower()
    if userOption == 'y':
        print("\n-GET READY!!!💨")
        # This will get me a rand float to freeze
        randNum = random.uniform(0.5, 9.5)
        time.sleep(randNum)
        startTime = time.time()
        print("\nNOW!!!🧨")
        
        userReac = input("\nEnter: ")
        endTime = time.time()
        time = endTime - startTime
        message = "That was fasttttttt ⚡⚡⚡" if time <= 0.5 else "SLOWWWWWWWWW 🐢🐢🐢"
        print(f"\nYour reaction time is {time:.5f} {message}\n")
        break
    else:
        print("\nGet ready then!")