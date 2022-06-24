# dict can have any type as key like number, boolean ,string anything (but not list)

# Dictionary Methods Cheat Sheet
# Definition

# x = {key1:value1, key2:value2} 

# Operations

# len(dictionary) - Returns the number of items in the dictionary

# for key in dictionary - Iterates over each key in the dictionary

# for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary

# if key in dictionary - Checks whether the key is in the dictionary

# dictionary[key] - Accesses the item with key key of the dictionary

# dictionary[key] = value - Sets the value associated with key

# del dictionary[key] - Removes the item with key key from the dictionary

# Methods

# dict.get(key, default) - Returns the element corresponding to key, or default if it's not present

# dict.keys() - Returns a sequence containing the keys in the dictionary

# dict.values() - Returns a sequence containing the values in the dictionary

# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.

# dict.clear() - Removes all the items of the dictionary.


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)


# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for key,values in group_dictionary.items():
		# Now go through the users in the group
		for value in values:
			print(value)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))