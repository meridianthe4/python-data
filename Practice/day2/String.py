s = "Python is Dynamic Language"

is_present = 'Python' in s
print(is_present)

not_present = 'java' not in s
print(not_present)

print("=============================================================================")

'''Indexing'''

print(s[8])
print(s[-8])
print(s[3:10])  # startting from 3 and will not include 10

print(s[-10:-3])

# print(s[40]) will give IndexOutofBond Error

print(s[2:14:2])
print(s[:10])

print("=============================================================================")

s1 = 'helloA'
print(s1.isalpha())

s1 = '1234'
print(s1.isdecimal())

s1 = '12\u0082'
print(s1.isdigit())


print("=============================================================================")

s2 = "Welcome to Python"
print(s2.lower())
print(s2.upper())
print(s2.title())
print(s2.capitalize())
print(s2.swapcase())  #capitial to small and small to capital



print("=============================================================================")

s3 = '        sit bit fit sit chit bit Vedant'
s3=s3.strip()
words = s3.split(' ')
print(words)
print(s3.count('sit'))
s4 = ','.join(words)
print(s4)

partition = s3.partition('Vedant')
print(partition)