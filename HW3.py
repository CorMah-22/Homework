# 13. Create a dictionary with at least 5 values of different data types
dict1 = {
    "maker": "toyota",
    "model": "crown",
    "year": 2015,
    "suv": False,
    "milage": 31
    
}

#   - Print out 1 value
print(dict1["year"])

#   - Replace any one value in your dictionary with your name
dict1["name"] = "Mahfoud"
print(dict1)

#   - Add your favorite color to the dictionary
dict1["favorite_color"] = "green"
print(dict1)

#   - Add a list, tuple or set to your dictionary
dict1["list1"] = [10, 20, 30]
print(dict1)

#   - Print a list of the dictionary keys
print(list(dict1.keys()))

#   - Print a list of the dictionary values
print(list(dict1.values()))

#   - Copy your 1st dictionary into a 2nd dictionary
dict2 = dict1.copy()
print(dict2)

#   - Pop an item from the 2nd dictionary, and print the dictionary
popped_item = dict2.pop("year")
print(popped_item)
print(dict2)

#   - Remove all the elements from the 2nd dictionary and print the result
dict2.clear()
print(dict2)