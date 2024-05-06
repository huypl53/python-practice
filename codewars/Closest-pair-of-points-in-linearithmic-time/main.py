from typing import Any, List, Tuple, Union


class Point:
    def __init__(self, xy: Tuple[int, int]) -> None:
        self._x, self._y = xy

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, v):
        self._x = v

    @y.setter
    def y(self, v):
        self._y = v

    def get_distance(self, point) -> float:
        return (self.x - point.x) ** 2 + (self.y - point.y) ** 2

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def get_distance(point1: Point, point2: Point) -> float:
    # return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2
    return point1.get_distance(point2)


def bf_closest_pair(
    points: List[Point],
) -> Tuple[Union[Tuple[Point, Point], None], float]:
    n = len(points)
    min_d = float("inf")

    best_pairs: Union[Tuple[Point, Point], None] = None
    for i in range(0, n - 1):
        point_i = points[i]
        for j in range(i + 1, n):
            point_j = points[j]
            d_ij = get_distance(point_i, point_j)
            if min_d > d_ij:
                min_d = d_ij
                best_pairs = (point_j, point_i)

    return best_pairs, min_d


# def get_strip_closest_pair(strip_points: List[Point]):
#     min_d = float('inf')
#     strip = sorted(strip_points, key=lambda p: p.y)


def closest_pair(list_points: List[Tuple[int, int]]):

    points: List[Point] = [Point(xy) for xy in list_points]

    points = sorted(points, key=lambda p: p.x)

    def get_closest_pair(
        points: List[Point],
    ) -> Tuple[Union[Tuple[Point, Point], None], float]:
        n = len(points)
        if n < 3:  # make sure input has at least 2 points
            return tuple(points[:2]), float("inf")
            # return bf_closest_pair(points)
        mid_idx = n // 2
        left_points = points[:mid_idx]
        right_points = points[mid_idx:]

        left_pair, left_d = get_closest_pair(left_points)
        right_pair, right_d = get_closest_pair(right_points)

        pair, d = left_pair, left_d
        if right_d < d:
            pair, d = right_pair, right_d

        # strip_regions = left_pair
        strip_points: List[Point] = []
        # strip_points = points
        for point in points:
            # if point.get_distance(points[mid_idx]) < d:
            if (point.x - points[mid_idx].x) ** 2 < d:
                strip_points.append(point)

        # strip_points = sorted(strip_points, key=lambda p: p.y)
        n_s = len(strip_points)
        for i in range(0, n_s - 1):
            point_i = strip_points[i]
            for j in range(i + 1, n_s):
                point_j = strip_points[j]
                if (point_j.y - point_i.y) ** 2 > d:
                    continue
                ij_d = get_distance(point_i, point_j)
                if ij_d < d:
                    d = ij_d
                    pair = (point_i, point_j)

        # strip_pair, strip_d = bf_closest_pair(strip_points)
        # if strip_d < d:
        #     pair = strip_pair
        #     d = strip_d
        return pair, d

    pair, _ = get_closest_pair(points)
    if pair:
        return tuple((p.x, p.y) for p in pair)


if __name__ == "__main__":
    points = [
        (2, 2),  # A
        (2, 8),  # B
        (5, 5),  # C
        (6, 3),  # D
        (6, 7),  # E
        (7, 4),  # F
        (7, 9),  # G
    ]
    expected = ((6, 3), (7, 4))
    result = closest_pair(points)
    print(f"Expected: {expected}, Result: {result}")
