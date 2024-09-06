# Sudoku Solver

Este é um programa em Python que resolve um tabuleiro de Sudoku usando um algoritmo de força bruta e backtracking. O programa tenta todas as possíveis soluções para encontrar uma que satisfaça todas as regras do Sudoku.

## Como Funciona

O programa utiliza uma abordagem de "backtracking" para resolver o Sudoku. Ele tenta colocar números de 1 a 9 em células vazias do tabuleiro e verifica se o número colocado é válido de acordo com as regras do Sudoku (sem repetição na mesma linha, coluna ou subgrade 3x3). Se uma solução válida for encontrada, o programa imprime o tabuleiro resolvido.

## Estrutura do Código

- **`is_valid(board, row, col, num)`**: Função que verifica se um número pode ser colocado em uma célula específica.
- **`solve_sudoku(board)`**: Função principal que tenta resolver o Sudoku usando backtracking.
- **`print_board(board)`**: Função que imprime o tabuleiro de Sudoku de forma formatada.

## Como Usar

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/sudoku-solver.git
    ```

2. Navegue para o diretório do projeto:

    ```bash
    cd sudoku-solver
    ```

3. Execute o script em Python:

    ```bash
    python sudoku_solver.py
    ```

## Exemplo

Um exemplo de tabuleiro de Sudoku a ser resolvido é:

```plaintext
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

Após a execução, o programa exibirá o tabuleiro resolvido.


## Autor

Criado por Jean Cassiano após passar muito extresse jogando sudoku.