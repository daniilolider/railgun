from numpy.linalg import solve
from numpy import cos, sin, radians, arctan2, degrees, dot

from .solveDU import finding_move
from .projectile import Projectile


class Gun:
    """Пушка."""

    def __init__(self):
        """Создание пушки."""
        # Начальное положение.
        self.x = 0
        self.y = 0
        self.direction = [0, 0]  # Координаты конечной точки вектора, задающего начальное направление пушки.
        self.inclination = 0  # Угол наклона.
        self.turn = 0  # Угол поворота.

    def set_location(self, location: list[float]) -> None:
        """
        Располагаем пушку на плоскости.

        :param location: Список коэффициентов A, B, C двух прямых, записанных в общем виде.
        :return: None.
        """
        # Коэффициенты двух прямых.
        A1, B1, C1, A2, B2, C2 = location
        # Решая систему, ищем точку пересечения двух прямых. Это и будет координаты пушки.
        self.x, self.y = solve([[A1, B1], [A2, B2]], [-C1, -C2])

    def shoot(self,
              inclination: float,
              turn: float,
              projectile: Projectile,
              air_resistance: float,
              ) -> tuple:
        """
        Выстрел с пушки.

        :param inclination: Угол наклона пушки.
        :param turn: Угол поворота пушки.
        :param projectile: Снаряд, которым будем стрелять.
        :param air_resistance: Коэффициент сопротивления среды, в которой происходит выстрел.
        :return: Дальность полёта снаряда. Иксы и игреки для графиков.
        """

        # Ставим угол наклона и поворота пушки.
        self.inclination = inclination
        self.turn = turn

        # Длина перемещения снаряда.
        moving_length, x_for_graph, y_for_graph = finding_move(m=projectile.projectile_mass,
                                                               k=air_resistance,
                                                               v0=projectile.initial_speed,
                                                               alpha=inclination,
                                                               end_t=100)

        # Новые координаты после падения снаряда.
        new_x = moving_length * cos(radians(self.turn)) + self.x
        new_y = moving_length * sin(radians(self.turn)) + self.y

        # Переопределяем координаты снаряда.
        projectile.position = [new_x, new_y]

        return moving_length, x_for_graph, y_for_graph

    def get_direction(self, direction: tuple[float]) -> float:
        """
        Ставит пушку в стартовом направлении и угол начального поворота, относительно оси OX.
        Направление задаётся вектором, начало которого - расположение пушки, конец - точка на плоскости.

        :param direction: Концевая точка вектора.
        :return: Угол начального поворота, относительно оси OX.
        """

        # Задаём начальное направление пушки.
        self.direction = direction

        # Координаты нового соответствующего вектора с началом в (0, 0).
        new_x = direction[0] - self.x
        new_y = direction[1] - self.y

        # Считаем угол между новым вектором и положительной осью OX.
        start_angle = degrees(arctan2(new_y, new_x))

        # Проверяем, чтобы угол не был отрицательным.
        if start_angle < 0:
            start_angle += 360
        return start_angle
