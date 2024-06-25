# Advance example of  - as applied on List, tuple and Set - same results
# To be used in API and Automation testing

letters_list = ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'o']
letters_tuple = ('a', 'b', 'c', 'd', 'e', 'i', 'j', 'o')
letters_set = {'a', 'b', 'c', 'd', 'e', 'i', 'j', 'o'}

# filter the vowels
# chatGPT
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # return True if letter in vowels else False
    return letter in vowels


# a, e, i, o, u
result = filter_vowels('p')
print(result) # false

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


