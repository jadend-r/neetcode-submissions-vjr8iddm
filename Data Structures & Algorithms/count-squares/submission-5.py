class CountSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.pointCount[(x, py)] * self.pointCount[(px, y)]
        return res
