from src.gun import Gun
from src.projectile import Projectile
from src.target import Target
from src.environment import Environment
from src.graphs import draw_3graphs
from src.random_shoot import random_shoot
from src.print_all_information import print_all_info


def main():

    conditions = {
        'gun_location': [1, -2, -1, 2, 1, -2],
        'projectile_mass': 2,
        'initial_speed': 30,
        'target_coords': ((4, 8), (5, 12), (11, 12), (10, 8)),
        'air_resistance': 0.04,
        'direction_point': (3, 0.3),
        'turn_angle': 45,
        'inclination_angle': 30,
        'delta_turn': 5,
        'delta_inclination': 5,
        'delta_speed': 5
    }

    gun_location = conditions.get('gun_location', ((0, 0), (0, 0)))
    projectile_mass = conditions.get('projectile_mass', 0)
    initial_speed = conditions.get('initial_speed', 0)
    target_coords = conditions.get('target_coords', ((0, 0), (0, 0), (0, 0), (0, 0)))
    direction_point = conditions.get('direction_point', (0, 0))
    air_resistance = conditions.get('air_resistance', 0)
    turn_angle = conditions.get('turn_angle', 0)
    inclination_angle = conditions.get('inclination_angle', 0)
    delta_turn = conditions.get('delta_turn', 0)
    delta_inclination = conditions.get('delta_inclination', 0)
    delta_speed = conditions.get('delta_speed', 0)

    gun = Gun()
    projectile = Projectile(projectile_mass=projectile_mass, initial_speed=initial_speed)
    target = Target(coords=target_coords)
    environment = Environment()

    gun.set_location(location=gun_location)
    direction_angle = gun.get_direction(direction=direction_point)
    environment.set_K(value=air_resistance)

    moving_length, x_for_graph, y_for_graph = gun.shoot(inclination=inclination_angle,
                                                        turn=turn_angle + direction_angle,
                                                        projectile=projectile,
                                                        air_resistance=air_resistance)

    result_in_target = projectile.inTheTarget(target=target)

    # Вывод графиков.
    draw_3graphs(x_for_graph=x_for_graph,
                 y_for_graph=y_for_graph,
                 moving_length=moving_length,
                 gun=gun,
                 projectile=projectile,
                 target=target)

    # Добавляем погрешность и составляем результирующий csv файл о результатах 100 выстрелов со случайностями.
    random_shoot(gun=gun,
                 projectile=projectile,
                 target=target,
                 inclination=inclination_angle,
                 turn=turn_angle,
                 air_resistance=air_resistance,
                 delta_inclination=delta_inclination,
                 delta_turn=delta_turn,
                 delta_speed=delta_speed)

    # Выводим всю информацию об эксперименте.
    random_values = (delta_turn, delta_inclination, delta_speed)
    print_all_info(gun=gun,
                   turn=turn_angle,
                   inclination=inclination_angle,
                   projectile=projectile,
                   target=target,
                   environment=environment,
                   moving_length=moving_length,
                   result_in_target=result_in_target,
                   direction_angle=direction_angle,
                   random_values=random_values)

    # Идем в shoots_plot и запускаем.


if __name__ == '__main__':
    main()
