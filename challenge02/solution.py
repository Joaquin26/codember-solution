# MIN_VALUE = 97 letter 'a' in code ASCII
# MAX_VALUE = 122 letter 'z' in code ASCII


def transform_code_to_word(code: str):
    word = ""
    letter_encrypted = ""
    index = 0
    while index < len(code):
        next_index: int = index + 2
        if int(code[index]) == 1:
            next_index += 1
        letter_encrypted += code[index:next_index]
        word += chr(int(letter_encrypted))
        index = next_index
        letter_encrypted = ""
    return word


with open("encrypted.txt", "r") as file:
    codes = file.read().split(" ")
    [print(transform_code_to_word(code), end=" ") for code in codes]
