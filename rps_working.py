# # code on GitHub at ./snippets/rps.py
# from random import choice; one_line_rps_with_memory_and_input_check_ver_02 = \
# [evl_inp_gme := lambda usr_inp: range(int(usr_inp)) if usr_inp.isdigit() else evl_inp_gme(input("Number of games to pla\
# y? ")), scr := [], [print([f"Tie: {usr.capitalize()} vs {cho}", scr.append(0)][0] if (cho := choice(rps := (pro := "Cho\
# ose: Rock Paper Scissors  ").split()[1:])).lower() == (usr := (evl_inp_cho := lambda usr_inp: usr_inp if usr_inp.
# capitalize() in rps else evl_inp_cho(input(pro)))('-e')).lower() else ([f"Win {usr.capitalize()} vs {cho}", scr.append
# (1)][0] if ({k: ['s', 'k', 'r'][i] for i, k in enumerate([i[-1] for i in rps])})[usr[-1]] == cho[-1] else [f"Lose \
# {usr.capitalize()} vs {cho}", scr.append(0)][0])) for i in evl_inp_gme('foobar')], print(f'Game Over: {sum(scr)} wins i\
# n {len(scr)} games.')]  # noqa


# code on GitHub at ./snippets/rps.py
from random import choice; one_line_rps_nightmare_with_memory_and_input_check_v03 = [
    get_inp := lambda usr_inp='foobar': range(int(usr_inp)) if usr_inp.isdigit() else get_inp(input("Number of games to play? ")),
    display := lambda xy: print(f"{'WinLossTie'[xy[0]:xy[1]]}: {usr_inp.capitalize()} vs {get_cpu}"),
    games := [[display((7,256)), 0][1]
            if (get_cpu := choice(rps := (prompt := "Choose: Rock Paper Scissors  ").split()[1:])).lower() ==
               (usr_inp := (evl_play := lambda usr_inp: usr_inp
                                                        if usr_inp.capitalize() in rps
                                                        else evl_play(input(prompt)))('-e')).lower()
            else ([display((-0,3)), 1][1]
                if ({k: ['s', 'k', 'r'][i] for i, k in enumerate([i[-1] for i in rps])})[usr_inp.lower()[-1]] == get_cpu[-1]
                else [display((3,7)), 0][1])
     for i in get_inp()],
    print(f'Game Over: {sum(games)} wins in {len(games)} games.')
]  # noqa
print(one_line_rps_nightmare_with_memory_and_input_check_v03)
print(games)



# bug
'''
Number of games to play? 3
Choose: Rock Paper Scissors  rock
Loss: Rock vs Paper
Choose: Rock Paper Scissors  ScissorS
Traceback (most recent call last):
  File "C:\\Users\Computer\github\snippets\\rps_working.py", line 16, in <module>
    games := [[display((7,256)), 0][1]
  File "C:\\Users\Computer\github\snippets\\rps_working.py", line 22, in <listcomp>
    if ({k: ['s', 'k', 'r'][i] for i, k in enumerate([i[-1] for i in rps])})[usr_inp[-1]] == get_cpu[-1]
KeyError: 'S'

Process finished with exit code 1
'''
