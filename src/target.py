class Target:
    """Мишень. В нее стреляем."""

    def __init__(self, coords: tuple[tuple[(float, float)]]):
        """Создание мишени."""
        # Координаты вершин прямоугольника, определяющие границы мишени.
        self.point1, self.point2, self.point3, self.point4 = coords
