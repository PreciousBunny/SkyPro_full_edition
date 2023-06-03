import random

words = ["snake", "programmer", "soul", "cookie",
         "flawless victory", "destiny", "well-done"]

MORSE_CODES = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

answers = []


def morse_encode(word):
    """
    Функция переводит слова на английском языке
    в последовательности точек и тирe.
    :param word: исходное слово.
    :return: строка Морзе.
    """
    word_encode = []

    for letter in word:
        word_encode.append(MORSE_CODES.get(letter, ""))
    return " ".join(word_encode)


def get_word():
    """
    Функция получает случайное слово из списка.
    :return: строка слова.
    """
    return random.choice(words)


def print_statistics(answers):
    """
    Функция которая на основе списка answers типа
    [True, False, False, True, False] выводит статистику.
    :param answers: список верности ответов.
    """

    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct

    print(f"Всего задачек: {answers_total}\n"
          f"Отвечено верно: {answers_correct}\n"
          f"Отвечено неверно: {answers_incorrect}\n")


def main():
    """
    Основная функция этой программы. Происходит
    взаимодействие с пользователем, ведется подсчет
    верных и неверных ответов.
    """

    print("\nСегодня мы потренируемся расшифровывать азбуку Морзе.")
    input("Нажмите Enter и начнем\n>_ ")
    print()

    for i in range(1, len(words) + 1):

        current_word = get_word()
        current_encoded = morse_encode(current_word)
        print(f"Слово {i} {current_encoded}")

        user_input = input(">_ Ответ: ")

        if user_input.lower() == current_word:
            print(f"Верно, {current_word}!\n")
            answers.append(True)
        else:
            print(f"Неверно, {current_word}!\n")
            answers.append(False)

    print_statistics(answers)


if __name__ == "__main__":
    main()
