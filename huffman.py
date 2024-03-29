# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return {char: s.count(char) for char in s}.items()

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len(freqs) <= 1:
        return
    if len(s) == 0:
        return ''

    encode.cipher = {char[0]: '' for char in freqs}
    sorted_freq = sorted(freqs, key=lambda x: x[1])
    find_cipher(sorted_freq)
    result = ""
    for c in s:
        result += encode.cipher[c]
    return result


def find_cipher(freqs):
    if len(freqs) <= 1:
        return
    new_node = freqs.pop(0)
    new_node2 = freqs.pop(0)
    for c in new_node[0]:
        encode.cipher[c] = '1' + encode.cipher[c]
    for c in new_node2[0]:
        encode.cipher[c] = '0' + encode.cipher[c]

    insert_node = [new_node[0] + new_node2[0], new_node[1] + new_node2[1]]
    insert_point = 0
    for i in range(len(freqs)):
        if insert_node[1] > freqs[i][1]:
            insert_point = i+1
    freqs.insert(insert_point, insert_node)
    find_cipher(freqs)


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    if len(freqs) <= 1:
        return
    if len(bits) == 0:
        return ''
    decode.cipher = dict((v, k) for k, v in encode.cipher.items())
    result = ""
    symbol = ""
    for c in bits:
        symbol += c
        decoded_symbol = decode.cipher.get(symbol, "")
        if decoded_symbol != "":
            result += decoded_symbol
            symbol = ""

    return result


str1 = "5"
freq = [('D', 8), ('B', 8), ('T', 8), ('C', 8), ('P', 8), ('m', 8), ('M', 8), ('O', 8), ('l', 8), ('S', 8), ('A', 8), ('L', 8), ('j', 8), ('r', 8), ('x', 8), ('5', 8)]
encoded = encode(freq, str1)
print(encoded)
decoded = decode(freq, encoded)
print(decoded)