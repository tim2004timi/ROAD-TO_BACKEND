class Point:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"{str(self.x)} {str(self.y)} {str(self.z)} {str(self.w)}"


def is_pair(p1: Point, p2: Point):
    count = 0

    if p1.x != p2.x:
        count += 1
    if p1.y != p2.y:
        count += 1
    if p1.z != p2.z:
        count += 1
    if p1.w != p2.w:
        count += 1

    if count > 1:
        return True
    return False


def func(points):
    end = len(points) - 1
    i = 0
    while i < end:
        j = i + 1
        while j < len(points):
            if not is_pair(points[i], points[j]):
                points.pop(j)
                j -= 1
                end -= 1
            j += 1
        i += 1


def main():
    points = []

    for x in range(10):
        for y in range(10):
            for z in range(10):
                for w in range(10):
                    points.append(Point(x, y, x, w))

    func(points)

    print(len(points))


if __name__ == "__main__":
    main()
