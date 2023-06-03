# Создание словарей по уровню сложности.
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# Создание словаря оценки уровня пользователя.
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Создание словаря ответов пользователя.
answers = {}

# Старт программы
print("\nВыберите уровень сложности.")
user_level = input("Легкий, средний, сложный:\n>_ ").lower()

if user_level == "средний":
    words = words_medium
elif user_level == "сложный":
    words = words_hard
else:
    user_level = "легкий"
    words = words_easy

# Альтернативное начало
# if user_level == "легкий":
#     words = words_easy
# elif user_level == "средний":
#     words = words_hard
# elif user_level == "сложный":
#     words = words_hard
# else:
#     print("Уровень сложности не найден\n")
#     exit()


word_count = len(words)

print(f"\nВыбран уровень сложности: {user_level}, "
      f"мы предложим {word_count} слов, подберите перевод.")
# while True:
#     if input("\nНажмите Enter для продолжения\n") == '':
#             break


for word_en, word_ru in words.items():
    input("\nНажмите Enter для продолжения ")

    letter_count = len(word_ru)
    first_letter = word_ru[0]

    print(f"{word_en}, {letter_count} букв, начинается на {first_letter}...")
    user_answer = input("Перевод: ").lower()

    if user_answer == word_ru:
        print(f"Верно, {word_en.title()} — это {word_ru}.")
        answers[word_en] = True
    else:
        print(f"Неверно. {word_en.title()} — это {word_ru}.")
        answers[word_en] = False

# Результат ответов пользователя.

# Альтернативный вариант.
# print("\nПравильно отвечены слова:")

# for word_en, is_correct in answers.items():
#     if is_correct:
#         print(word_en)

# print("\nНеправильно отвечены слова:")
# for word_en, is_correct in answers.items():
#     if not is_correct:
#         print(word_en)
# print()

correct_words = []
incorrect_words = []

for word_en, is_correct in answers.items():
    if is_correct:
        correct_words.append(word_en)
    else:
        incorrect_words.append(word_en)

print("\nПравильно отвечены слова:")
print("\n".join(correct_words))
print("\nНеправильно отвечены слова:")
print("\n".join(incorrect_words))
# print()

""" Выводим ранг пользователя. """
correct_count = len(correct_words)
user_level = levels[correct_count]

print(f"\nВаш ранг:\n{user_level}\n")
