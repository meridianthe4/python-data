# Q1. Define a function overlapping () that takes two lists and returns True if they have at
# least one member in common, False otherwise.

def overlapping(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False

l1 = [10,52,41,63,85,41,45]
l2 = [4,5,6,7,8,9,1,45]

print(overlapping(l1,l2))

b1 = lambda l1,l2: bool(set(l1) & set(l2))
print(b1(l1, l2))