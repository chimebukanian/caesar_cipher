#caesar-cipher encryption

txt=input("enter text-")
cipher=''
for char in txt:
    if not char.isalpha():
        continue
    char=char.upper()
    code=ord(char)+1
    if code>ord('Z'):
        code=ord('A')
    cipher+=chr(code)
print(cipher)

#caesar cipher:encrypt by user-defined input
text=input("input text to be encrypted")
shift=0
while shift==0:
    try:
        shift=int(input("crypt by"))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift=0
    if shift==0:
        print('bad shift')
cipher=''
for char in text:
    if char.isalpha():
        code=ord(char)+shift
        if char.isupper():
            first=ord('A')
        else:
            first=ord('a')
        code-=first
        code%=26
        cipher+=chr(first+code)
    else:
        cipher+=char
print(cipher)