def atbash(message: str):
    encoded_str = ""
    for letter in message:
        if letter.isalpha():
            base = ord("a") if ord(letter) >= 97 else ord("A")
            encoded_str += chr((2 * base) + 25 - ord(letter))
        else:
            encoded_str += letter

    print(encoded_str)


message = input("Enter message: ")
atbash(message)
