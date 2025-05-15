# Account Access System practicing conditional expressions

print("Account Access System")

userRole = input("What is your role (admin/guest): ")

if userRole == "admin":
    userCode = int(input("What is your password: "))
    # Since we typecasting the userCode to an int I must cmp to an int rather "6066". 
    access = "Access" if userCode == 6066 else "Access denied"
    print(access)
elif userRole == "guest":
    print("Limited Access")
else:
    print("Sorry access denied.")