# code on GitHub at ./snippets/rps.py
from random import choice; one_line_rps_with_memory_and_input_check_ver_01 = \
[(scr := []), (pro := "Choose: Rock Paper Scissors  "), evl_inp_gme := lambda usr_inp: range(int(usr_inp)) if usr_inp.
isdigit() else evl_inp_gme(input("Number of games to play? ")), [print([f"Tie: {usr.capitalize()} vs {cho}", scr.append(
0)][0] if (cho := choice(rps := pro.split()[1:])).lower() == (usr := (evl_inp_cho := lambda usr_inp: usr_inp if usr_inp.
capitalize() in rps else evl_inp_cho(input(pro)))('-e')).lower() else ([f"Win: {usr.capitalize()} vs {cho}", scr.append(
1)][0] if ({k: ['s', 'k', 'r'][i] for i, k in enumerate([i[-1] for i in rps])})[usr[-1]] == cho[-1] else [f"Lose: \
{usr.capitalize()} vs {cho}", scr.append(0)][0])) for i in evl_inp_gme('foobar')], print(f'Game Over: {sum(scr)} wins \
in {len(scr)} games.')]  # noqa
