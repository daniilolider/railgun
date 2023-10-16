import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy import linspace, arange
import csv

from .gun import Gun
from .projectile import Projectile
from .target import Target


def draw_3graphs(x_trajectory: list,
                 y_trajectory: list,
                 time: list,
                 speed: list,
                 gun: Gun,
                 projectile: Projectile,
                 target: Target
                 ) -> None:
    """
    Рисует графики: траектории полёта снаряда, скорости снаряда
    и иллюстрацию расположения стартовой точки, мишени и точки падения снаряда.

    :param x_trajectory: Координаты x для графика траектории.
    :param y_trajectory: Координаты y для графика траектории.
    :param time: Время для графика скорости.
    :param speed: Скорость для графика скорости.
    :param gun: Пушка, из которой стреляли.
    :param projectile: Снаряд, которым стреляли.
    :param target: Мишень, в которую стреляли.
    :return: None.
    """

    plt.figure()

    # Первый график.
    plt.subplot2grid((2, 2), (0, 0), colspan=2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Траектория полета снаряда', fontsize=20)
    plt.xticks(linspace(0, max(x_trajectory), 12))
    plt.yticks(linspace(0, max(y_trajectory), 10))
    plt.plot(x_trajectory, y_trajectory)
    plt.grid()

    # Второй.
    plt.subplot2grid((2, 2), (1, 0), colspan=2)
    plt.xlabel("t")
    plt.ylabel("V(t)")
    plt.title('Скорость снаряда', fontsize=20)
    plt.xticks(linspace(0, max(time), 12))
    plt.yticks(linspace(0, max(speed), 12))
    plt.plot(time, speed, color='red')
    plt.grid()

    # Увеличиваем расстояние между первыми двумя графиками.
    plt.subplots_adjust(hspace=0.5)

    # Третий
    # Координаты точек: первые 4 - мишени, пятая - расположение пушки, 6 - расположение снаряда после выстрела.
    x_points = (target.point1[0], target.point2[0], target.point3[0], target.point4[0], gun.x, projectile.position[0])
    y_points = (target.point1[1], target.point2[1], target.point3[1], target.point4[1], gun.y, projectile.position[1])
    colors = ('g', 'g', 'g', 'g', 'b', 'r')  # Цвета точек.

    # Длину осей и расстояние между метками галочек.
    xmin, xmax, ymin, ymax = -min(x_points) - 5, max(x_points) + 5, -min(y_points) - 5, max(y_points) + 5
    ticks_frequency = 1  # Масштаб на осях.

    # Создаем полотно, на котором рисуем.
    fig, ax = plt.subplots(figsize=(10, 10))

    # Рисуем область мишени.
    rectangle = [target.point1, target.point3, target.point4, target.point2]  # Задаём область точками.
    ax.add_patch(mpatches.Polygon(rectangle, color='lightgreen'))  # Красим эту область.

    # Ставим точки и сразу красим их.
    ax.scatter(x_points[:4], y_points[:4], c=colors[:4])
    ax.scatter(x_points[4], y_points[4], c=colors[4], marker='^')
    ax.scatter(x_points[5], y_points[5], c=colors[5], marker='*')

    # Добавляем текст к объектам.
    ax.text(gun.x + 0.2, gun.y + 0.2, 'ПУШКА')
    ax.text(x_points[0] + 0.2, y_points[0] + 0.2, 'МИШЕНЬ')
    ax.text(x_points[-1] + 0.2, y_points[-1] + 0.2, 'СНАРЯД')

    # Устанавливаем длину осей.
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    # Ставим оси по центру графика.
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Убираем верхнею и правую границу графика.
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Добавляем название осей на их концы.
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=1)

    # Добавляем метки на оси в соответствии с масштабом.
    x_ticks = arange(xmin, xmax + 1, ticks_frequency)
    y_ticks = arange(ymin, ymax + 1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Уплотняем сетку на заднем фоне. Ничего не поменяет, если масштаб 1.
    ax.set_xticks(arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(arange(ymin, ymax + 1), minor=True)

    # Рисуем сетку на заднем фоне.
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Добавляем стрелки на концы осей.
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot(1, 0, marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot(0, 1, marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    plt.title('Иллюстрация эксперимента', fontsize=20)

    plt.show()  # Выводим.
