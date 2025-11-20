def calc_mandelbrot_steps(c: complex, max_steps: int) -> int:
    z = 0 + 0j
    for step in range(max_steps):
        if abs(z) > 2:
            return step
        z = z * z + c
    return max_steps


def generate_matrix(
    xmin: float,
    xmax: float,
    width: int,
    ymin: float,
    ymax: float,
    height: int,
    *,
    max_steps: int,
) -> list[list[int]]:
    matrix: list[list[int]] = []
    for iy in range(height):
        row = []
        y = ymin + (ymax - ymin) * iy / (height - 1)
        for ix in range(width):
            x = xmin + (xmax - xmin) * ix / (width - 1)
            c = complex(x, y)
            steps = calc_mandelbrot_steps(c, max_steps)
            row.append(steps)
        matrix.append(row)
    return matrix
