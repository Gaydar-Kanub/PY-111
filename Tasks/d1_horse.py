def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)
    steps = [(0, 0), ]
    for st in steps:
        if st[0] + 1 < shape[0] and st[1] + 2 < shape[1]:
            steps.append((st[0] + 1, st[1] + 2))
        if st[0] + 2 < shape[0] and st[1] + 1 < shape[1]:
            steps.append((st[0] + 2, st[1] + 1))
        if st[0] - 1 >= 0 and st[1] + 2 < shape[1]:
            steps.append((st[0] - 1, st[1] + 2))
        if st[1] - 1 >= 0 and st[1] + 1 < shape[1]:
            steps.append((st[0] + 2, st[1] - 1))
    return steps


if __name__ == '__main__':
    print(calculate_paths((8, 8), (7, 7)))