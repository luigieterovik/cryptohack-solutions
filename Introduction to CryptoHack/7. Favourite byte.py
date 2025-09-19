from pwn import xor

encoded_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
message_to_bytes = bytes.fromhex(encoded_hex)

flag = None

for i in range(256):
    key = bytes([i])
    xored = xor(message_to_bytes, key)

    if xored.startswith(b"crypto{"):
        flag = xored.decode("utf-8")
        break
        
print(flag)


# More performatic solution:
#
# message = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
# first_char = ord('c')
# key = message[0] ^ first_char

# flag = bytearray()

# for c in message:
#     flag.append(c ^ key)
    
# print(flag.decode("utf-8"))