"""Solutions for problem_0 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

def b91decode_deepseek_cot(strng):
    b = 0
    n = 0
    out = []
    for c in strng:
        if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"':
            continue
        v = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'.index(c)
        if v < 0:
            continue
        b |= v * (1 << n)
        n += 7
        if n > 7:
            out.append(b & 255)
            b >>= 8
            n -= 8
    if n > 0:
        out.append(b & 255)
    return ''.join(map(chr, out))


# ========== GEMINI_SELF_PLANNING ==========

def b91decode_gemini_self_planning(strng):
    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'
    decoded = bytearray()
    value = 0
    bits = 0

    for char in strng:
        index = charset.find(char)
        if index == -1:
            continue
        value += index * (91 ** bits)
        bits += 1

        if bits == 2:
            decoded.append(value & 0xFF)
            decoded.append((value >> 8) & 0xFF)
            value = 0
            bits = 0

    if bits != 0:
        decoded.append(value & 0xFF)

    return decoded.decode('utf-8', 'ignore')


def b91encode(strng):
    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'
    encoded = ''
    value = 0
    bits = 0

    for byte in strng.encode('utf-8'):
        value |= (byte << bits)
        bits += 8

        while bits > 13:
            index = value % 91
            encoded += charset[index]
            value //= 91
            bits -= 13

    if bits > 0:
        encoded += charset[value]

    return encoded

