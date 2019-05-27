# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel_count = 0
for letter in ["а", "о", "и", "е", "ё", "э", "ы", "у", "ю", "я"]:
    vowel_count += word.lower().count(letter)
print("Vowel count: {}".format(vowel_count))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0].upper())


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words_len  = [len(word) for word in sentence.split()]
print("Average word length: {}".format(int(sum(words_len) / len(words_len))))
