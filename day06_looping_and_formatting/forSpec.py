# format specifiers

print("----------------------------------------")

print("Welcome to the format specifiers program")

userNum1 = 1345000.432
userNum2 = 6654000.578
userNum3 = -678000.765
print("----------------------------------------")

print(f"Here is is number rounded {userNum1:.2f}")
print(f"Here is is number rounded {userNum2:.2f}")
print(f"Here is is number rounded {userNum3:.2f}")
print("----------------------------------------")

print(f"Here is num1: {userNum1:015}")
print(f"Here is num2: {userNum2:015}")
print(f"Here is num3: {userNum3:015}")
print("----------------------------------------")

print(f"Here is num1: {userNum1:15}")
print(f"Here is num2: {userNum2:15}")
print(f"Here is num3: {userNum3:15}")
print("----------------------------------------")

print(f"Here is num1: {userNum1: >15}")
print(f"Here is num2: {userNum2:%>15}")
print(f"Here is num3: {userNum3:&>15}")
print("----------------------------------------")

print(f"Here is num1: {userNum1:*<15}")
print(f"Here is num2: {userNum2:*<15}")
print(f"Here is num3: {userNum3:*<15}")
print("----------------------------------------")

print(f"Here is num1: {userNum1:M^15}")
print(f"Here is num2: {userNum2:-^15}")
print(f"Here is num3: {userNum3:#^15}")
print("----------------------------------------")

print(f"Here is num1: {userNum1:+}")
print(f"Here is num2: {userNum2:+}")
print(f"Here is num3: {userNum3:+}")

print("----------------------------------------")
print(f"Here is num1: {userNum1:-}")
print(f"Here is num2: {userNum2:-}")
print(f"Here is num3: {userNum3:-}")
print("----------------------------------------")

print(f"Here is num1: {userNum1: }")
print(f"Here is num2: {userNum2: }")
print(f"Here is num3: {userNum3: }")
print("----------------------------------------")

print(f"Here is num1: {userNum1:@=15}")
print(f"Here is num2: {userNum2:0=15}")
print(f"Here is num3: {userNum3:-=15}")
print("----------------------------------------")

print(f"Here is num1: {userNum1:,}")
print(f"Here is num2: {userNum2:,}")
print(f"Here is num3: {userNum3:,}")
print("----------------------------------------")