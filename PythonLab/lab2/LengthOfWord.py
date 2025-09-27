# Q.3.  Write a Python function that takes a list of words and returns the length of the longest one

def longest_word(words):
    max = 0
    for word in words:
        if len(word) > max:
            max = len(word)
    return max

words = ["Hello", "world", "Helsinki", "Oslo", "Manila", "Copenhagen"]
print(longest_word(words))
