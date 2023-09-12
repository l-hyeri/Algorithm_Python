"""
입력 : S (문자열)
출력 : ROT13으로 암호화한 내용 출력
"""

S = input()
blank = ''

for i in range(len(S)):
    if S[i] == '' or ord(S[i]) < ord('A'):
        blank += S[i]

    else:
        if ord(S[i]) + 13 > 122:
            blank += chr(96 + (ord(S[i]) + 13) - 122)
        elif ord(S[i]) + 13 > 90 and ord(S[i]) < 91:
            blank += chr(64 + (ord(S[i]) + 13) - 90)
        else:
            blank += chr(ord(S[i]) + 13)

print(blank)