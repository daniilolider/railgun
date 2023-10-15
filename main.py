from math import sqrt
from numpy import linspace

from src.gun import Gun
from src.projectile import Projectile
from src.target import Target
from src.environment import Environment
from src.solveDU import finding_move
from src.graphs import draw_graphs


def main():

    conditions = {
        'gun_location': [1, -2, -1, 2, 1, -2],
        'projectile_mass': 2,
        'initial_speed': 30,
        'target_coords': ((4, 12), (10, 12), (4, 8), (10, 8)),
        'air_resistance': 0.04,
        'turn_angle': 60,
        'inclination_angle': 45,
    }  # еще 3 параметра (которые на оценку отлично)

    gun_location = conditions.get('gun_location', ((0, 0), (0, 0)))
    projectile_mass = conditions.get('projectile_mass', 0)
    initial_speed = conditions.get('initial_speed', 0)
    target_coords = conditions.get('target_coords', ((0, 0), (0, 0), (0, 0), (0, 0)))
    air_resistance = conditions.get('air_resistance', 0)
    turn_angle = conditions.get('turn_angle', 0)
    inclination_angle = conditions.get('inclination_angle', 0)

    gun = Gun()
    projectile = Projectile(projectile_mass=projectile_mass, initial_speed=initial_speed)
    target = Target(coords=target_coords)
    environment = Environment()

    gun.set_location(location=gun_location)
    environment.set_K(value=air_resistance)

    gun.shoot(inclination=inclination_angle,
              turn=turn_angle,
              projectile=projectile,
              air_resistance=air_resistance)

    result = projectile.inTheTarget(target=target)

    print(f'Координаты падения снаряда - {projectile.position}')
    print(f'Попал? - {result}')

    # Для графиков.
    max_x, x, y = finding_move(m=projectile.projectile_mass,
                               k=air_resistance,
                               v0=projectile.initial_speed,
                               alpha=inclination_angle,
                               end_t=100)

    # Отберем только первые столбики для графика траектории. Берем только положительные игреки и их иксы.
    index_of_max_x = list(x[:, 0]).index(max_x)
    x_trajectory = x[:index_of_max_x, 0]
    y_trajectory = y[:index_of_max_x, 0]

    # Вторые столбики для графика скорости.
    x_speed = x[:index_of_max_x, 1]
    y_speed = y[:index_of_max_x, 1]
    speed = [sqrt(x_s ** 2 + y_s ** 2) for x_s, y_s in zip(x_speed, y_speed)]
    time = list(linspace(0, len(speed), len(speed)))

    # Вывод графиков.
    draw_graphs(x_trajectory, y_trajectory, time, speed, gun, projectile, target)


if __name__ == '__main__':
    main()