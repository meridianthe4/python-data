# Q.4. Write a Python program to remove duplicates from a list

# Approach 1
duplicate_list = [45, 37, 68, 23, 19, 67, 23, 49, 61, 67, 37]
st = set(duplicate_list)
lst = list(st)
print(lst)

# Approach 2
duplicate_list = [45, 37, 68, 23, 19, 67, 23, 49, 61, 67, 37]
updated_list = []
for num in duplicate_list:
    if num not in updated_list:
        updated_list.append(num)
print(updated_list)
    