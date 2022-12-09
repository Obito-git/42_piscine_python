class InitializationError(Exception):
    pass


class IllegalOperation(Exception):
    pass


class NotImplementedError(Exception):
    pass


class Vector:
    """
    values: list of list of floats (for row vector) or list of lists of single float (for column vector)

    shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a column vector of dimension n.
        Just consider the dimension is the number of floats (elements/coordinates) of a vector, and shape gives the layout:
        if (1, n) the vector is a row, if (n, 1) the vector is a column.
    """
    values = []
    shape = ()

    def __new__(cls, value):
        error = "To initialize vector with list you must provide list of list of floats\n (ex. [[0.0, 1.0, 2.0, " \
                "3.0]] or [[0.0], [1.0], [2.0], [3.0]]) "
        if isinstance(value, int):
            if value <= 0:
                raise InitializationError("To initialize vector with size you must use positive integer")
        elif isinstance(value, tuple):
            if len(value) != 2 or not all(isinstance(item, int) for item in value) or value[0] > value[1]:
                raise InitializationError("To initialize vector in range you must provide two int (from, to) where to "
                                          "is greater than from")
        elif isinstance(value, list):
            if len(value) == 0:
                raise InitializationError("To initialize vector with list it must be not empty")
            if len(value) == 1 and isinstance(value[0], list) and len(value[0]) != 0 and all(isinstance(item, float) for item in value[0]):
                pass
            elif all(isinstance(item, list) and len(item) == 1 and isinstance(item[0], float) for item in value):
                pass
            else:
                raise InitializationError(error)
        else:
            raise InitializationError(error)
        return object.__new__(cls)

    def __init__(self, value):
        if isinstance(value, int):
            self.values = [[float(item)] for item in range(0, value)]
            self.shape = (len(self.values), 1)
        elif isinstance(value, tuple):
            self.values = [[float(item)] for item in range(value[0], value[1])]
            self.shape = (len(self.values), 1)
        else:
            self.values = value
            if isinstance(self.values[0], list) and len(self.values) == 1:
                self.shape = (1, len(self.values[0]))
            else:
                self.shape = (len(self.values), 1)

    def dot(self, second):
        if not isinstance(second, Vector) or self.shape != second.shape:
            raise IllegalOperation("Need to provide vectors of same shape")
        if self.shape[0] == 1:
            return sum([self.values[0][i] * second.values[0][i] for i in range(self.shape[1])])
        return sum([self.values[i][0] * second.values[i][0] for i in range(self.shape[0])])

    def T(self):
        if self.shape[0] == 1:
            return Vector([[item] for item in self.values[0]])
        return Vector([[item[0] for item in self.values]])

    def __add__(self, other):
        """
        add & radd : only vectors of same shape.
        """
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise IllegalOperation("You can add only vectors of the same shape")
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] + other.values[0][i] for i in range(self.shape[1])]])
        return Vector([[self.values[i][0] + other.values[i][0]] for i in range(self.shape[0])])

    def __radd__(self, other):
        """
        add & radd : only vectors of same shape.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        sub & rsub: only vectors of same shape.
        """
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise IllegalOperation("You can sub only vectors of the same shape")
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] - other.values[0][i] for i in range(self.shape[1])]])
        return Vector([[self.values[i][0] - other.values[i][0]] for i in range(self.shape[0])])

    def __rsub__(self, other):
        """
        sub & rsub: only vectors of same shape.
        """
        return other.__sub__(self)

    def __mul__(self, other):
        """
        mul & rmul: only scalars (to perform multiplication of Vector by a scalar).
        """
        if not isinstance(other, (float, int)):
            raise IllegalOperation("You can use only scalar to multiply")
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] * other for i in range(self.shape[1])]])
        return Vector([[self.values[i][0] * other] for i in range(self.shape[0])])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        truediv : only with scalars (to perform division of Vector by a scalar).
        """
        if not isinstance(other, (float, int)):
            raise IllegalOperation("You can use only scalar for division")
        if other == 0:
            raise IllegalOperation("Really? Zero division?")
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] / other for i in range(self.shape[1])]])
        return Vector([[self.values[i][0] / other] for i in range(self.shape[0])])

    def __rtruediv__(self, other):
        """
        rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined
        here."
        """
        raise NotImplementedError("Division of a scalar by a Vector is not defined here")

    def __str__(self):
        return f"{self.values} {self.shape}"

    def __repr__(self):
        return f"{self.values} {self.shape}"
