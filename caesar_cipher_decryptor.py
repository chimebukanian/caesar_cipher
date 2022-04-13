#caesar cipher:decrypt
text=input("cryptogram-")
decipher=''
for char in text:
    if not char.isalpha():
        continue
    char=char.upper()
    code=ord(char)-1
    if code<ord('A'):
        code=ord('Z')
    decipher+=chr(code)
print(decipher)
