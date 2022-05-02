# Python Institute ...
# erroneous = [
#     'Hello, World!',
#     'Hello, World',
#     'Hello World!',
#     'Hello World',
# ]
#
# error_input = []
# for each in erroneous:
#     error_input.append('print(' + each + ')')
#
# for i, each in enumerate(error_input):
#     try:
#         eval(each)
#     except Exception as e:
#         a = str(i)
#         b = str(each)
#         c = str(e.__class__)
#         print(f'{a:5} {b:25} {c:30}')

# for _ in range(3):
#     print('a')
#
# print(_)


# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(vals)
# print(nums)

# for i in range(2):
#     print(i)

# print(range(4))

# y = 0
# for x in range(3):
#     print("x is:", x)
#     y = x + 2
#     if False:
#         print("we are breaking the for loop!")    # noqa
#         break
# else:
#     print("foo")

#
# print(range(0, 3))
#
# [0, 1, 2]


# def my_function():
#     return True
#
# print(False and my_function())