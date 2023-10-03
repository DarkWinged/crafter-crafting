from app.protected_list import PList

original_list = [1, 2, 3]
protected_list = PList(original_list)

# Modifying elements
protected_list[1] = 5
protected_list.append(4)
protected_list.extend([6, 7])

# Original list is still uncurrent
print("\nBefore update:")
print("original_list", original_list)  # Output: [1, 2, 3]
print("protected_list", protected_list)  # Output: [1, 5, 3, 4, 6, 7]

# Applying the changes using the update method
protected_list.update()

# Now the original list reflects the changes
print("\nAfter update:")
print("original_list", original_list)  # Output: [1, 5, 3, 4, 6, 7]
print("protected_list", protected_list)  # Output: [1, 5, 3, 4, 6, 7]

# Further modifications after updating
print("\nFurther modifications:")
protected_list.append(8)
protected_list[2] = 9

# Print the state of the protected_list and original_list
print("\nBefore reset:")
print("protected_list", protected_list) # Output: [1, 5, 9, 4, 6, 7, 8]
print("original_list", original_list) # Output: [1, 5, 3, 4, 6, 7]

# Resetting the changes
protected_list.reset()

# The changes are discarded, and the protected_list is reset to the original state
print("\nAfter reset:")
print("protected_list", protected_list) # Output: [1, 5, 3, 4, 6, 7]
print("original_list", original_list) # Output: [1, 5, 3, 4, 6, 7]

protected_list.current = [11, 12, 13]

print("\nBefore update:")
print("original_list", original_list)  # Output: [1, 5, 3, 4, 6, 7]
print("protected_list", protected_list)  # Output: [11, 12, 13]
protected_list.update()
print("\nAfter update:")
print("original_list", original_list)  # Output: [11, 12, 13]
print("protected_list", protected_list)  # Output: [11, 12, 13]


protected_list.current = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print("\nBefore update:")
print("original_list", original_list)  # Output: [11, 12, 13]
print("protected_list", protected_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
protected_list.update()
print("\nAfter update:")
print("original_list", original_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("protected_list", protected_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
