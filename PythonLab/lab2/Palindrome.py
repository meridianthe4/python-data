# Q. 2. Write a version of a palindrome recognizer that also accepts phrase palindromes such as :
# Was it a rat I saw? or Dammit, I'm mad!
# Note that punctuation, capitalization, and spacing are usually ignored.

# Was it a rat I saw?
# was it a rat I saw?
# wasitaratisaw

# st = "Was it a rat I saw?"
st = "Dammit, I'm mad!"
st = st.lower()
st = st.strip()
chlist = []
for ch in st:
    if ch.isalpha():
        chlist.append(ch)
st = "".join(chlist)
print(st)

if st == st[::-1] :
    print("Palindrome")
else:
    print("Not Palindrome")