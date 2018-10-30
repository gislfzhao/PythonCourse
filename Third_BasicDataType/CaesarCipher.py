# Caesar Cipher
code = input()
cc_code = ""
for ch in code:
    if 'a' <= ch <= 'z':
        cc_code += chr(ord('a') + (ord(ch) - ord('a') + 3) % 26)
    elif 'A' <= ch <= 'Z':
        cc_code += chr(ord('A') + (ord(ch) - ord('A') + 3) % 26)
    else:
        cc_code += ch
print(cc_code)
