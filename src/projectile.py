from .target import Target


class Projectile:
    """Снаряд."""

    def __init__(self, projectile_mass: float, initial_speed: float) -> None:
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

        # Координаты мишени.
        xp = [target.point1[0], target.point2[0], target.point3[0], target.point4[0]]
        yp = [target.point1[1], target.point2[1], target.point3[1], target.point4[1]]

        c = 0
        for i in range(len(xp)):
            if (((yp[i] <= y < yp[i - 1]) or (yp[i - 1] <= y < yp[i])) and
                    (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])):
                c = 1 - c
        return True if c else False
