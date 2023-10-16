from numpy.linalg import solve
from numpy import cos, sin, radians

from .solveDU import finding_move
from .projectile import Projectile


class Gun:
    """Пушка обычная. Из нее стреляем."""

    def __init__(self):
        """Создание пушки."""
        # Начальное положение.
        self.x = 0
        self.y = 0
        self.inclination = 0  # Угол наклона.
        self.turn = 0  # Угол поворота.

    def set_location(self, location: list[float]) -> None:
        """
        Располагаем пушку на плоскости.

        :param location: Список коэффициентов A, B, C двух прямых в общем виде.
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
              ) -> float:
        """
        Выстрел с пушки.

        :param inclination: Угол наклона пушки.
        :param turn: Угол поворота пушки.
        :param projectile: Снаряд, которым будем стрелять.
        :param air_resistance: Коэффициент сопротивления среды, в которой происходит выстрел.
        :return: Дальность полёта снаряда.
        """
        # Длина перемещения снаряда.
        moving_length = finding_move(m=projectile.projectile_mass,
                                     k=air_resistance,
                                     v0=projectile.initial_speed,
                                     alpha=inclination,
                                     end_t=100)[0]

        # Новые координаты после падения снаряда.
        new_x = moving_length * cos(radians(turn)) + self.x
        new_y = moving_length * sin(radians(turn)) + self.y

        # Переопределяем координаты снаряда.
        projectile.position = [new_x, new_y]

        return moving_length
