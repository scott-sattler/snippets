import builtins
import unittest
import main


test_list_1d = [x for x in range(1, 10)]
test_list_2d = [[(x + 3 * y) for x in range(1, 4)] for y in range(0, 3)]
test_list_3d = [[[(x + 3 * y + 9 * z) for x in range(1, 4)] for y in range(0, 3)] for z in range(0, 3)]
test_list_4d = [[[[(x + 3 * y + 9 * z + 27 * w) for x in range(1, 4)] for y in range(0, 3)]
                 for z in range(0, 3)] for w in range(0, 3)]


# TODO: test rectangular matrices
def test_recursive_dimension_finder():

    assert main.recursive_dimension_finder(test_list_1d) == [9]
    assert main.recursive_dimension_finder(test_list_2d) == [3, 3]
    assert main.recursive_dimension_finder(test_list_3d) == [3, 3, 3]
    assert main.recursive_dimension_finder(test_list_4d) == [3, 3, 3, 3]

    unittest.TestCase().assertRaises(TypeError, main.recursive_dimension_finder, 'foo')


test_recursive_dimension_finder()