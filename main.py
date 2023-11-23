from random import choice, sample

GAME_SYMBOLS = 'XO'


def check_diagonals(field: list[list[int]]) -> str | None:
    diagonal_1 = []
    diagonal_2 = []
    size = len(field)
    max_col = size - 1
    for i, row in enumerate(field):
        diagonal_1.append(row[i])
        diagonal_2.append(row[max_col - i])
    for symbol in GAME_SYMBOLS:
        if diagonal_1.count(symbol) == size or \
           diagonal_2.count(symbol) == size:
            return symbol


def check_winner(field: list[list[int]]) -> str | None:
    size = len(field)
    rotated_field = (list(zip(*field)))

    for symbol in GAME_SYMBOLS:

        # check columns
        for row in rotated_field: 
            symbol_count = row.count(symbol)
            if symbol_count == size:
                return symbol
        # check rows    
        for row in field:
            symbol_count = row.count(symbol)
            if symbol_count == size:
                return symbol
            
        # check diagonals
        winner = check_diagonals(field)
        if winner:
            return winner


def main():
    field_size = 3
    field = [['_'] * field_size for _ in range(field_size)]
    free_positions = [[j, i] for i in range(field_size) for j, row in enumerate(field) if not (row[i] in GAME_SYMBOLS)]
    player, cpu = sample(GAME_SYMBOLS, k=2)
    current_turn = GAME_SYMBOLS[0]
    print(f'Вы ставите {player}')
    while free_positions:
        current_field = '\n'.join([' '.join(row) for row in field])
        print(f"\nТекущее поле:\n{current_field}\n")

        if current_turn == player:
            while True:
                print('Ваш ход, кожаный! Введите координаты через пробел:')
                try:
                    coords = [int(i) for i in input().split()]
                except ValueError:
                    print('Вы ввели не числа!')
                    continue
                if len(coords) > 2:
                    print('Вы ввели больше 2-х чисел')
                    continue
                if coords not in free_positions:
                    print('Данное поле уже занято!')
                    continue
                break
        else:
            print('Ход машины!')
            coords = choice(free_positions)
            
        field[coords[0]][coords[1]] = current_turn
        winner = check_winner(field)
        if winner:
            break
        current_turn = GAME_SYMBOLS[(GAME_SYMBOLS.find(current_turn) + 1) % len(GAME_SYMBOLS)]
        free_positions = [[j, i] for i in range(field_size) for j, row in enumerate(field) if not (row[i] in GAME_SYMBOLS)]
    
    current_field = '\n'.join([' '.join(row) for row in field])
    print(f"\nТекущее поле:\n{current_field}\n")
    print('Игра закончена!\n')

    if winner:
        if winner == cpu:
            print('Машины победили, кожаный мешок!')
        else:
            print('В этот раз ты победил, кожаный мешок!')
    else:
        print('Ничья!')
    print('\n')


if __name__ == '__main__':
    main()
