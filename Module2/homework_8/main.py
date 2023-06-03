
from classes.question import Question
from functions import load_questions, count_correct_answers, count_points


def main():

    questions = load_questions()

    for question in questions:
        print(question.build_question())
        user_answer = input()
        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    correct_counter = count_correct_answers(questions)
    points = count_points(questions)

    print("Вот и все!")
    print(f"Отвечено {correct_counter} из {len(questions)}")
    print(f"Набрано баллов: {points}")


if __name__ == "__main__":
    main()
