username = input("Enter your username(only number and latter)")
if username.isalnum():
    print(f"Hi, {username}")
else:
    print("Please only enter latter and number no other characters")