string_encoded = "label"
integer_to_xor = 13

flag = ""

for char in string_encoded:
    char_to_unicode_integer = ord(char)
    xored_char = char_to_unicode_integer ^ integer_to_xor
    xored_integer_to_char = chr(xored_char)
    flag += xored_integer_to_char
print(flag)

