# Data Types in Python

# 1. Numbers
# Integer
a = 10
print(type(a), a)  # <class 'int'>

# Float
b = 3.14
print(type(b), b)  # <class 'float'>

# Complex
c = 2 + 3j
print(type(c), c)  # <class 'complex'>

# 2. String
s = "Hello, World!"
print(type(s), s)  # <class 'str'>

# 3. Boolean
flag = True
print(type(flag), flag)  # <class 'bool'>

# 4. List (ordered, mutable, allows duplicates)
lst = [1, 2, 3, "apple", 3.14]
print(type(lst), lst)  # <class 'list'>

# 5. Tuple (ordered, immutable, allows duplicates)
tup = (1, 2, 3, "banana")
print(type(tup), tup)  # <class 'tuple'>

# 6. Set (unordered, mutable, no duplicates)
st = {1, 2, 3, 2, 1}
print(type(st), st)  # <class 'set'>

# 7. Dictionary (key-value pairs, unordered, mutable)
d = {"name": "Alice", "age": 25}
print(type(d), d)  # <class 'dict'>

# 8. NoneType
n = None
print(type(n), n)  # <class 'NoneType'>

# Type Conversion
x = "123"
y = int(x)
print(type(y), y)  # <class 'int'> 123

# Checking types
print(isinstance(a, int))  # True
print(isinstance(s, str))  # True

# More examples
# List of all built-in types: https://docs.python.org/3/library/stdtypes.html

# Bytes
bts = b'hello'
print(type(bts), bts)  # <class 'bytes'>

# Bytearray
ba = bytearray(5)
print(type(ba), ba)  # <class 'bytearray'>

# Range
r = range(5)
print(type(r), list(r))  # <class 'range'> [0, 1, 2, 3, 4]

# Frozenset (immutable set)
fs = frozenset([1, 2, 3])
print(type(fs), fs)  # <class 'frozenset'>

# Memoryview
mv = memoryview(b'abc')
print(type(mv), mv)  # <class 'memoryview'>

val = 4e3
print(type(val), val)  # <class 'float'> 4000.0

val = 4E-3
print(type(val), val)  # <class 'float'> 0.004
print(val)

# for i in range(30):
#     if i == 10:
#         pass
#     else:
#         print(i)

for i in range(5):
    if i == 3:
        continue
    elif  i == 4:
        pass
    else:
        print(i)