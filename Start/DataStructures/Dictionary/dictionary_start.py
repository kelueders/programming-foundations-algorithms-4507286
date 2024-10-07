# Example file for Programming Foundations: Algorithms by Joe Marini
# demonstrate dictionary usage
'''
Keys
Values
Hash Functions 
- maps keys to their associated values using a hash function
- has function uses the key to compute an index into the slots that are in the hash table and map the key to a value
- key-to-value mappings are unique
- typically very fast
- for small datasets, arrays are usually more efficient
- don't always order entries in a predictable way
'''

# TODO: create a dictionary all at once
items1 = dict({"key1" : 1, "key2" : 2, "key3" : 3})
print(items1)


# TODO: create a dictionary progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)


# TODO: replace an item
items2["key2"] = "two"

# TODO: try to access a nonexistent key
# print(items1["key6"])

# TODO: iterate the keys and values in the dictionary
for key, value in items2.items():
  print("Key: ",key, " Value: ",value)