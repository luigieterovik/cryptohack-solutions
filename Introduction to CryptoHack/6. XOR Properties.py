from pwn import xor

# Se na expressão aparece duas vezes o mesmo termo → ele some.
# Exemplo:
# F ^ A ^ B ^ A = F ^ (A ^ A) ^ B = F ^ 0 ^ B = F ^ B

# por isso KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e é irrelevante para a equação, pois já sabemos o valor de A.

A = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
B = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
C = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

flag_bytes = xor(A, xor(B, C))
flag_hex = flag_bytes.hex()
flag_decoded = flag_bytes.decode("utf-8")


print(flag_decoded)