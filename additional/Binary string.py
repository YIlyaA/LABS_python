binary_string = input()
text = ''.join([chr(int(byte, 2)) for byte in binary_string.split(' ')])  # convert binary string into ASCII symbols

print(text)
