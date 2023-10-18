class Target:
    """Мишень."""

    def __init__(self, coords: tuple[tuple[(float, float)]]):
        """Создание мишени."""
        # Координаты вершин прямоугольника, определяющего расположение мишени.
        self.point1, self.point2, self.point3, self.point4 = coords
