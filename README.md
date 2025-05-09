# section-B
# str.lower()
The str.lower() method in Python is used to convert all the uppercase characters in a string to lowercase. It does not modify any non-alphabetic characters, and the original string remains unchanged since strings are immutable in Python
# str.upper()
The str.upper() method converts all the lowercase characters in a string to uppercase. But, Non-alphabetic characters like numbers, symbols, and spaces remain unchanged.
# str.title()
The str.title() method is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase. This method is particularly useful for formatting strings to resemble titles or headings.
# str.capitalize()
The str.capitalize() method is used to convert the first character of a string to uppercase and all other characters to lowercase. This method is useful when you want to ensure that a string starts with a capital letter while making all other letters lowercase.
# str.swapcase()
The str.swapcase() method is a string method that returns a new string with all the uppercase letters converted to lowercase and all the lowercase letters converted to uppercase. It does not modify the original string but instead creates and returns a new one.v
# str.find()
The str.find() method is used to search for a substring within a string and returns the lowest index where the substring is found. If the substring is not found, it returns -1.
# str.index()
The str.index() method is similar to str.find() it searches for a substring within a string and returns the lowest index where the substring is found. The key difference is that str.index() raises a ValueError if the substring is not found, while str.find() returns -1.
# str.startswith()
The str.startswith() method checks if a string starts with a specified substring (or any of multiple possible prefixes) and returns True or False.
# str.endswith()
The str.endswith() method checks if a string ends with a specified suffix (or any of multiple possible suffixes) and returns True or False. It's the counterpart to str.startswith().
# str.count()
The str.count() method returns the number of times a specified substring appears in a given string. If the the substring in not found, it returns 0.
# str.replace()
The str.replace() method returns a new string where all occurrences of a specified substring are replaced with another substring.
# str.strip()
The strip() method is a built-in string function used to remove leading and trailing whitespace (spaces, tabs, newlines) or specified characters from a string.
# str.lstrip()
The lstrip() method is a string method that returns a copy of the string with leading characters removed from the left side. By default, it removes whitespace characters, but you can specify which characters to remove.
# str.rstrip()
The rstrip() method is a string method that returns a copy of the string with trailing characters removed from the right side. Like lstrip(), it defaults to removing whitespace but can remove specified characters.
# str.split()
The split() method breaks up a string at the specified separator and returns a list of substrings.
# str.join()
The str.join() method is a string method that concatenates (joins together) elements of an iterable (like a list, tuple, or string) with the string acting as a separator between each element.
# str.isalpha()
The str.isalpha() method is a string method that checks if all characters in the string are alphabetic letters and the string contains at least one character.
# str.isdigit()
The str.isdigit() method checks if all characters in a string are digits (0-9) and the string contains at least one character.
# str.isalnum()
The str.isalnum() method checks if all characters in a string are alphanumeric (either letters or numbers) and the string contains at least one character.
# str.isspace()
The str.isspace() method in Python is used to check if a string consists only of whitespace characters. If the string contains only spaces, tabs, newlines, or other whitespace characters, it returns True. Otherwise, it returns False.
# str.format()
The str.format() method is a powerful tool for formatting strings. It allows you to insert values into a string dynamically and control how they are displayed. This method is particularly useful when you want to create more readable or customizable output.
# f-strings
f-strings , introduced in Python 3.6 , are a concise and powerful way to format strings. The "f" stands for "formatted," and they allow you to embed expressions directly inside string literals using curly braces {}. This makes the code more readable and efficient compared to older methods like str.format()
# len()
The len() function in Python is a built-in function that returns the length (number of items) of an object. It works with various data types, such as strings, lists, tuples, dictionaries, sets, and more.
# str.encode()
The str.encode() method is used to convert a string into its byte representation using a specific encoding standard, such as UTF-8, ASCII, or others. This is particularly useful when you need to work with binary data, send data over a network, or save text in a file with a specific encoding.
# str.islower()
The str.islower() method is a built-in string method that checks whether all alphabetic characters in a string are lowercase. It returns True if all the alphabetic characters are lowercase and there is at least one alphabetic character in the string; otherwise, it returns False.
# str.isupper()
The str.isupper() method is a built-in string method that checks whether all alphabetic characters in a string are uppercase. It returns True if all the alphabetic characters are uppercase and there is at least one alphabetic character in the string; otherwise, it returns False.
#       'list'
 a list is a built-in data structure used to store an ordered collection of items.
 # append()
 The append() method is used to add an element to the end of a list. It modifies the original list in place and does not return a new list.
 # clear()
 The clear() method is used to remove all elements from a list, making it empty. It modifies the original list in place and does not return any value (returns None).
