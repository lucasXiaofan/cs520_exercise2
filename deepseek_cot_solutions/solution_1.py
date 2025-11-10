"""
Problem 1: Base91 Decode

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: FAILED
Pass Rate: 0/2

Problem Description:
    [BasE91](http://base91.sourceforge.net/) is a method for encoding binary as ASCII characters.
    It is more efficient than Base64 and needs 91 characters to represent the encoded data.

    Create two functions that encode strings to basE91 string and decodes the other way round.

    Examples:
        b91encode('test') = 'fPNKd'
        b91decode('fPNKd') = 'test'
        b91decode('>OwJh>Io0Tv!8PE') = 'Hello World!'
        b91encode('Hello World!') = '>OwJh>Io0Tv!8PE'
"""

def b91decode(strng):
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


def b91encode(strng):
    """Not implemented in CoT solution"""
    raise NotImplementedError("b91encode not implemented")
