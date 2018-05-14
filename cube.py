# cube.py


from util import SqMatrix


class Cube:
    """Rubik's cube"""
    def __init__(self, fs=None):
        """
        A cube is a map from direction to a SqMatrix.
        fs must be list of cube faces in the order
        [F, B, L, R, U, D]
        """
        if fs:
            zs = zip("FBLRUD", fs)
            self._cube = {f: SqMatrix(xs) for f, xs in zs}
        else:
            self._cube = {
                "F": Cube._newMatrix("R"),
                "B": Cube._newMatrix("O"),
                "L": Cube._newMatrix("G"),
                "R": Cube._newMatrix("B"),
                "U": Cube._newMatrix("W"),
                "D": Cube._newMatrix("Y"),
            }

        self._rotations = []

    @property
    def rotations(self):
        return self._rotations[::]

    @property
    def faces(self):
        """
        Return a list of the form [fs, bs, ls, rs, us, ds].
        """
        return [m.mlist for _, m in self._cube.items()]

    @faces.setter
    def faces(self, fs):
        """
        Set faces from a list of the form
        [fs, bs, ls, rs, us, ds].
        """
        zs = zip("FBLRUD", fs)
        self._cube = {f: SqMatrix(xs) for f, xs in zs}

    @property
    def formattedList(self):
        return [m.formattedList for _, m in self._cube.items()]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._cube == other._cube
        else:
            return False

    def __str__(self):
        return str(self.faces)

    @staticmethod
    def _newMatrix(e):
        xss = [[e for _ in range(3)] for _ in range(3)]
        return SqMatrix(xss)


