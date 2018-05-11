# play.py


from cube import Cube, rotate_cube_face

from util import SqMatrix


def rotate_face(cube, xs):
    for x in xs:
        rotate_cube_face(cube, x)

    display(cube)


def rcube():
    return Cube()


def display(cube):
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


def test_cube():
    fss = [["F00", "F01", "F02"],
           ["F10", "F11", "F12"],
           ["F20", "F21", "F22"]]

    bs = ["B" + x[1:] for xs in fss for x in xs]
    bss = [bs[:3], bs[3:6], bs[6:]]

    ls = ["L" + x[1:] for xs in fss for x in xs]
    lss = [ls[:3], ls[3:6], ls[6:]]

    rs = ["R" + x[1:] for xs in fss for x in xs]
    rss = [rs[:3], rs[3:6], rs[6:]]

    us = ["U" + x[1:] for xs in fss for x in xs]
    uss = [us[:3], us[3:6], us[6:]]

    ds = ["D" + x[1:] for xs in fss for x in xs]
    dss = [ds[:3], ds[3:6], ds[6:]]

    xss = [fss, bss, lss, rss, uss, dss]
    c = Cube(xss)

    display(c)
    return c
