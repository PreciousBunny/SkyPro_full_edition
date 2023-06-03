class Player:
    """
    Базовый класс Player.
        Args:
            name: передается имя пользователя.
        Attributes:
            used_subwords: использованные слова пользователя.
    """

    def __init__(self, name):
        self.name = name
        self.used_subwords = []

    @property
    def get_count_used_subwords(self) -> int:
        """
        Метод возвращает количество использованных слов (возвращает int).
        """
        return len(self.used_subwords)

    def append_subword_in_used_subwords(self, subword) -> None:
        """
        Метод добавляет подслово в список использованных подслов (ничего не возвращает).
        """
        self.used_subwords.append(subword)

    def is_subword_in_used_subwords(self, subword) -> bool:
        """
        Метод возвращает проверку использования данного подслова в списке использованных подслов (возвращает bool).
        """
        return subword in self.used_subwords

    def __repr__(self) -> str:
        """
        Метод возвращает приветствие пользователя.
        """
        return f"Привет, {self.name.title()}!"
