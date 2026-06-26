import math

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def _generate_cipher(keyword: str) -> str:
    cipher = [""] * 5
    cipher_row = 0
    cipher_col = 0

    cipher_alphabet = "".join(dict.fromkeys(keyword + ALPHABET))

    for letter in cipher_alphabet:
        if cipher_col == 5:
            cipher_col = 0
            cipher_row += 1

        if cipher_row == 5:
            break

        if letter.isalpha():
            cipher[cipher_row] += letter

        cipher_col += 1

    return cipher, cipher_alphabet


def _message_prep(message: str) -> list:
    message = "".join(char for char in message if char.isalpha())

    pair_i = 0
    message_pairs = [""] * math.ceil(len(message) / 2)
    for i, letter in enumerate(message):
        message_pairs[pair_i] += letter
        if i % 2 == 1:
            pair_i += 1

    for i, pair in enumerate(message_pairs):
        if len(message_pairs[i]) == 2 and pair[0] == pair[1]:
            message_pairs[i] = pair[0] + "X" + pair[1]

        if len(message_pairs[i]) == 3:
            if i + 1 < len(message_pairs):
                message_pairs[i + 1] = message_pairs[i][-1] + message_pairs[i + 1]
            else:
                message_pairs.append(message_pairs[i][-1])

            message_pairs[i] = message_pairs[i][:-1]

    if len(message_pairs[-1]) == 1:
        message_pairs[-1] += "X"

    return message_pairs


def _get_coordinates(letter: str, cipher: list):
    row, col = 0, 0

    for i in range(len(cipher)):
        if letter in cipher[i]:
            row = i
            col = cipher[i].index(letter)

    return (row, col)


def playfair(message: str, keyword: str):
    message = message.upper()
    keyword = keyword.upper()

    cipher_grid, cipher_alphabet = _generate_cipher(keyword)
    message_pairs = _message_prep(message)

    letter_coordinates = {}
    for letter in cipher_alphabet:
        letter_coordinates[letter] = _get_coordinates(letter, cipher_grid)

    encrypted = ""
    for pair in message_pairs:
        # Same row
        if letter_coordinates[pair[0]][0] == letter_coordinates[pair[1]][0]:
            col_1 = (letter_coordinates[pair[0]][1] + 1) % 5
            col_2 = (letter_coordinates[pair[1]][1] + 1) % 5
            encrypted += (
                cipher_grid[letter_coordinates[pair[0]][0]][col_2]
                + cipher_grid[letter_coordinates[pair[1]][0]][col_1]
            )
        # Same column
        elif letter_coordinates[pair[0]][1] == letter_coordinates[pair[1]][1]:
            row_1 = (letter_coordinates[pair[0]][0] + 1) % 5
            row_2 = (letter_coordinates[pair[1]][0] + 1) % 5
            encrypted += (
                cipher_grid[row_1][letter_coordinates[pair[0]][1]]
                + cipher_grid[row_2][letter_coordinates[pair[1]][1]]
            )
        # Rectangle
        else:
            col_1 = letter_coordinates[pair[0]][1]
            col_2 = letter_coordinates[pair[1]][1]
            encrypted += (
                cipher_grid[letter_coordinates[pair[0]][0]][col_2]
                + cipher_grid[letter_coordinates[pair[1]][0]][col_1]
            )

    print(f"{encrypted=}")


playfair("hello", "keyword")
