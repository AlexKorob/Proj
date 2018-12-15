import string

alfa = list(string.ascii_lowercase)
n = 2
d = {}

for x,y in enumerate(alfa):
    d[x+1] = y

text_in = 'Hello Kitty'
text_out = text_in
print(d)
for i in range(len(text_in)):
    text_out[i] = d[i+1]

print(text_out)