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

    def _step(self):
        self.starting_pos = (self.starting_pos + 1) % 26

    def _encode(self, letter: chr):
        index = ord(letter) - ord("A")
        shifted_index = (index + self.starting_pos) % 26
        wiring_output = chr(
            (ord(WIRING[shifted_index]) - ord("A") - self.starting_pos) % 26 + ord("A")
        )
        return wiring_output

    def _decode(self, letter: chr):
        index = ord(letter) - ord("A")
        shifted_index = (index + self.starting_pos) % 26
        shifted_letter = chr(shifted_index + ord("A"))
        wiring_output = chr(
            (WIRING.index(shifted_letter) - self.starting_pos) % 26 + ord("A")
        )
        return wiring_output

    def rotate(self, message: str, is_encode: bool = True):
        message = message.upper()
        rotated_message = ""
        for letter in message:
            if letter.isalpha():
                if is_encode:
                    rotated_message += self._encode(letter)
                else:
                    rotated_message += self._decode(letter)
                self._step()

        print(rotated_message)


rotor = Rotor(0)
rotor.rotate("Hello")

rotor = Rotor(0)
rotor.rotate("QFUVO", False)

rotor = Rotor(0)
rotor.rotate("A" * 27)
rotor = Rotor(0)
rotor.rotate("EJKCHBXJNQDICJKSHDAWGNFUEKE", False)
