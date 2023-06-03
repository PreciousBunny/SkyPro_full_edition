class BasicWord:
    """
    Базовый класс BasicWord.
        Args:
            word: передается исходное слово.
            subwords: передается список подслов, составленных из исходного слова.
    """

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def has_subword(self, user_subword) -> bool:
        """
        Метод возвращает наличие введенного слова в списке допустимых подслов (вернет bool).
        """
        return user_subword in self.subwords

    @property
    def get_count_subwords(self) -> int:
        """
        Метод возвращает подсчет количества подслов (вернет int).
        """
        return len(self.subwords)

    @property
    def get_min_length_subword(self):
        """Метод возвращает самую минимальную длину из подслов"""
        return len(min(self.subwords, key=len))

    def __repr__(self):
        """Метод возвращает информацию о слове и кол-ве его подслов"""
        return f"Составьте {self.get_count_subwords} слов из слова {self.word.upper()}" \
               f"\nСлова не должны быть короче {len(min(self.subwords, key=len))}-х букв"
