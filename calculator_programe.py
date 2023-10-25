# Create a list
my_list = [1, 2, 3, 4, 5]

# Access elements by index
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modify elements
my_list[2] = 10

# Add elements to the end of the list
my_list.append(6)

# Insert an element at a specific position
my_list.insert(1, 7)

# Remove an element by value
my_list.remove(4)

# Remove an element by index
del my_list[3]

# Find the index of an element
index = my_list.index(5)
print("Index of 5:", index)

# Check if an element is in the list
if 3 in my_list:
    print("3 is in the list")

# Get the length of the list
length = len(my_list)
print("Length of the list:", length)

# Iterate through the list using a for loop
print("Elements in the list:")
for item in my_list:
    print(item)

# Sort the list in ascending order
my_list.sort()

# Reverse the list
my_list.reverse()

# Copy the list
copy_list = my_list.copy()

# Clear all elements from the list
my_list.clear()

# Print the modified list
print("Modified List:", my_list)