def caesar(message: str, shift: int, is_encode: int):
    encoded_str = ""
    for letter in message:

        if letter.isalpha():
            base = ord("A") if letter.isupper() else ord("a")
            encoded_str += chr(
                (ord(letter) - base + (int(shift) * is_encode)) % 26 + int(base)
            )
        else:
            encoded_str += letter

    print(f"Encoded message: {encoded_str}")


encode_decode = input("Encode or Decode? ")
msg = input("Enter the message: ")
shift = input("Enter shift amount: ")

(caesar(msg, shift, 1) if encode_decode.lower() == "encode" else caesar(msg, shift, -1))
