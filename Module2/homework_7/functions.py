import os
import json


def read_json_file(path):
    """
    Функция для чтения json файла.
    """
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)

def load_students():
    """
    Функция возвращает список с информацией о студентах.
    """
    path = os.path.abspath("data/students.json")
    return read_json_file(path)


def load_professions():
    """
    Функция возвращает список с информацией о профессиях.
    """
    path = os.path.abspath("data/professions.json")
    return read_json_file(path)



def get_student_by_pk(pk):
    """
    Функция возвращает словарь с информацией о студенте.
    :param pk: передает номер студента.
    :return: словарь с информацией о студенте.
    """
    students = load_students()
    if pk <= 0 or pk > len(students):
        print("У нас нет такого студента")
        exit()
        # quit()
    student = students[pk - 1]
    print(f"Студент {student['full_name']}")
    print(f"Знает {', '.join(student['skills'])}")
    return student


def get_profession_by_title(title):
    """
    Функция ищет профессию по title и возвращает словарь с информацией о ней.
    :param title: название профессии.
    :return: словарь с информацией о профессии.
    """
    professions = load_professions()
    for profession in professions:
        if profession["title"] == title.title():
            return profession
    print("У нас нет такой специальности")
    exit()
    # quit()


def check_fitness(student, profession):
    """
    Функция возвращает соответствие студента с выбранным
    направлением в профессии в виде словаря.
    """
    has_skill = set(student["skills"]).intersection(profession["skills"])
    lacks = set(profession["skills"]).difference(student["skills"])
    fit_percent = round((len(has_skill) / len(profession["skills"])) * 100)
    return {"has_skill": has_skill, "lacks": lacks, "fit_percent": fit_percent}




