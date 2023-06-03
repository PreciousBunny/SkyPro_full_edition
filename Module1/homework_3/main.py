
# Создание списка с вопросами.
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
# Создание списка с ответами.
answers = ["is", "am", "in"]


# Счетчик правильных ответов.
correct_answer_counter = 0

# Приветсвие программы и предложение начать.
print("\nПривет! Предлагаю проверить свои знания английского!")
lets_begin = input("Наберите \"ready\", чтобы начать!\n>_ ")

if lets_begin.lower() != "ready":
    print("\nКажется, вы не хотите играть. Очень жаль.\n")
else:
    # Начинаем задавать вопросы.
    for i in range(len(questions)):

        questions_text = questions[i]
        answers_text = answers[i]

        print("\nВопрос:", questions_text)
        user_answer = input("Ответ:  ")

        if user_answer.lower() == answers_text:
            correct_answer_counter += 1
            print("Ответ верный!")
        else:
            print(f"Неправильно.\nПравильный ответ: {answers_text}\n")


# Количество процентов.
user_percentage = round((correct_answer_counter / len(questions)) * 100, 2)


print("Вот и все!\n"
      f"Вы ответили на {correct_answer_counter} вопросов из 3 верно.\n"
      f"Это {user_percentage} процентов.\n")

