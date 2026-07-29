WIRING = [
    "E",
    "K",
    "M",
    "F",
    "L",
    "G",
    "D",
    "Q",
    "V",
    "Z",
    "N",
    "T",
    "O",
    "W",
    "Y",
    "H",
    "X",
    "U",
    "S",
    "P",
    "A",
    "I",
    "B",
    "R",
    "C",
    "J",
]


class Rotor:

    def __init__(self, starting_pos: int):
        self.starting_pos = starting_pos

    def step(self):
        self.starting_pos = (self.starting_pos + 1) % 26

    def encode_letter(self, letter: chr):
        index = ord(letter) - ord("A")
        shifted_index = (index + self.starting_pos) % 26
        wiring_output = chr(
            (ord(WIRING[shifted_index]) - ord("A") - self.starting_pos) % 26 + ord("A")
        )
        return wiring_output

    def decode_letter(self, letter: chr):
        index = ord(letter) - ord("A")
        shifted_index = (index + self.starting_pos) % 26
        shifted_letter = chr(shifted_index + ord("A"))
        wiring_output = chr(
            (WIRING.index(shifted_letter) - self.starting_pos) % 26 + ord("A")
        )
        return wiring_output

    def rotate(self, message: str, is_decode: bool = False):
        message = message.upper()
        rotated_message = ""
        for letter in message:
            if letter.isalpha():
                if not is_decode:
                    rotated_message += self.encode_letter(letter)
                else:
                    rotated_message += self.decode_letter(letter)
                self.step()

        # print(rotated_message)
        return rotated_message


# rotor = Rotor(0)
# rotor.rotate("Hello")

# rotor = Rotor(0)
# rotor.rotate("QFUVO", False)

# rotor = Rotor(0)
# rotor.rotate("A" * 27)
# rotor = Rotor(0)
# rotor.rotate("EJKCHBXJNQDICJKSHDAWGNFUEKE", False)
