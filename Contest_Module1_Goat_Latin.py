def goat(sentence):
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    def convert_word(word, index):
        if word[0] in vowels:
            return word + "ma" + "a" * (index + 1)
        else:
            return word[1:] + word[0] + "ma" + "a" * (index + 1)
    goat_latin_words = [convert_word(word, i) for i, word in enumerate(words)]
    result = " ".join(goat_latin_words)
    return result
input_sentence = input()
print(goat(input_sentence))