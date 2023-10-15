class Environment:
    """Среда, в которой проходит эксперимент."""

    def __init__(self):
        """Создание среды."""
        # Коэффициент сопротивления среды, в которой находится мишень, пушка и вообще вся система.
        self.__K = 0

    def set_K(self, value: float):
        """
        Определение коэффициента сопротивления среды, в которой находится система.

        :param value: Значение коэффициента.
        :return: None
        """
        self.K = value

    def get_K(self):
        """
        Получения коэффициента сопротивления среды.

        :return: Коэффициент сопротивления среды.
        """
        return self.K