# copy()
 The copy() method returns a shallow copy of a list. This means it creates a new list with the same elements as the original, but modifications to the new list do not affect the original list (and vice versa).
# count()
 The count() method returns the number of times a specified element appears in a list.
# extend()
The extend() method is used to add multiple elements (from an iterable) to the end of a list. Unlike append(), which adds a single element, extend() unpacks and adds each element of the iterable individually.
# index()
 The index() method is used to find the first occurrence of a specified value in a list and return its position (index). If the value is not found, it raises a ValueError.
# insert()
 The insert() method is used to add an element at a specific position in a list. Unlike append(), which only adds to the end, insert() allows you to place the element anywhere in the list.
# pop()
 The pop() method is used to remove and return an element from a list at a specified index. If no index is provided, it removes and returns the last element by default.
# remove()
 The remove() method is used to delete the first occurrence of a specified value from a list. Unlike pop(), which removes an item by index, remove() targets the value itself.
# reverse()
 The reverse() method is used to reverse the order of elements in a list in place. This means it modifies the original list and does not return a new list.
# sort()
 The sort() method is used to arrange the elements of a list in ascending or descending order in place (i.e., it modifies the original list). 
#         'Dictionary'
A dictionary is a built-in data structure that stores data in key-value pairs.
# clear()
 The clear() method is used to remove all items (key-value pairs) from a dictionary, making it empty. This modifies the original dictionary in place and returns None.
# copy()
 The copy() method is used to create a shallow copy of a dictionary. This means it creates a new dictionary with the same key-value pairs as the original, but modifying the copy does not affect the original (and vice versa).
# fromkeys()
 The fromkeys() method is a built-in dictionary method that creates a new dictionary with specified keys and a default value for all those keys.
# get()
 The get() method is a safe way to retrieve values from a dictionary without raising a KeyError if the key doesn't exist.
# items()
 The items() method returns a view object that displays a list of a dictionary's key-value pairs as tuples. This is extremely useful for iterating through both keys and values simultaneously.
# keys()
 The keys() method returns a view object that displays a list of all the keys in a dictionary. This is useful when you need to work with just the keys of a dictionary.
# pop()
 The pop() method removes and returns the value associated with a specified key from a dictionary. This is useful when you need to both retrieve and remove an item from a dictionary in one operation.
# popitem()
 The popitem() method is used to remove and return the last inserted key-value pair from a dictionary. 
# setdefault()
 The setdefault() method in Python is used to get the value of a key in a dictionary. If the key doesn't exist, it inserts the key with a specified default value and returns that default value.
# update()
 The update() method is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs. It merges the contents of the provided dictionary or iterable into the existing dictionary.
# values()
 The values() method returns a view object that displays a list of all values in the dictionary. This view object reflects any changes made to the dictionary.
#            'Tuple'
 A tuple is a collection of items or values. Some key differences between a tuple and List are: tuple are created by adding comma separated values inside parentheses () tuple are immutable wherein once values are added to tuple, they can't be changed.
# count()
 The count() method is a built-in tuple method that returns the number of times a specified value appears in the tuple.
# index()
 The index() method is a built-in tuple method that returns the index of the first occurrence of a specified value in the tuple.
 #             'set'
 Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data.
# add()
 The add() method is used to add a single element to a set in Python. Sets are unordered collections of unique elements, and the add() method helps maintain this uniqueness by only adding the element if it doesn't already exist in the set.
# clear()
 The clear() method removes all elements from a set, leaving it empty. This is an in-place operation that modifies the original set rather than creating a new one.
# copy()
 The copy() method creates a shallow copy of a set. This means it returns a new set containing the same elements as the original, but the two sets are independent objects in memory.