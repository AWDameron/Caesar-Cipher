# refactoring of the code after discovering the enumerate function.   This code is runs more
# efficiently and allows for a negative shift to convert the coded sentence back.

def Caesar_Cipher(sentence,shift=5):
    letters = "abcdefghijklmnopqrstuvwxyz"
    sentence_list = [letter.lower() for letter in sentence]
    for index,letter in enumerate(sentence_list):
        if letter in letters:
            letter_index = (letters.index(letter) + shift) % 26
            sentence_list[index] = letters[letter_index]
    coded_message = ''.join(sentence_list)

    return coded_message


sentence = "i love coding python"
print(Caesar_Cipher(sentence))

sentence = "n qtaj htinsl udymts"
print(Caesar_Cipher(sentence,-5))