def rotate_cube_face(cube, direction):
        """
        All rotations are clockwise quarter-turn
        Possible rotations are F, B, U, D, L, and R.

        >>> import spec
        >>> t, f = Cube(spec.TEST_CUBE), Cube(spec.TEST_CUBE)
        >>> tr= Cube(spec.TOP_ROTATED)

        >>> t == tr
        False

        >>> rotate_cube_face(t, "U")
        >>> t == tr
        True

        >>> rotate_cube_face(t, "U")
        >>> rotate_cube_face(t, "U")
        >>> rotate_cube_face(t, "U")
        >>> t == f
        True

        >>> tr= Cube(spec.BOTTOM_ROTATED)

        >>> t == tr
        False

        >>> rotate_cube_face(t, "D")
        >>> t == tr
        True

        >>> rotate_cube_face(t, "D")
        >>> rotate_cube_face(t, "D")
        >>> rotate_cube_face(t, "D")
        >>> t == f
        True

        >>> tr= Cube(spec.LEFT_ROTATED)

        >>> t == tr
        False

        >>> rotate_cube_face(t, "L")
        >>> t == tr
        True

        >>> rotate_cube_face(t, "L")
        >>> rotate_cube_face(t, "L")
        >>> rotate_cube_face(t, "L")
        >>> t == f
        True

        >>> tr= Cube(spec.RIGHT_ROTATED)

        >>> t == tr
        False

        >>> rotate_cube_face(t, "R")
        >>> t == tr
        True

        >>> rotate_cube_face(t, "R")
        >>> rotate_cube_face(t, "R")
        >>> rotate_cube_face(t, "R")
        >>> t == f
        True

        >>> tr= Cube(spec.FRONT_ROTATED)

        >>> t == tr
        False

        >>> rotate_cube_face(t, "F")
        >>> t == tr
        True

        >>> rotate_cube_face(t, "F")
        >>> rotate_cube_face(t, "F")
        >>> rotate_cube_face(t, "F")
        >>> t == f
        True

        >>> tr= Cube(spec.BACK_ROTATED)

        >>> t == tr
        False

        >>> rotate_cube_face(t, "B")
        >>> t == tr
        True

        >>> rotate_cube_face(t, "B")
        >>> rotate_cube_face(t, "B")
        >>> rotate_cube_face(t, "B")
        >>> t == f
        True
        """
        if direction == "U":
            order = "FLBR"
            d = {f: (lambda m, s: m.getRowSlice(s),
                     lambda m, s, v: m.setRowSlice(s, v))
                 for f in order}
            ss = {f: slice(0, 1) for f in order}

            _rotate_face_slice(cube, order, ss, d)
            cube._cube["U"].rotate
            cube._rotations.append("U")

        elif direction == "D":
            order = "FRBL"
            d = {f: (lambda m, s: m.getRowSlice(s),
                     lambda m, s, v: m.setRowSlice(s, v))
                 for f in order}
            ss = {f: slice(2, 3) for f in order}

            _rotate_face_slice(cube, order, ss, d)
            cube._cube["D"].rotate
            cube._rotations.append("D")

        elif direction == "L":
            order = "FDBU"
            d = {"F": (lambda m, s: reverse(m.getColumnSlice(s)),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "D": (lambda m, s: m.getColumnSlice(s),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "B": (lambda m, s: reverse(m.getColumnSlice(s)),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "U": (lambda m, s: m.getColumnSlice(s),
                       lambda m, s, v: m.setColumnSlice(s, v))}
            ss = {"F": slice(0, 1),
                  "D": slice(2, 3),
                  "B": slice(2, 3),
                  "U": slice(0, 1)}

            _rotate_face_slice(cube, order, ss, d)
            cube._cube["L"].rotate
            cube._rotations.append("L")

        elif direction == "R":
            order = "FUBD"
            d = {"F": (lambda m, s: m.getColumnSlice(s),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "D": (lambda m, s: reverse(m.getColumnSlice(s)),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "B": (lambda m, s: m.getColumnSlice(s),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "U": (lambda m, s: reverse(m.getColumnSlice(s)),
                       lambda m, s, v: m.setColumnSlice(s, v))}
            ss = {"F": slice(2, 3),
                  "D": slice(0, 1),
                  "B": slice(0, 1),
                  "U": slice(2, 3)}

            _rotate_face_slice(cube, order, ss, d)
            cube._cube["R"].rotate
            cube._rotations.append("R")

        elif direction == "F":
            order = "URDL"
            d = {"R": (lambda m, s: m.getColumnSlice(s),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "L": (lambda m, s: reverse(m.getColumnSlice(s)),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "U": (lambda m, s: m.getRowSlice(s),
                       lambda m, s, v: m.setRowSlice(s, v)),
                 "D": (lambda m, s: reverse(m.getRowSlice(s)),
                       lambda m, s, v: m.setRowSlice(s, v))}
            ss = {"L": slice(2, 3),
                  "D": slice(2, 3),
                  "R": slice(0, 1),
                  "U": slice(2, 3)}

            _rotate_face_slice(cube, order, ss, d)
            cube._cube["F"].rotate
            cube._rotations.append("F")

        elif direction == "B":
            order = "ULDR"
            d = {"R": (lambda m, s: m.getColumnSlice(s),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "L": (lambda m, s: reverse(m.getColumnSlice(s)),
                       lambda m, s, v: m.setColumnSlice(s, v)),
                 "D": (lambda m, s: m.getRowSlice(s),
                       lambda m, s, v: m.setRowSlice(s, v)),
                 "U": (lambda m, s: reverse(m.getRowSlice(s)),
                       lambda m, s, v: m.setRowSlice(s, v))}
            ss = {"L": slice(0, 1),
                  "D": slice(0, 1),
                  "R": slice(2, 3),
                  "U": slice(0, 1)}

            _rotate_face_slice(cube, order, ss, d)
            cube._cube["B"].rotate
            cube._rotations.append("B")

        else:
            pass


def _rotate_face_slice(cube, order, slices, accessors):
    first, _, _, last = order
    getter, _ = accessors[last]
    ro = order[::-1]

    tmp = getter(cube._cube[last], slices[last])
    for s, d in zip(ro[1:], ro):
        g, _ = accessors[s]
        _, f = accessors[d]
        sf, df = cube._cube[s], cube._cube[d]
        ss, ds = slices[s], slices[d]

        xss = g(sf, ss)
        f(df, ds, xss)

    _, f = accessors[first]
    f(cube._cube[first], slices[first], tmp)


def reverse(mlist):
    return [xs[::-1] for xs in mlist]
