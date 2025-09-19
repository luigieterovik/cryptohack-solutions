hex_encoding = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

hex_to_bytes = bytes.fromhex(hex_encoding)
print(hex_to_bytes)

reverse_process = bytes.hex(hex_to_bytes)
print(reverse_process)

print(hex_encoding == reverse_process)