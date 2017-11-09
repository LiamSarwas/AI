import copy


def main():
    puzz = get_puzzle()
    print()
    puzz = fill_domain(puzz)
    print_sudoku(puzz)

    puzz_next = copy.copy(puzz)
    constrain_domains(puzz_next)

    while puzz != puzz_next:
        puzz = puzz_next
        puzz_next = copy.copy(puzz)
        constrain_domains(puzz_next)

    print()
    print_sudoku(puzz)


def constrain_domains(puzzle):
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle[i])):
            if not isinstance(puzzle[i][j], int):
                new_domain = []
                neighbors = get_neighbors(i, j, puzzle)
                for value in range(1, 10):
                    if value in neighbors:
                        continue
                    else:
                        new_domain.append(value)

                # if there is only one element in the list, make the domain an int not a list
                if len(new_domain) == 1:
                    new_domain = new_domain[0]

                puzzle[i][j] = new_domain


def get_neighbors(i, j, puzzle):
    neighbors = set()

    # get neighbors in local square
    for element in get_square(i, j, puzzle):
        if isinstance(element, int):
            neighbors.add(element)

    # get neighbors in row
    for element in get_row(i, puzzle):
        if isinstance(element, int):
            neighbors.add(element)

    # get neighbors in column
    for element in get_column(j, puzzle):
        if isinstance(element, int):
            neighbors.add(element)

    return neighbors


def get_square(i, j, puzzle):
    square = []
    m = (i // 3)*3
    n = (j // 3)*3
    for a in range(0, 3):
        for b in range(0, 3):
            element = puzzle[m+a][n+b]
            square.append(element)
    return square


def get_row(m, puzzle):
    return puzzle[m]


def get_column(n, puzzle):
    column = []
    for i in range(0, len(puzzle)):
        column.append(puzzle[i][n])
    return column


def fill_domain(puzzle):
    for row in puzzle:
        for index in range(0, len(row)):
            if row[index] == 0:
                row[index] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return puzzle


def print_sudoku(puzzle):
    for i in range(0, len(puzzle)):
        for item in puzzle[i]:
            if isinstance(item, int):
                print(item, " ", end="")
            else:
                print("0", " ", end="")
        print()


def get_puzzle():
    print('It is assumed that the file with the sudoku contains one sudoku and is on the Desktop.')
    sudoku_file_in = input('What is the file name of the sudoku?')
    file = '/Users/Liam/Desktop/%s' %sudoku_file_in

    mat = []
    with open(file, 'r') as matFile:
        for line in matFile:
            row = [int(num) for num in line.strip().split(',')]
            mat.append(row)

    print_sudoku(mat)

    return mat

main()
