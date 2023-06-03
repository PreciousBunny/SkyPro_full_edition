class Question:

    def __init__(self, question_text, question_diff, question_answer) -> None:
        self.question_text = question_text
        self.question_diff = question_diff
        self.question_answer = question_answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.question_diff * 10

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верными ответами иначе False.
        """
        return self.user_answer == self.question_answer
        # if self.user_answer == self.question_answer:
        #     return True

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        answer_text = f"\nВопрос: {self.question_text}\nСложность: {self.question_diff}/5"
        return answer_text

    def build_positive_feedback(self):
        """
        Возвращает:
        Ответ верный, получено __ баллов
        """
        answer_text = f"Ответ верный, получено {self.points} баллов"
        return answer_text

    def build_negative_feedback(self):
        """
        Возвращает:
        Ответ неверный, верный ответ __
        """
        answer_text = f"Ответ неверный. Верный ответ - {self.question_answer}"
        return answer_text

    def __repr__(self):
        return f"{self.question_text} - {self.question_answer} ({self.question_diff}/5)"

