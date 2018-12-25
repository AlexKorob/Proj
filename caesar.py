import string


def encrypt(text_in, step):
    ''' For decrypt text point step with minus '''
    text_out = ''
    text_in = list(text_in.lower())
    alfa = list(string.ascii_lowercase)
    d = {}

    track = 0
    for x, y in enumerate(alfa):
        d[y] = x+step
        if x > len(alfa)-step-1:
            d[y] = track
            track += 1

    for i in text_in:
        if i == ' ':
            text_out += ' '
            continue
        text_out += alfa[d[i]]

    return text_out


step = 2
enc_text = encrypt('How are you doing', step)
dec_text = encrypt(enc_text, -step)
print(enc_text)
print(dec_text)
