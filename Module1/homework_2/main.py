# Приветствие пользователя.
print("\nПривет! Предлагаю проверить свои знания английского!")
personal_name = input("Расскажи, как тебя зовут!\n>_ ")
print(f"Привет, {personal_name.title()}, начинаем тренировку!\n")

# Счетчик правильных ответов.
correct_answer_counter = 0
# Счетчик вопросов.
question_counter = 0

# Начинаем задавать 3 вопроса.
# first_question
question_counter += 1
first_answer = "is"

print("Первый вопрос: My name ___ Vova")
user_answer = input("Ответ:  ")

if user_answer.lower() == first_answer:
    correct_answer_counter += 1
    print("Ответ верный!\nВы получаете 10 баллов!\n")
else:
    print(f"Неправильно.\nПравильный ответ: {first_answer}\n")

# second_question
question_counter += 1
second_answer = "am"

print("Второй вопрос: I ___ a coder")
user_answer = input("Ответ:  ")

if user_answer.lower() == second_answer:
    correct_answer_counter += 1
    print("Ответ верный!\nВы получаете 10 баллов!\n")
else:
    print(f"Неправильно.\nПравильный ответ: {second_answer}\n")

# third_question
question_counter += 1
third_answer = "in"

print("Третий вопрос: I live ___ Moscow")
user_answer = input("Ответ:  ")

if user_answer.lower() == third_answer:
    correct_answer_counter += 1
    print("Ответ верный!\nВы получаете 10 баллов!\n")
else:
    print(f"Неправильно.\nПравильный ответ: {third_answer}\n")

# Количество баллов пользователя.
user_score = correct_answer_counter * 10
# Количество процентов.
user_percentage = round((correct_answer_counter / question_counter) * 100, 4)

print(f"Вот и все, {personal_name.title()}!\n"
      f"Вы ответили на {correct_answer_counter} вопросов из 3 верно.\n"
      f"Вы заработали {user_score} баллов.\n"
      f"Это {user_percentage} процентов.\n")
