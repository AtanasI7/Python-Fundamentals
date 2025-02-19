def no_vowels(data):
    vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
    no_vowel_word = [i for i in word if i not in vowels]
    return ''.join(no_vowel_word)


word = input()
print(no_vowels(word))