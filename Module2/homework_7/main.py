from functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    """
    Основная функция. Общение с пользователем и вывод результата профпригодности.
    """
    student_number = int(input("Введите номер студента:\n> "))
    student = get_student_by_pk(student_number)
    student_name = student["full_name"]
    profession_name = str(input(f"Выберите специальность для оценки студента {student_name}\n> "))
    profession = get_profession_by_title(profession_name)
    student_result = check_fitness(student, profession)

    print(f"Пригодность {student_result['fit_percent']}%")
    print(f"{student_name} знает {', '.join(student_result['has_skill'])}")
    print(f"{student_name} не знает {', '.join(student_result['lacks'])}")


if __name__ == "__main__":
    main()
