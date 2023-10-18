from .gun import Gun
from .projectile import Projectile
from .target import Target
from .environment import Environment


def print_all_info(gun: Gun,
                   turn: float,
                   inclination: float,
                   projectile: Projectile,
                   target: Target,
                   environment: Environment,
                   moving_length: float,
                   result_in_target: bool,
                   direction_angle: float,
                   random_values: tuple
                   ) -> None:
    """
    Выводит всю информацию об эксперименте в консоль.

    :param gun: Пушка, с которой стреляли.
    :param turn: Угол, на который поворачивали пушку.
    :param inclination: Угол, на который наклонили пушку.
    :param projectile: Снаряд, которым стреляли.
    :param target: Мишень, в которую стреляли.
    :param environment: Среда, в которой стреляли.
    :param moving_length: Длина перемещения снаряда.
    :param result_in_target: Ответ, попал ли снаряд в мишень.
    :param direction_angle: Начальный угол поворота пушки.
    :param random_values: Погрешности.
    :return: None.
    """
    result_print = f"\n############################\n" \
                   f"ПУШКА:\n" \
                   f"\tПушка находится в точке: {gun.x, gun.y};\n" \
                   f"\tНачальный угол поворота пушки: {direction_angle};\n" \
                   f"\tУгол попорота: {turn};\n" \
                   f"\tУгол наклона: {inclination};\n" \
                   f"СНАРЯД:\n" \
                   f"\tМасса снаряда: {projectile.projectile_mass};\n" \
                   f"\tНачальная скорость снаряда: {projectile.initial_speed};\n" \
                   f"МИШЕНЬ:\n" \
                   f"\tТочки границ мишени: {target.point1, target.point2, target.point3, target.point4};\n" \
                   f"СРЕДА:\n" \
                   f"\tКоэффициент сопротивления среды: {environment.get_K()};\n" \
                   f"ПОГРЕШНОСТИ:\n" \
                   f"\tПогрешность угла поворота: {random_values[0]};\n" \
                   f"\tПогрешность угла наклона: {random_values[1]};\n" \
                   f"\tПогрешность начальной скорости: {random_values[2]};\n" \
                   f"РЕЗУЛЬТАТЫ:\n" \
                   f"\tДлина перемещения снаряда: {moving_length};\n" \
                   f"\tКоординаты падения снаряда: {projectile.position[0] + gun.x, projectile.position[1] + gun.y};\n" \
                   f"\tПопал? = {result_in_target}"

    print(result_print)
