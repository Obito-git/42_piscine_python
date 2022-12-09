from vector import Vector
import sys


def try_vector(arg):
    try:
        Vector(arg)
        print("ok")
    except Exception as e:
        print(f"error caught ({e})")


def range_test():
    print("range_test: Expecting 7 errors")
    try_vector(-1)
    try_vector(None)
    try_vector("10")
    try_vector(tuple())
    try_vector((1, 2, 3))
    try_vector((1, "2"))
    try_vector((16, 11))
    print()


def row_test():
    print("row_test: Expecting 5 errors")
    try_vector([])
    try_vector([1])
    try_vector([1.0, 3, 4.0])
    try_vector(["1", 2, 3])
    try_vector([None])
    print()


def column_test():
    print("column_test: Expecting 6 errors")
    try_vector([[]])
    try_vector([[], [], [1.1]])
    try_vector([[1.1], [1.2], [1.3, 1.4]])
    try_vector([["Error"], ["is"], ["expected"]])
    try_vector([[1.1], 2.1, [3.1]])
    try_vector([[1], [1.2], [1.5]])
    print()


def shape_test():
    print("Shape test:")
    print("(1, 5) is expected")
    print(Vector([[1., 2., 3., 4., 5.]]).shape)
    print("\n(5, 1) is expected")
    print(Vector([[1.], [2.], [3.], [4.], [5.]]).shape)
    print("\n(100, 1) is expected")
    print(Vector(100).shape)
    print("\n(50, 1) is expected")
    print(Vector((0, 50)).shape)
    print()


def dot_test():
    print("dot_test:")
    print("\nExpected 14:")
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    print("\nExpected 18:")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    print()


def t_test():
    print("t_test:")
    print("\nExpected (1,4):")
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    print("\nExpected [[0.0], [1.0], [2.0], [3.0]]:")
    print(v2.T().values)
    print("\nExpected (4,1):")
    print(v2.T().shape)


v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[0.0], [1.0], [2.0], [3.0]])


def add_test():
    try:
        v1 + Vector([[0.0, 1.0, 2.0]])
        print("ERROR")
    except Exception as e:
        print(f"__add__: {e}")
    try:
        v1 + "String"
        print("ERROR")
    except Exception as e:
        print(f"__add__: {e}")
    try:
        v2 + v1
        print("ERROR")
    except Exception as e:
        print(f"__add__: {e}")
    try:
        "10" + v1
        print("ERROR")
    except Exception as e:
        print(f"__radd__: {e}")

    print("\n_add__ Expected [[42.0, 42.0, 42.0, 42.0]], Shape: (1, 4):")
    print(v1 + Vector([[42., 41., 40., 39.]]))

    print("\n_add__ Expected [[42.0], [42.0], [42.0], [42.0]], Shape: (4, 1):")
    print(v2 + Vector([[42.], [41.], [40.], [39.]]))

    print("\n_radd__ Expected [[42.0, 42.0, 42.0, 42.0]], Shape: (1, 4):")
    print(Vector([[42., 41., 40., 39.]]) + v1)

    print("\n_radd__ Expected [[42.0], [42.0], [42.0], [42.0]], Shape: (4, 1):")
    print(Vector([[42.], [41.], [40.], [39.]]) + v2)


def sub_test():
    # v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    # v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
    try:
        v1 - Vector([[0.0, 1.0, 2.0]])
        print("ERROR")
    except Exception as e:
        print(f"__sub__: {e}")
    try:
        v1 - "String"
        print("ERROR")
    except Exception as e:
        print(f"__sub__: {e}")
    try:
        v2 - v1
        print("ERROR")
    except Exception as e:
        print(f"__sub__: {e}")
    try:
        "10" + v1
        print("ERROR")
    except Exception as e:
        print(f"__rsub__: {e}")

    print("\n__sub__ Expected [[-42.0, -42.0, -42.0, -42.0]], Shape: (1, 4):")
    print(v1 - Vector([[42., 43., 44., 45.]]))

    print("\n__sub__ Expected [[-42.0], [-42.0], [-42.0], [-42.0]], Shape: (4, 1):")
    print(v2 - Vector([[42.], [43.], [44.], [45.]]))

    print("\n__rsub__ Expected [[42.0, 42.0, 42.0, 42.0]], Shape: (1, 4):")
    print(Vector([[42., 43., 44., 45.]]) - v1)

    print("\n__rsub__ Expected [[42.0], [42.0], [42.0], [42.0]], Shape: (4, 1):")
    print(Vector([[42.], [43.], [44.], [45.]]) - v2)


def mult_test():
    # v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    # v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
    try:
        v1 * Vector([[0.0, 1.0, 2.0]])
        print("ERROR")
    except Exception as e:
        print(f"__mult__: {e}")
    try:
        v1 * None
        print("ERROR")
    except Exception as e:
        print(f"__mult__: {e}")

    try:
        "10" * v1
        print("ERROR")
    except Exception as e:
        print(f"__rsub__: {e}")

    print("\n__mult__ Expected [[0., -1.0, -2.0, -3.0]], Shape: (1, 4):")
    print(v1 * -1)

    print("\n__mult__ Expected [[0.0], [1.5], [3.0], [4.5]], Shape: (4, 1):")
    print(v2 * 1.5)

    print("\n__mult__ Expected [[0., -1.0, -2.0, -3.0]], Shape: (1, 4):")
    print(-1 * v1)

    print("\n__mult__ Expected [[0.0], [1.5], [3.0], [4.5]], Shape: (4, 1):")
    print(1.5 * v2)


def div_test():
    v3 = Vector([[10., 20., 30., 40.]])
    v4 = Vector([[10.], [20.], [30.], [40.]])

    try:
        v3 / Vector([[0.0, 1.0, 2.0]])
        print("ERROR")
    except Exception as e:
        print(f"__truediv__: {e}")
    try:
        "String" / v3
        print("ERROR")
    except Exception as e:
        print(f"__rtruediv__: {e}")
    try:
        v3 / 0
        print("ERROR")
    except Exception as e:
        print(f"__truediv__: {e}")

    print("\n__truediv__ Expected [[5.0, 10.0, 15.0, 20.0]], Shape: (1, 4):")
    print(v3 / 2)

    print("\n__truediv__ Expected [[5.0], [10.0], [15.0], [20.0]], Shape: (4, 1):")
    print(v4 / 2)


if __name__ == "__main__":
    range_test()
    row_test()
    column_test()
    shape_test()
    dot_test()
    t_test()
    add_test()
    sub_test()
    mult_test()
    div_test()
