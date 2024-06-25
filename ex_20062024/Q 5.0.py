# Count vowels in a String
# WOW indentation so important
# Method 1: usinf for loop
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# call the function
input_string = "Hello, how are you?"
vowel_count = count_vowels(input_string)
print(f"The total number of vowels: {vowel_count}")

# or use filter function - very easy and simple
# Advance example of  - as applied on List, tuple and Set - same results

letters_list = ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'o']
letters_tuple = ('a', 'b', 'c', 'd', 'e', 'i', 'j', 'o')
letters_set = {'a', 'b', 'c', 'd', 'e', 'i', 'j', 'o'}

# filter the vowels
# chat GPT
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # return True if letter in vowels else False # using chatGPT
    return letter in vowels


# a, e, i, o, u
result = filter_vowels('p')
print(result) # false

# Own implenentation using list, tuple, set
# as applied on List, tuple and Set - same results

# now apply filter function - list
vowels_list = filter(filter_vowels, letters_list)
print(list(vowels_list))

# now apply filter function - tuple
vowels_tuple = filter(filter_vowels, letters_tuple)
print(list(vowels_tuple))

# now apply filter function - set
vowels_set = filter(filter_vowels, letters_set)
print(list(vowels_set))

input_string = "Hello, how are you?"
input_string_list = list(input_string)
print(input_string_list)

input_string_tuple = tuple(input_string)
print(input_string_tuple)

input_string_set = set(input_string)
print(input_string_set)