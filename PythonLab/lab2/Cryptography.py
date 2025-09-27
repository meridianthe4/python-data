# Q.7 In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a 
# letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, 
# and so on. Create a cipher to represent each key with corresponding value as :

# {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 
# 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}

# encrypted = 'nbrkrq'
# Expected output : decrypted = python


def encrypt(secret, key):
    secret = secret.lower()
    encrypted_list = []
    for ch in secret:    
        ascii_value = ord(ch)
        new_ascii_value = None
        if ascii_value+key>122 :
            new_ascii_value = 97 + (ascii_value + key - 122)
        else:
            new_ascii_value = ascii_value + key
        encrypted_list.append(chr(new_ascii_value))
    return "".join(encrypted_list)




def decrypt(encrypt,key):
    encrypt = encrypt.lower()
    decrypt_list = []
    for ch in encrypt:
        ascii_value = ord(ch)
        new_ascii_value = None
        if ascii_value-key < 97:
            new_ascii_value = 122 - (97 - ascii_value + key )
        else:
            new_ascii_value = ascii_value - key
        decrypt_list.append(chr(new_ascii_value))
    
    return "".join(decrypt_list)


if __name__ == "__main__":
    
    s1 = input("Enter a Secret ")
    key = int(input("Enter a key "))
    enc = encrypt(s1,key)
    print(f"Encrypted message is {enc}" )
    
    dec = decrypt(enc,key)
    print(f"Decrypted message is {dec}" )
