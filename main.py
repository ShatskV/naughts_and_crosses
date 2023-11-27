from random import choice, sample
from typing import Union


class NaughtsAndCrosses:
    game_symbols = 'XO'

    def __init__(self, field_size: int=3) -> None:
        self.field: list[list[str]] = [['_'] * field_size for _ in range(field_size)]
        self.player, self.cpu = sample(self.game_symbols, k=2)
        self.current_turn = self.game_symbols[0]
        self.field_size: int = field_size

    @property
    def free_positions(self) -> list[list[int, int]]:
        return [[j, i] for i in range(self.field_size) for j, row in enumerate(self.field) 
                if not (row[i] in self.game_symbols)]
    
    @staticmethod
    def check_row(field: list[list[str]], symbol: str, size: int) -> Union[str,None]:
        for row in field: 
            symbol_count = row.count(symbol)
            if symbol_count == size:
                return symbol
        return None
                
    def check_winner_in_rows_and_columns(self) -> Union[str, None]:
        for symbol in self.game_symbols:
            winner_col = self.check_row(self.field, symbol, self.field_size)
            rotated_field = (list(zip(*self.field)))
            winner_row = self.check_row(rotated_field, symbol, self.field_size)
            if any([winner_col, winner_row]):
                return winner_row or winner_col
        return None
    
    def check_winner_in_diagonals(self) -> Union[str, None]:
        first_diagonal = []
        second_digonal = []
        max_col = self.field_size - 1
        for i, row in enumerate(self.field):
            first_diagonal.append(row[i])
            second_digonal.append(row[max_col - i])
        for symbol in self.game_symbols:
            if first_diagonal.count(symbol) == self.field_size or \
            second_digonal.count(symbol) == self.field_size:
                return symbol
    
    def check_winner(self) -> Union[str, None]:
        winner_diagonal = self.check_winner_in_diagonals()
        winner_row_col = self.check_winner_in_rows_and_columns()
        if any([winner_diagonal, winner_row_col]):
            return winner_row_col or winner_diagonal
        return None
            
    def print_current_field(self) -> None:
        current_field = '\n'.join([' '.join(row) for row in self.field])
        print(f"\nТекущее поле:\n{current_field}\n")

    def reset_game(self) -> None:
        print('\nНовый раунд!\n')
        self.field = [['_'] * self.field_size for _ in range(self.field_size)]
        self.player, self.cpu = sample(self.game_symbols, k=2)
        self.current_turn = self.game_symbols[0]

    def start_game(self) -> None:
        print(f'Вы ставите {self.player}')
        while self.free_positions:
            self.print_current_field()
            if self.current_turn == self.player:
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
                    if coords not in self.free_positions:
                        print('Данное поле уже занято!')
                        continue
                    break
            else:
                print('Ход машины!')
                coords = choice(self.free_positions)
            self.field[coords[0]][coords[1]] = self.current_turn
            winner = self.check_winner()
            if winner:
                break
            self.current_turn = self.game_symbols[(self.game_symbols.find(self.current_turn) + 1) % 
                                                      len(self.game_symbols)]
            
        self.print_current_field()
        print('Игра закончена!\n')

        if winner:
            if winner == self.cpu:
                print('Машины победили, кожаный мешок!')
            else:
                print('В этот раз ты победил, кожаный мешок!')
        else:
            print('Ничья!')
        print('\n')


def main():
    game = NaughtsAndCrosses()
    answer = 'y'
    while answer == 'y':
        game.start_game()
        answer = input('Хотите еще раунд? y/n ').lower()
        if answer in 'y':
            game.reset_game()


if __name__ == '__main__':
    main()




