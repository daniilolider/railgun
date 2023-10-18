from random import uniform
from csv import writer
from copy import deepcopy

from .gun import Gun
from .projectile import Projectile
from .target import Target


def random_shoot(gun: Gun,
                 projectile: Projectile,
                 target: Target,
                 inclination: float,
                 turn: float,
                 air_resistance: float,
                 delta_turn: float,
                 delta_inclination: float,
                 delta_speed: float,
                 count: int = 100
                 ) -> None:
    """
    100 случайных выстрелов пушкой. Запись результатов в csv файл. Количество выстрелов можно задавать.

    :param gun: Пушка, из которой будем стрелять.
    :param projectile: Снаряд, которым будем стрелять.
    :param target: Мишень, по которой стреляем.
    :param inclination: Угол наклона пушки.
    :param turn: Угол поворота пушки.
    :param air_resistance: Коэффициент сопротивления среды, в которой происходит выстрел.
    :param delta_speed: Границы погрешности угла поворота пушки.
    :param delta_inclination: Границы погрешности угла наклона пушки.
    :param delta_turn: Границы погрешности начальной скорости снаряда.
    :param count: Количество итераций.
    :return: None.
    """

    # Один раз открыли и по новой переписали csv файл.
    with open('shoots.csv', mode='w', encoding='utf-8') as w_file:
        file_writer = writer(w_file, delimiter=",", lineterminator="\r")
        # Поля.
        file_writer.writerow(['№',
                              'Погрешность угла наклона',
                              'Погрешность угла поворота',
                              'Погрешность скорости',
                              'Угол наклона',
                              'Угол поворота',
                              'Скорость',
                              'Дальность полета',
                              'x',
                              'y',
                              'Результат попадания'])

        # 100 случайных выстрелов. Каждый выстрел записываем в файл.
        for i in range(1, count + 1):

            # Случайные величины, на которые происходит ошибка при выстреле.
            error_inclination_value = uniform(-delta_inclination, delta_inclination)
            error_turn_value = uniform(-delta_turn, delta_turn)
            error_speed_value = uniform(-delta_speed, delta_speed)

            # Создаём новые значения с учётом погрешностей.
            new_inclination = inclination + error_inclination_value
            new_turn = turn + error_turn_value

            # Сохраняем скорость, чтобы вернуть ее в конце случайного эксперимента.
            speed_save = deepcopy(projectile.initial_speed)

            # Переопределяем скорость.
            projectile.initial_speed += error_speed_value

            # Стреляем с новыми параметрами, но в тех же условиях.
            moving_length = gun.shoot(inclination=new_inclination,
                                      turn=new_turn,
                                      projectile=projectile,
                                      air_resistance=air_resistance)[0]

            # Попали или нет
            result = projectile.inTheTarget(target=target)

            # Записываем.
            file_writer.writerow([i,
                                  error_inclination_value,
                                  error_turn_value,
                                  error_speed_value,
                                  new_inclination,
                                  new_turn,
                                  projectile.initial_speed,
                                  moving_length,
                                  projectile.position[0],
                                  projectile.position[1],
                                  result])

            # Сейчас снаряд с новой скоростью. Необходимо вернуть изначально точное значение.
            projectile.initial_speed = speed_save
