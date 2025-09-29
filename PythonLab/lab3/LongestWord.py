# Q.2. Write a function find_longest_word() to find the longest word from the list of words

list1 = ['Mrugank','Vedant','Gajanan','Ganesh','Sayali','Gayatri', 'Shirurkar']

def find_logest_word(lst):
    max = 0
    maxword = None
    for word in lst:
        if len(word) > max:
            max = len(word)
            maxword = word
    return maxword

max_word = lambda lst: max(lst, key = lambda word: len(word))

print(find_logest_word(list1))
print(max_word(list1))