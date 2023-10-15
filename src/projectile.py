from .target import Target


class Projectile:
    """Снаряд обычный. Им стреляем."""

    def __init__(self, projectile_mass: float, initial_speed: float):
        """
        Создание снаряда.

        :param projectile_mass: Масса снаряда.
        :param initial_speed: Начальная скорость снаряда.
        """
        self.projectile_mass = projectile_mass
        self.initial_speed = initial_speed
        self.position = [0, 0]  # Начальное положение снаряда.

    def inTheTarget(self, target: Target) -> bool:
        """
        Определяем, находится ли снаряд в границах мишени.

        :param target: Мишень, в которую стреляли.
        :return: Попал или не попал снаряд в мишень.
        """
        # Координаты снаряда.
        x, y = self.position

        # Границы по x.
        x_start = target.point3[0]
        x_end = target.point4[0]

        # Границы по y.
        y_start = target.point1[1]
        y_end = target.point3[1]

        # Проверяем, находится ли снаряд в пределах мишени или на ее границах.
        if x_end >= x >= x_start and y_end <= y <= y_start:
            return True
        return False
