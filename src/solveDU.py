from numpy import cos, sin, radians, linspace
from scipy.integrate import odeint


def finding_move(m: float,
                 k: float,
                 v0: float,
                 alpha: float,
                 end_t: float = 10000
                 ) -> tuple:
    """
    Нахождения длины перемещения снаряда после выстрела.

    :param m: Масса снаряда.
    :param k: Коэффициент сопротивления среды, в которой происходит выстрел.
    :param v0: Начальная скорость снаряда, с которой он вылетает с пушки.
    :param alpha: Угол наклона пушки к горизонту в градусах.
    :param end_t: Конечная граница генерации аргументов.
    :return: Длина перемещения снаряда.
             Набор x-сов и y-ков, и их производных после численного решения ДУ.
    """

    def FX(s: list,
           t: list,
           k: float,
           m: float
           ) -> list:
        """
        Вспомогательная функция, описывающая ДУ второго порядка,
        как систему уравнений первого порядка для проекции на ось OX.

        :param s: Массив функций, которые необходимо найти.
        :param t: Массив аргументов. Требуется для использования функции в odeint().
        :param k: Коэффициент сопротивления среды, в которой происходит выстрел.
        :param m: Масса снаряда.
        :return: Численное решение пути и скорости в проекции OX.
        """
        dxdt = s[1]  # Правая первая запись системы.
        dvdt = -k / m * s[1] ** 3  # Правая вторая запись системы.
        return [dxdt, dvdt]  # Численные левые части соответственно.

    def FY(s: list,
           t: list,
           k: float,
           m: float
           ) -> list:
        """
        Вспомогательная функция, описывающая ДУ второго порядка,
        как систему уравнений первого порядка для проекции на ось OY.

        :param s: Массив функций, которые необходимо найти.
        :param t: Массив аргументов. Требуется для использования функции в odeint().
        :param k: Коэффициент сопротивления среды, в которой происходит выстрел.
        :param m: Масса снаряда.
        :return: Численное решение пути и скорости в проекции OY.
        """
        dydt = s[1]  # Правая первая часть системы.
        dvdt = - 9.8 - k / m * s[1] ** 3  # Правая вторая запись системы.
        return [dydt, dvdt]  # Численные левые части соответственно.

    # Начальные условия.
    X0 = [0, v0 * cos(radians(alpha))]  # Для проекции на OX.
    Y0 = [0, v0 * sin(radians(alpha))]  # Для проекции на OY.

    # Аргументы. Для большей наглядности на графиках нужно менять второй аргумент, поэтому - это переменная.
    t = linspace(0, end_t, 10000)

    # Численные решения.
    x_for_graph = odeint(FX, X0, t, args=(k, m))  # Иксы и производные.
    y_for_graph = odeint(FY, Y0, t, args=(k, m))  # Игреки и производные.

    # Найдем длину перемещения снаряда.
    # Отбираем координаты снаряда.
    x_sol = odeint(FX, X0, t, args=(k, m))[:, 0]
    y_sol = odeint(FY, Y0, t, args=(k, m))[:, 0]

    # Неотрицательные игреки.
    y_positive = [element for element in y_sol[1:] if element >= 0]

    # Ищем наименьший игрек среди неотрицательных (он будет ближайший к нулю).
    # Ищем его индекс в списке всех игреков.
    # По полученному индексу ищем соответствующий икс, который будет равен длине перемещения снаряда.
    moving_length = x_sol[list(y_sol).index(min(y_positive))]

    # Для графиков вернем еще и значения иксов и игреков, и их производных.
    return moving_length, x_for_graph, y_for_graph
