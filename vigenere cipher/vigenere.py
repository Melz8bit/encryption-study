def vigenere(message: str, key: str, is_encode: str):
    is_encode = 1 if is_encode.lower() == "encode" else -1
    encoded_str = ""
    for i, letter in enumerate(message):
        if letter.isalpha():
            key_index = i % len(key)
            shift = ord(key[key_index].lower()) - ord("a")
            base = ord("A") if letter.isupper() else ord("a")

            encoded_str += chr(
                (ord(letter) - base + (shift * int(is_encode))) % 26 + int(base)
            )
        else:
            encoded_str += letter

    print(f"Encoded message: {encoded_str}")


message = input("Enter the message: ")
key = input("Enter the key: ")
is_encode = input("Encode or Decode? ")
vigenere(message, key, is_encode)
