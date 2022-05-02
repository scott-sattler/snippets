"""

"""

from typing import Optional


# find the dimensions of an n*n matrix
# TODO: rectangular work?
def recursive_dimension_finder(given_object: list, list_dimensions: Optional[list] = None):
    """
    :param given_object: matrix to inspect
    :param list_dimensions:
    :return: list containing dimensions (x, y, z, ...)
    """
    if list_dimensions is None:  # PyCharm seems to want this...
        list_dimensions = []

    if type(given_object) != list:
        if len(list_dimensions) == 0:
            raise TypeError
        else:
            return list_dimensions
    else:
        list_dimensions.append(len(given_object))
        return recursive_dimension_finder(given_object[0], list_dimensions)


# flatten dictionary with list comprehension in one line
# probably a better solution

my_dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
dict_to_list = [list(my_dict.items())[y][x] for x in [0, 1] for y in range(len(my_dict))]










