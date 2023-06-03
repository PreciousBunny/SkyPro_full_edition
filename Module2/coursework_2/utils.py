from random import choice
import requests
from classes.basic_word import BasicWord
from classes.player import Player


def load_random_word(path) -> BasicWord:
    """
    Функция возвращает экземпляр класса BasicWord со случайным словом.
    """
    random_word = choice(requests.get(path).json())
    return BasicWord(random_word["word"], random_word["subwords"])


def get_player() -> Player:
    """
    Функция запрашивает имя игрока и возвращает экземпляр класса Player.
    """
    player_name = input("Введите имя игрока:\n> ")
    return Player(player_name)


def output_start_play(player, word) -> None:
    """
    Функция выводит приветствие и оговаривает правила игры.
    """
    print(player)
    print(word)
    print("Чтобы закончить игру, угадайте все слова или напишите 'stop' ('стоп')")
    print("Поехали, ваше первое слово?")


def output_statistics(answers) -> None:
    """
    Функция выводит статистику ответов пользователя.
    """
    word = ""
    if answers == 1 or (answers > 20 and answers % 10 == 1) \
            and answers % 100 != 11:
        word = "слово"
    elif (1 < answers < 5) or \
            (answers > 20 and 1 < answers % 10 < 5):
        word = "слова"
    elif answers == 0 or (answers > 1 and answers < 20) \
            or answers % 10 == 0 or answers % 100 >= 11 \
            or answers % 10 >= 5 or answers % 100 >= 10:
        word = "слов"
    print(f"\nИгра завершена, вы угадали {answers} {word}!\n")
