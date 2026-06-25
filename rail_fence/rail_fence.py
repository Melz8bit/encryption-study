def rail_fence(message: str, rails: int):
    rails = int(rails)
    is_down = True
    fence = [""] * rails

    rail_i = 0
    for letter in message:
        if rail_i == rails - 1:
            is_down = False
        elif rail_i == 0:
            is_down = True

        fence[rail_i] += letter

        if is_down:
            rail_i += 1
        else:
            rail_i -= 1

    fence_msg = ""
    for _ in fence:
        fence_msg += _

    print(fence_msg)


message = input("Enter message: ")
rails = input("Enter rail amount: ")
rail_fence(message, rails)
