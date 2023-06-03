import random

from data import questions_data
from classes.question import Question


def load_questions():
    """
    Функция возвращает список вопросов.
    """

    questions = []

    for question_data in questions_data:
        questions.append(Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        ))
    random.shuffle(questions)

    return questions


def count_correct_answers(questions):
    """
    Функция возвращает количество правильных ответов на вопросы.
    :param questions:
    :return: int
    """
    correct_counter = 0

    for question in questions:
        if question.is_correct():
            correct_counter += 1

    return correct_counter


def count_points(questions):
    """
    Функция возвращает количество набранных баллов.
    :param questions:
    :return: int
    """
    points_counter = 0

    for question in questions:
        if question.is_correct():
            points_counter += question.get_points()

    return points_counter
