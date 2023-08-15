# code on GitHub at ./snippets/rps.py
from random import choice; one_line_rps_nightmare_with_memory_and_input_check_v03 = [
    get_inp := lambda usr_inp='foobar': range(int(usr_inp)) if usr_inp.isdigit() else get_inp(input("Number of games to play? ")),
    display := lambda xyz: print(f"{'WinLossTie'[xyz[0]:xyz[1]]}: {usr_inp.capitalize()} vs {get_cpu}"),
    games := [[display((7,256)), 0][1]
            if (get_cpu := choice(rps := (prompt := "Choose: Rock Paper Scissors  ").split()[1:])).lower() ==
               (usr_inp := (evl_play := lambda usr_inp: usr_inp
                if usr_inp.capitalize() in rps
                else evl_play(input(prompt)))('-e')).lower()
            else ([display((-0,3)), 1][1]
                if ({k: ['s', 'k', 'r'][i] for i, k in enumerate([i[-1] for i in rps])})[usr_inp[-1]] == get_cpu[-1]
                else [display((3,7)), 0][1])
     for i in get_inp()],
    print(f'Game Over: {sum(games)} wins in {len(games)} games.')
]  # noqa