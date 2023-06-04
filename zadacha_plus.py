# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте. НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ МЕТОД SPLIT

text = input("Введите сюда что хотите:").rstrip(" ")  # rstrip возвращает копию указанной строки в которой устранены указанные символы ()
words = set()

current_word = ""
for char in text:
    if char != " ":
        current_word += char
    elif current_word:
        words.add(current_word)
        current_word = ""

if current_word:
    words.add(current_word)

print(len(words))
