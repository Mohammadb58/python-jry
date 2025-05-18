# Final while loop 

print("----------------------------------")

userPass1 = input("What do you think the password is: ")

userPass2 = userPass1.strip()
userPass3 = userPass2.lower()

if not userPass3 == "league":
    print("❌ Wrong, you got 2 attempts left")
    userPass4 = input("What do you think the password is: ")
    
    if not userPass4 == "league":
        print("❌ Wrong, you got 1 attempts left")
        userPass5 = input("What do you think the password is: ")
        
        if not userPass5 == "league":
            print("❌ Wrong, Access Denied")
            
        else:
            print("✅ Wow, you got it")
    
    else:
        print("✅ Wow, you got it")
              
else: 
    print("✅ Wow, you got it")



"""while not userPass3 == "league":
    print(f"{userPass3} <---")
    print("❌ Wrong, you got 2 attempts left")
    userPass3 = input("What do you think the password is: ")
    print("❌ Wrong, you got 1 attempt left")
    userPass3 = input("What do you think the password is: ")
    
"""
