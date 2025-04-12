text = input("Enter a valid input to get valid")
if text.isspace():
    print(f"valid input, {text}")
else:
    print("invalid") # a code that return valid for input like " "
## second example
dash = "    "
print(dash.isspace()) # returns True value since there is a nothing 