REFLECTOR = [
    "Y",
    "R",
    "U",
    "H",
    "Q",
    "S",
    "L",
    "D",
    "P",
    "X",
    "N",
    "G",
    "O",
    "K",
    "M",
    "I",
    "E",
    "B",
    "F",
    "Z",
    "C",
    "W",
    "V",
    "J",
    "A",
    "T",
]


def reflector(message: str):
    new_message = ""
    for letter in message:
        index = ord(letter) - ord("A")
        new_message += REFLECTOR[index]

    # print(new_message)
    return new_message


# reflector("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
