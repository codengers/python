"""
string shift by two steps
Interview question
provide string and integer times to shift
"""


def string_shift(word_str, bit):
    shfited_str = ''
    for s in word_str:
        shfited_str += chr(ord(s) + int(bit))
    return shfited_str


input_str = input("Please enter string: ")

print(input_str, string_shift(input_str, 2), end="")
