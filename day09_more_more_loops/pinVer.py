# more for loops

accessBool = False

print("\nPIN code verification system\n")
for i in range (0, 4):
    userPIN = input("\nPlease enter a PIN📌: ").strip().lower()
    userPINBool = userPIN.isdigit()
    
    while userPINBool == False:
        print("\nThe PIN must be all digits")
        userPIN = input("\nPlease enter a PIN📌: ").strip().lower()
        userPINBool = userPIN.isdigit()
    userPIN0Occur = userPIN.find('0')
    if userPIN0Occur == 0:
        #print(f"DEBUG: <<-->> {userPIN0Occur}")
        print("\nThe PIN can't start with a 0")
        continue
    userPINlen = len(userPIN)
    if userPINlen < 4:
        #print(f"DEBUG: <<-->> {userPINlen}")
        print("\nThe PIN can't be less than 4 digits")
        continue
    if userPINBool == True:
        print("\nCorrect PIN")
        accessBool = True
        break
    else:
        print("\nInvail PIN")
if accessBool == True:
    print("\nThanks, Have a good day!\n")
else:
    print("\nSorry you used all you attempts\n")