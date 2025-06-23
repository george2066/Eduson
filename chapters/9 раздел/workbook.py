from colorama import Back, Style
winner = {
        'X':[],
        'O':[]
    }

def draw_lattice(integer):
    create_cell = lambda column, row: Back.YELLOW + ('___|' if row != integer - 1 else '   |') + Style.RESET_ALL if column != integer - 1 else Back.YELLOW + ('___' if row != integer - 1 else '   ') + Style.RESET_ALL
    lattice = [[create_cell(column, row) for column in range(integer)] for row in range(integer)]
    return lattice

def show_lattice(lattice):
    for row in lattice:
        print(''.join(row))

def step(sign, lattice):
    row = int(input(f"В какую строку хотите поставить свой {sign}? "))

    if row > len(lattice):
        print(f"Строка должна быть меньше {len(lattice)}")
        step(sign, lattice)

    column = int(input(f"В какой столбец хотите поставить свой {sign}? "))

    if column > len(lattice):
        print(f"Столбец должен быть меньше {len(lattice)}")
        step(sign, lattice)

    winner.get(f'{sign}').append([row - 1, column - 1])

    cell = (f'_{sign}_|' if row != len(lattice) else f' {sign} |') if column < len(lattice) else (f'_{sign}_' if row != len(lattice) else f' {sign} ')
    lattice[row - 1][column - 1] = (Back.BLUE if sign == 'X' else Back.MAGENTA) + cell + Style.RESET_ALL
    show_lattice(lattice)
    return lattice

def positions_win(lattice):
    cells = len(lattice)
    integer = cells - 1
    wins = ([[[row, column] for column in range(cells)] for row in range(cells)])
    wins += [[[cell, cell] for cell in range(cells)]]
    wins += [[[integer - column, column] for column in range(cells)]]
    wins += [[[row, column] for row in range(cells)] for column in range(cells)]
    return wins

def tic_tac_toe():
    count = 0
    lattice = draw_lattice(int(input('Какую решётку вы хотите нарисовать? ')))
    wins = positions_win(lattice)

    while True:
        count += 1
        sign = 'O' if count % 2 == 0 else 'X'
        lattice = step(sign, lattice)
        list_sign = winner.get(f'{sign}')


        if len(list_sign) >= len(lattice):
            list_sign_set = set(map(tuple, list_sign))
        
            if any(list_sign_set == set(map(tuple, win)) for win in wins):
                print(f'{sign} победил!')
                show_lattice(lattice)
                return

tic_tac_toe()
