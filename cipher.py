
# Dress your text up to the Caesar's preferred method of encryption, the default value for this 
# program is 5, but if you'd like to use a different shift you can simply call the function as
# Caesar_Dressing(sentence,integer_here).   

def Caesar_Dressing (sentence, shift=5):
    letters = "abcdefghijklmnopqrstuvwxyz"
    sentence_index = 0 
    # used print for checking program as it's being written: print(sentence)
    sentence_list = [letter.lower() for letter in sentence]
    # used print for checking program as it's being written: print(sentence_list)
    for letter in sentence_list:
        if letter in letters:
            index = letters.index(letter)
            if index + shift >= 26:
                new_index = (index+shift) % 26
                sentence_list[sentence_index] = letters[index]
                sentence_index += 1
            else:
                sentence_list[sentence_index] = letters[index+shift]
                sentence_index += 1
        else:
            sentence_index += 1
    # used print for checking program as it's being written: print(sentence_list)
    coded_sentence = "".join(sentence_list) 
    
    return coded_sentence


sentence = 'n qtvj htinsl ns uyymts'
print(sentence)
print(Caesar_Dressing(sentence,-5))

