ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = ""

for ascii in ascii_list:
    flag += chr(ascii)
print(flag)

ascii_list_again = []
for letter in flag:
    ascii_list_again.append(ord(letter))
print(ascii_list_again)