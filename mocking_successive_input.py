import pytest
import main


'''
The student's game was designed to request user input until a valid input was 
provided.

How could we then mock an arbitrary number of successive inputs, that were then
followed by a valid input (allowing the program to break the loop)?

This solution should probably be turned into a few different tests, but it does 
provide the means to test captured output, as well as test mocked input.
'''


def test_user_input_1(capfd):
    # setup game state
    class_instance = main.TTTgame()
    board_copy_for_test = class_instance.board[:]
    board_copy_for_test[0][0] = 'O'

    # use a generator to first input '0', then '1'
    generator = (x for x in ['0', '1'])
    main.input = lambda x: next(generator)

    class_instance.enter_move()
    captured = capfd.readouterr()[0]  # reads print() output; [1] is error out

    assert board_copy_for_test == class_instance.board
    assert captured == 'Not a free space\n'
    for i in range(3):
        for j in range(3):
            if i == j == 0 or (i == 0 and j == 1):
                assert type(class_instance.board[i][j]) is str
                continue
            assert type(class_instance.board[i][j]) is int
