class Display:
    def __init__(self):
        self.stage = 0
        self.noose = 'Ô'
        self.progression = ['@', '|', '/', '\\', '/', '\\']
        self.indices = list()

        # [(2, 6), (3, 6), (4, 5), (4, 7), (3, 5), (3, 7)]
        self.hang_man = [
            [' ', ' ', '╔', '═', '═', '═', '╗', ' ', ' ', ' '],
            [' ', ' ', '║', ' ', ' ', ' ', '│', ' ', ' ', ' '],
            [' ', ' ', '║', ' ', ' ', ' ', '0', ' ', ' ', ' '],  # 2 (6)
            [' ', ' ', '║', ' ', ' ', '4', '1', '5', ' ', ' '],  # 3 (5, 6, 7)
            [' ', ' ', '║', ' ', ' ', '2', ' ', '3', ' ', ' '],  # 5 (5, 7)
            ['═', '═', '╩', '═', '═', '═', '═', ' ', ' ', ' '],
         ]

        # find the indices for 0-5
        height = len(self.hang_man)
        width = len(self.hang_man[0])
        while len(self.indices) < len(self.progression):
            for i in range(height):
                for j in range(width):
                    next_char = self.hang_man[i][j]
                    next_numb = str(len(self.indices))
                    if next_char == next_numb:
                        self.indices.append((i, j))

        for i, j in self.indices:
            self.hang_man[i][j] = ' '

        # add noose
        r = self.indices[0][0]
        c = self.indices[0][1]
        self.hang_man[r][c] = self.noose

    def render(self):
        display_string = ''
        for row in self.hang_man:
            display_string += ''.join(row)
            display_string += '\n'
        return display_string

    def update(self, wrong_guesses: int = None):
        if wrong_guesses is not None:
            while self.stage < wrong_guesses:
                next_char = self.progression[self.stage]
                next_row, next_col = self.indices[self.stage]
                self.hang_man[next_row][next_col] = next_char
                self.stage += 1
        return self.render()


if __name__ == '__main__':
    out = Display()
    display_me = out.update(wrong_guesses=0)
    print(display_me)
    display_me = out.update(wrong_guesses=3)
    print(display_me)
    display_me = out.update(wrong_guesses=6)
    print(display_me)
