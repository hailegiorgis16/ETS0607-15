uv_name = "Addis Ababa Science and Technology University" # a code that print out the value
try:
    index = uv_name.index("Ababa")
    print(index)
except ValueError:
    print("substring is not found")

text = "Learning in aastu is so boring" # a code that print out ValueError
try:
    test = text.index("Hope!")
    print(test)
except ValueError:
    print("Error Hope is not found")