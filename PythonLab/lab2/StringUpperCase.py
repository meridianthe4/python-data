# Q. 1. Check if all letters in a string are uppercase

# def check_uppercase(str):
#   return str.isupper()

def check_uppercase(st):
    for ch in st:
        if not 65<=ord(ch)<=97:
            return False
    return True

print(check_uppercase("MRUGANK"))
