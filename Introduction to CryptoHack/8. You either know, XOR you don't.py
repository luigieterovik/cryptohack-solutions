from pwn import xor

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
partial_key = b'crypto{'

partial_flag = bytes([message[i] ^ partial_key[i] for i in range(len(partial_key))])

print(partial_flag.decode("utf-8"))

key = partial_flag + b'y'

flag = xor(key, message)

print(flag.decode("utf-8")) 