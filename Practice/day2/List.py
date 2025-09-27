words = ['pat','bat','mat','sat','rat','cat','fat']

print("=============================================================================")
for item in words:
    print(item , end=" ")

print('')
print('fat' in words)
print('fit' not in words)


print("=============================================================================")

print(words[5])
print(words[-5])
print(words[1:6])
print(words[-6:-1])
print(words[-1:-6:-1])

print(words[:4]+ words[4:])