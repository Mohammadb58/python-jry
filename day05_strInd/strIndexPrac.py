# Secret Message Decoder

print("Welcome to the Secret Message Decoder")

userSecMes1 = input("Please enter your secret message: ")

# remove leading and trailing whitespace
userSecMes = userSecMes1.strip()

first4chars = userSecMes[0:4]
lastChars = userSecMes[-1]
every2Char = userSecMes[0::2]
revStr = userSecMes[::-1]
regStr = userSecMes[0::]


print(f"'{first4chars}' are the first 4 characters")

print(f"'{lastChars}' is the last character")

print(f"'{every2Char}' are every second character")

print(f"'{revStr}' is the message reversed")

print(f"'{regStr}' is your message")
