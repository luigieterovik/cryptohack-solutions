import base64

hex_encoded = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
hex_to_bytes = bytes.fromhex(hex_encoded)
print(hex_to_bytes)

bytes_to_base64 = base64.b64encode(hex_to_bytes)
print(bytes_to_base64)