import art

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar(original_text, shift_amount, encode_or_decode):
    
    if encode_or_decode == "decode":
        shift_amount *= -1

    output_text = ""

    for character in original_text:
        if character in ALPHABET:
            shifted_position = ALPHABET.index(character) + shift_amount
            shifted_position %= len(ALPHABET)
            output_text += ALPHABET[shifted_position]
        else:
            # Keep spaces, numbers, and symbols unchanged.
            output_text += character

    return output_text


def main():
    print(art.logo)

    should_continue = True

    while should_continue:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower().strip()

        while direction not in ("encode", "decode"):
            print("Please enter either 'encode' or 'decode'.")
            direction = input(
                "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
            ).lower().strip()

        text = input("Type your message:\n").lower()

        while True:
            try:
                shift = int(input("Type the shift number:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        result = caesar(
            original_text=text,
            shift_amount=shift,
            encode_or_decode=direction
        )

        print(f"Here is the {direction}d result: {result}")

        restart = input(
            "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
        ).lower().strip()

        if restart == "no":
            should_continue = False
            print("Goodbye!")


if __name__ == "__main__":
    main()
