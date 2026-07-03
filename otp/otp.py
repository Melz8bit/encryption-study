import os


def otp(message: str, is_encode: bool, key: str = None):
    key = os.urandom(len(message)) if is_encode else bytes.fromhex(key)
    msg_bytes = message.encode() if is_encode else bytes.fromhex(message)
    final_message = bytes(b1 ^ b2 for b1, b2 in zip(msg_bytes, key))

    print(f"{key.hex()=}")
    print(f"{final_message.hex()=}") if is_encode else print(f"{final_message=}")
    print("==============================")

    if is_encode:
        return final_message, key.hex()

    return final_message.decode()


user_is_encode = input("Encode or decode? ").lower()
is_encode = True if user_is_encode == "encode" else False
message = input("Enter message: ")
key = input("Enter key: ") if not is_encode else None
otp(message, is_encode, key)
