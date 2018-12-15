import string


alfa = list(string.ascii_lowercase)
d = {}

step = 2

track = 0
for x, y in enumerate(alfa):
    d[y] = x+step
    if x > len(alfa)-step-1:
        d[y] = track
        track += 1

text_out = ''
text_in = list('How are you doing'.lower())

for i in text_in:
    if i == ' ':
        text_out += ' '
        continue
    text_out += alfa[d[i]]

print(text_out)
