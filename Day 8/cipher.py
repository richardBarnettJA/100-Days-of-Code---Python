from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    new_text = ""
    for x in text:
        if x in alphabet:
            position = alphabet.index(x)
            if direction == "encode":
                num = position + shift
                if num > 25:
                    num = (num%25) - 1
                new_text +=  alphabet[num]
            elif direction == "decode":
                num = position - shift
                while num < 0:
                    num += 26
                new_text +=  alphabet[num]
        else:
            new_text +=  x

    print(f"The {direction}d text is {new_text}")

should_continue = True
while should_continue:
    print(logo)
    direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
    print(direction)
    if direction != "encode":
        if direction != "decode":
            print("Invalid Input...")
            continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    result = (input("Type 'yes' to continue and anything else am  to exit! ")).lower()
    if result != "yes":
        should_continue = False
        print("Goodbye!!!")