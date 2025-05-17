alphabet = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی۰۱۲۳۴۵۶۷۸۹"

def base42_encode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    num = int.from_bytes(data, 'big')
    if num == 0:
        return alphabet[0]
    enc = ""
    while num > 0:
        enc += alphabet[num % 42]
        num //= 42
    return enc[::-1]

def base42_decode(text):
    num = 0
    for ch in text:
        num = num * 42 + alphabet.index(ch)
    length = (num.bit_length() + 7) // 8
    return num.to_bytes(length, 'big')
