def is_valid(board, row, col, num):
    # Verifica se o número já está presente na linha
    for i in range(9):
        if board[row][i] == num:
            return False

    # Verifica se o número já está presente na coluna
    for i in range(9):
        if board[i][col] == num:
            return False

    # Verifica se o número já está presente na subgrade 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    # Encontra uma célula vazia no tabuleiro
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Representa uma célula vazia
                # Tenta preencher a célula com números de 1 a 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # Se o número é válido, coloca-o na célula
                        board[row][col] = num

                        # Recursivamente tenta preencher o restante do tabuleiro
                        if solve_sudoku(board):
                            return True

                        # Se não for possível, volta atrás (backtracking)
                        board[row][col] = 0

                # Se nenhum número é válido, retorna False (solução impossível)
                return False

    # Se o tabuleiro está completo, retorna True
    return True


def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()


# Exemplo de tabuleiro de Sudoku a ser resolvido (0 representa células vazias)
sudoku_board = [
    [0, 5, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 2, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [7, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 6],
    [2, 0, 0, 0, 6, 0, 0, 8, 0],
    [0, 0, 0, 0, 5, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0]
]

# Resolve o Sudoku e imprime o tabuleiro solucionado
if solve_sudoku(sudoku_board):
    print("Sudoku resolvido:")
    print_board(sudoku_board)
else:
    print("Não há solução para este Sudoku.")
