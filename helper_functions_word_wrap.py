CODE_1 = 79  # PEP8
CODE_2 = 99  # PEP8
CODE_3 = 120  # black
Code_4 = 80
A4_IDEAL = 66  # wikipedia
A4_LOW = 45  # wikipedia
A4_HIGH = 75  # wikipedia
A4_MIN_NOVICE = 34  # wikipedia (LCA)
A4_MAX_NOVICE = 60  # wikipedia (LCA)


def word_wrap(text: str, line_length: int) -> str:

    # look at multiple of line_length
    # if space, break, create new line
    # if not space, go back until space

    inspection_location = 0
    last_break = 0
    text_as_list = list(text)

    while inspection_location < len(text):
        inspection_location += line_length
        if inspection_location > len(text):
            break

        if text_as_list[inspection_location] in [' ', '\n']:
            text_as_list[inspection_location] = '\n'
            last_break = inspection_location
        else:
            # todo what about 0 ? (>= 0 or > -1)
            while inspection_location > 0 and text_as_list[inspection_location] not in [' ', '\n']:
                inspection_location -= 1

            # infinite loop when word lenth > line length
            if inspection_location ==  last_break:
                inspection_location += 1
                while True:
                    if inspection_location >= len(text):
                        return ''.join(text_as_list)

                    elif text_as_list[inspection_location] not in [' ', '\n']:
                        inspection_location += 1
                    else:
                        break

            if inspection_location > 0:
                text_as_list[inspection_location] = '\n'
                last_break = inspection_location

    return ''.join(text_as_list)



class Test():
    # space test"
    test_case_0 = "foo     bar           test     "
    spacing = 5

    # long string of text
    test_case_1 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
    spacing = None
    # has paragraphs in it

    # other tests

    # fail case 1
    text = ("123 56789A", 4)  #

    def test(self):
        # print('test')
        return None

# Test().test()

test_case_1 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

# foo = word_wrap(test_case_1, 60)
# foo = word_wrap(test_case_1, 30)
text = ("123 56789A", 4)
foo = word_wrap(text[0], text[1])
print(foo)