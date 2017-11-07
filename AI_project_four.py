def main():
    puzz = get_puzzle()
    puzz = fill_domain(puzz)
    print_sudoku(puzz)


def fill_domain(puzzle):
    for row in puzzle:
        for index in range(0,len(row)):
            if row[index] == 0:
                row[index] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return puzzle


def print_sudoku(puzzle):
    for i in range(0, len(puzzle)):
        print(puzzle[i])


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
