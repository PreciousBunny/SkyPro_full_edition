from functions import get_word_from_file, get_mix_word, save_top_player, get_statistics_games
from config import WORDS_PATH, HISTORY_PATH


def main():
    """
    Основная функция этой программы. Происходит
    взаимодействие с пользователем, ведется подсчет
    очков.
    """
    player_name = input("Введите ваше имя:\n> ")

    points = 10
    player_record = 0

    words = get_word_from_file(WORDS_PATH)

    for word in words:
        mix_word = get_mix_word(word)

        print(f"Угадайте слово: {mix_word}")
        user_answer = input("Ответ:> ")

        if user_answer == word:
            print(f"Верно! Вы получаете {points} очков")
            player_record += points
        else:
            print(f"Неверно! Верный ответ - {word}")

    save_top_player(HISTORY_PATH, player_name, player_record)

    statistics = get_statistics_games(HISTORY_PATH)

    print(f"\nВсего игр сыграно: {statistics.get('game_played')}")
    print(f"Максимальный рекорд: {statistics.get('max_record')}")


if __name__ == "__main__":
    main()