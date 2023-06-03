import random


def get_word_from_file(path):
    """
    Функция получает все слова из файла списком.
    :return: строка слова.
    """

    with open(path, "r", encoding="utf-8") as file:
        lines = file.read()
        words = lines.splitlines()
    return words


def get_mix_word(word):
    """
   Функция перемешивает буквы в слове.
   :return: строка слова.
   """
    items = random.sample(word, len(word))
    result = "".join(items)
    return result


def save_top_player(path, player_name, player_record):
    """
    Функция записывает в ТОП лист имя игрока
    и его числовой рекорд .
    """
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{player_name} {player_record}\n")


def get_statistics_games(path):
    """
   Функция запоминает максимальный рекорд и количество сыгранных игр.
   """

    records = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            #  if line.strip() == "":
            #      continue
            record = line.rstrip("\n").split(" ")[-1]
            records.append(int(record))

    max_record = max(records)
    game_played = len(records)

    return {"max_record": max_record, "game_played": game_played}
