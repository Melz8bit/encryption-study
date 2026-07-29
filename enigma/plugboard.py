PLUGBOARD = {
    "A": "B",
    "B": "A",
    "C": "F",
    "F": "C",
    "D": "Z",
    "Z": "D",
    "E": "Q",
    "Q": "E",
    "G": "T",
    "T": "G",
    "H": "Y",
    "Y": "H",
    "I": "X",
    "X": "I",
    "J": "W",
    "W": "J",
    "K": "V",
    "V": "K",
    "L": "U",
    "U": "L",
}


def plugboard(message: str):
    new_message = ""
    for letter in message:
        if letter not in PLUGBOARD:
            new_message += letter
        else:
            new_message += PLUGBOARD[letter]

    # print(new_message)
    return new_message


# plugboard("HELLO")
# plugboard("YQUUO")
