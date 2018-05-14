# play.py


from cubies import cubies_affected, rotate_cuby
from cube import Cube, rotate_cube_face
from util import SqMatrix


def cuby_cycles(op, repeat=1):
    op_actual = op * repeat
    affected_cubies, cycles = set(cubies_involved(op)), []
    c = affected_cubies.pop()
    cycle = [c]

    while affected_cubies:
        c = apply_operation_to_cuby(c, op_actual)

        if c in cycle:
            if len(cycle) > 1:
                cycles.append(cycle)
                cycle, c = [], affected_cubies.pop()
        else:
            affected_cubies -= {c}

        cycle.append(c)

    if len(cycle) > 1:
        cycles.append(cycle)

    return cycles


def cubies_involved(op):
    affected = set()
    for r in op:
        affected |= set(cubies_affected(r))

    return list(affected)


def apply_operation_to_cuby(cuby, op):
    cby = cuby
    for r in op:
        cby = rotate_cuby(cby, r)

    return cby


def order_of_face_operation(op):
    c, d = rcube(), rcube()

    i = 1
    apply_face_operation(c, op)
    while c != d:
        i += 1
        apply_face_operation(c, op)

    print("order of face operation: ", op, " is ", i)


def repeat_face_operation(cube, op, n):
    for _ in range(n):
        apply_face_operation(cube, op)


def apply_face_operation(cube, op):
    for r in op:
        rotate_cube_face(cube, r)


def rcube():
    return Cube()


def display_cube(cube):
    def rrotate(mat):
        mat.rotate
        mat.rotate
        mat.rotate

    xss = cube.faces
    tmps = [SqMatrix(xs) for xs in xss]
    f, b, l, r, t, d = tmps

    l.rotate  # rotate left face clockwise

    rrotate(r)  # rotate right face counter clockwise

    b.rotate  # rotate back 180 degrees clockwise
    b.rotate

    d.rotate  # rotate back 180 degrees clockwise
    d.rotate

    yss = [tmp.formattedList for tmp in tmps]
    front, back, left, right, top, bottom = yss

    n, m = len(front[1]), len(front)
    blank = [" " * n] * m
    margin = ["    "] * m

    rows = [[] for _ in range(4)]

    rows[0] = zip(blank, margin, back, margin, blank)

    rows[1] = zip(left, margin, top, margin, right)

    rows[2] = zip(blank, margin, front, margin, blank)

    rows[3] = zip(blank, margin, bottom, margin, blank)

    fs = []
    for i in range(4):
        fs += zip_to_list(rows[i])

    print("\n".join(fs))


def zip_to_list(zs):
    xs = []
    for a, b, c, d, e in zs:
        xs += [a + b + c + d + e]
    return xs
