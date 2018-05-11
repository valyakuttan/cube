# util.py


class SqMatrix:
    """Square Matrix"""
    def __init__(self, xss):
        """
        The argument xss must be a multilist with equal
        rows and columns.
        """
        self._mat = xss

    @property
    def mlist(self):
        return self._mat

    @mlist.setter
    def mlist(self, xss):
        self._mat = xss

    @property
    def toString(self):
        return "\n".join(self.formattedList)

    @property
    def formattedList(self):
        xs = [formatList(xs) for xs in self._mat]
        n = len(xs[0]) if xs else 0
        start = [" " + "-" * (n - 2) + " "]
        seps = [" " + "-" * (n - 2) + " "] * n
        ys = []
        for x, y in zip(xs, seps):
            ys += [x, y]
        return start + ys

    @property
    def rotate(self):
        "Rotate a matrix 90 degrees clockwise."
        xs = self.mlist
        self.mlist = [list(x) for x in zip(*reversed(xs))]

    @property
    def transpose(self):
        """
        Return transpose of this matrix.

        >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> s = SqMatrix(xs)
        >>> t = s.transpose
        >>> t.mlist
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        >>> s == s.transpose.transpose
        True

        >>> s == t.transpose
        True
        """
        xss = [list(xs) for xs in zip(*self._mat)]
        return SqMatrix(xss)

    def setColumnSlice(self, col_slice, xss):
        """
        Replace columns for the slice col_slice with
        contents of xss.

        >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> s = SqMatrix(xs)
        >>> s.mlist
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        >>> s.getColumnSlice(slice(1, 2))
        [[2, 5, 8]]

        >>> s.setColumnSlice(slice(1, 2), [[5, 5, 5]])
        >>> s.getColumnSlice(slice(1, 2))
        [[5, 5, 5]]

        >>> s.mlist
        [[1, 5, 3], [4, 5, 6], [7, 5, 9]]
        """
        tmp = self.transpose
        tmp.setRowSlice(col_slice, xss)
        self.mlist = tmp.transpose.mlist

    def getColumnSlice(self, col_slice):
        """
        Get columns for the slice.

        >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> s = SqMatrix(xs)

        >>> s.getColumnSlice(slice(1, 3))
        [[2, 5, 8], [3, 6, 9]]
        >>> s._mat
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
        return self.transpose.getRowSlice(col_slice)

    def setRowSlice(self, row_slice, xss):
        """
        Replace rows from start to end with the
        contents of xss.
        Note: end - start == len(xss) && every list
        in xss have the size equal to that of the _matrix.

        >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> s = SqMatrix(xs)

        >>> s.mlist
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        >>> s.getRowSlice(slice(1, 2))
        [[4, 5, 6]]

        >>> s.setRowSlice(slice(1, 2), [[5, 5, 5]])
        >>> s.getRowSlice(slice(1, 2))
        [[5, 5, 5]]

        >>> s.mlist
        [[1, 2, 3], [5, 5, 5], [7, 8, 9]]
        """
        self._mat[row_slice] = xss if self._mat[row_slice] else []

    def getRowSlice(self, row_slice):
        """
        Get rows from start to end.

        >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> s = SqMatrix(xs)

        >>> s.getRowSlice(slice(1, 3))
        [[4, 5, 6], [7, 8, 9]]
        >>> s._mat
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
        return self._mat[row_slice]

    @property
    def size(self):
        """
        >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> s = SqMatrix(xs)
        >>> s.size
        3
        """
        return len(self._mat)

    @property
    def clone(self):
        return SqMatrix([xs[::] for xs in self._mat])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __str__(self):
        return str(self.mlist)


def formatList(xs, start="| ", end=" |", sep=" | "):
    return start + sep.join(str(e) for e in xs) + end
