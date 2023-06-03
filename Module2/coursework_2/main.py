from config import WORDS_URL_JSON_KEEPER
from utils import *


def main():
    """
    Основная функция. Определяет корректность игры и в конце выводит статистику по ней.
    """
    player = get_player()
    basic_word = load_random_word(WORDS_URL_JSON_KEEPER)
    output_start_play(player, basic_word)

    while player.get_count_used_subwords < basic_word.get_count_subwords:
        user_subword = input("> ").lower()
        if user_subword.lower() in ['stop', 'стоп']:
            break
        elif len(user_subword) < basic_word.get_min_length_subword:
            print("слишком короткое слово")
        elif not basic_word.is_subword(user_subword):
            print("неверно")
        elif player.is_subword_in_used_subwords(user_subword):
            print("уже использовано")
        else:
            print("верно")
            player.append_subword_in_used_subwords(user_subword)

    output_statistics(player.get_count_used_subwords)


if __name__ == "__main__":
    main()
