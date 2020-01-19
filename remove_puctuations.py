"""This program removes all punctuations from a string.
 We will check each character of the string using for loop.
 If the character is a punctuation, empty string is assigned to it."""

#define punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
input_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in input_str:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)

