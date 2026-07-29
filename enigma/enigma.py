from rotor import Rotor
from plugboard import plugboard
from reflector import reflector

"""
Enigma Signal Path:
1. Plugboard
2. Rotor 1
3. Rotor 2
4. Rotor 3
5. Reflector
6. Rotor 3
7. Rotor 2
8. Rotor 1
9. Plugboard
10. Output
"""


def enigma(message: str, rotor_positions: tuple):
    rotor_1 = Rotor(rotor_positions[0])
    rotor_2 = Rotor(rotor_positions[1])
    rotor_3 = Rotor(rotor_positions[2])

    final_message = ""

    for letter in message:
        # Plugboard #1
        tmp_letter = plugboard(letter)

        # Rotor 1
        rotor_1.step()
        tmp_letter = rotor_1.encode_letter(tmp_letter)

        # Rotor 2
        if rotor_1.starting_pos == 0:
            rotor_2.step()
        tmp_letter = rotor_2.encode_letter(tmp_letter)

        # Rotor 3
        if rotor_2.starting_pos == 0:
            rotor_3.step()
        tmp_letter = rotor_3.encode_letter(tmp_letter)

        # Reflector
        tmp_letter = reflector(tmp_letter)

        # Rotor 3
        tmp_letter = rotor_3.decode_letter(tmp_letter)

        # Rotor 2
        tmp_letter = rotor_2.decode_letter(tmp_letter)

        # Rotor 1
        tmp_letter = rotor_1.decode_letter(tmp_letter)

        # Plugboard
        tmp_letter = plugboard(tmp_letter)

        final_message += tmp_letter

    print(final_message)


enigma("HELLO", (0, 0, 0))
enigma("MMGAS", (0, 0, 0))
