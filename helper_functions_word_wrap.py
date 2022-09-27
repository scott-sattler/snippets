
class HelperFunctions:

    CODE_1 = 79  # PEP8
    CODE_2 = 99  # PEP8
    CODE_3 = 120  # black
    Code_4 = 80
    A4_IDEAL = 66  # wikipedia
    A4_LOW = 45  # wikipedia
    A4_HIGH = 75  # wikipedia
    A4_MIN_NOVICE = 34  # wikipedia (LCA)
    A4_MAX_NOVICE = 60  # wikipedia (LCA)
    ERROR_MESSAGE = 'error: invalid input'

    def word_wrap(self, text: str, line_length: int, leading_whitespace: bool = True) -> str:
        """
        design decision
        only inserts newlines and ?optional? removes leading spaces on new lines

        todo failure to precisely define specificaiton caused most issues

        :param text:
        :param line_length:
        :param leading_whitespace:
        :return:
        """

        # input check
        if len(text) < 1 or line_length < 1:
            return HelperFunctions.ERROR_MESSAGE

        breakable_chars = [' ', '\n']
        text_as_list = list(text)
        inspection_index = line_length
        newest_line_index = 0  # last_break + 1

        # two pointer approach
        # last breakable space
        last_breakable_index = None

        while inspection_index < len(text_as_list):
            text_char = text_as_list[inspection_index]

            if text_char in breakable_chars:
                last_breakable_index = inspection_index

            # break length reached
            if inspection_index - newest_line_index == line_length:
                insertion_index = None
                # perfect match
                if text_char in breakable_chars:
                    insertion_index = inspection_index
                else:
                    # previous (eg space) split
                    if last_breakable_index is not None and last_breakable_index > newest_line_index:
                        insertion_index = last_breakable_index + 1  # todo consider +1/+0 for most consistent behavior
                    # forced (eg word) split
                    else:
                        insertion_index = newest_line_index + line_length

                text_as_list.insert(insertion_index, '\n')
                newest_line_index = insertion_index + 1

                inspection_index = newest_line_index

                if leading_whitespace:
                    # removes leading whitespaces
                    while inspection_index < len(text_as_list) and text_as_list[inspection_index] == ' ':
                        del text_as_list[inspection_index]

            inspection_index += 1

        return ''.join(text_as_list)

    # has unintended behavior
    # suboptimal implementation
    def word_wrap_old(self, text: str, line_length: int) -> str:
        """
        look at multiple of line_length
        if space/newline, replace with newline
        if not space, look left until space
        if looking left sees previous break, force break

        removes new line leading whitespace
        removes trailing whitespaces
        TODO ?add? removes trailing newlines?

        :param text:
        :param line_length:
        :return:
        """

        # input check
        if len(text) < 1 or line_length < 1:
            return HelperFunctions.ERROR_MESSAGE

        breakable_chars = [' ', '\n']
        text_as_list = list(text)
        inspection_location = line_length
        new_line_index = 0  # last_break + 1

        while inspection_location < len(text_as_list):
            # look right for perfect line breaks
            if text_as_list[inspection_location] in breakable_chars:
                text_as_list[inspection_location] = '\n'
            else:
                while inspection_location > 0:
                    # look left for char (eg space) to repalce with line break
                    inspection_location -= 1
                    if text_as_list[inspection_location] in breakable_chars:
                        break

                # force break on line too long
                if inspection_location ==  new_line_index - 1:
                    inspection_location = new_line_index + line_length # forced break location
                elif inspection_location == 0:
                    inspection_location = line_length

                text_as_list.insert(inspection_location, '\n')

            new_line_index = inspection_location + 1

            # remove leading whitespace from new line
            while inspection_location + 1 < len(text_as_list) and text_as_list[inspection_location + 1] == ' ':
                del text_as_list[inspection_location + 1]

            inspection_location += line_length + 1




        return ''.join(text_as_list)



class Test():
    # format: (input text, input line length, expected output)

    # Y/N removes leading whitespaces on new line?
    # Y/N replaces trailing whitespace with newlines?

    tests = [
        # bad user input
        ("foo", 0, HelperFunctions.ERROR_MESSAGE),
        ("foo", -1, HelperFunctions.ERROR_MESSAGE),
        ("foo", -99, HelperFunctions.ERROR_MESSAGE),

        ("a", 0, HelperFunctions.ERROR_MESSAGE),
        ("a", -1, HelperFunctions.ERROR_MESSAGE),
        ("a", -99, HelperFunctions.ERROR_MESSAGE),

        ("a b", 0, HelperFunctions.ERROR_MESSAGE),
        ("a b", -1, HelperFunctions.ERROR_MESSAGE),
        ("a b", -99, HelperFunctions.ERROR_MESSAGE),

        ("", 99, HelperFunctions.ERROR_MESSAGE),
        ("", 1, HelperFunctions.ERROR_MESSAGE),
        ("", 0, HelperFunctions.ERROR_MESSAGE),
        ("", -1, HelperFunctions.ERROR_MESSAGE),
        ("", -99, HelperFunctions.ERROR_MESSAGE),

        # forced split/insert
        ("123 56789A", 4, "123 \n5678\n9A"),
        ("12 45 78 9ABC", 2, "12\n45\n78\n9A\nBC"),
        ("12345 78 ABC D E F", 1, "1\n2\n3\n4\n5\n7\n8\nA\nB\nC\nD\nE\nF"),  # +

        ("123 5 7 9", 1, "1\n2\n3\n5\n7\n9"),

        # last element (& whitespace)
        ("123 567 89A", 2, "12\n3 \n56\n7 \n89\nA"),

        # white spaces
        ("123 56   ABC  ", 3, "123\n56 \nABC"),

        # trailing newline
        ("123 567 89A\n", 3, "123\n567\n89A\n"),

        # white spaces and trailing newline
        ("123 56   ABC  ", 3, "123\n56 \nABC\n"),

        # unclassified
        ("123 5 789", 3, "123\n5 \n789"),
    ]

    # space test"
    test_case_0 = "foo     bar           test     "
    spacing = 5

    # long string of text
    long_text_1 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."


    def test(self):
        failed = 0
        for each_test in self.tests:
            text = each_test[0]
            line_length = each_test[1]
            expected_output = each_test[2]
            output = HelperFunctions().word_wrap(text, line_length)
            info = str(each_test) + ' ' + repr(str(output))
            try:
                assert output == expected_output
                print('PASS:', info)
            except AssertionError:
                print('FAIL:', info)
                failed += 1
        print(f"{len(self.tests) - failed} PASSED | {failed} FAILED")

Test().test()
