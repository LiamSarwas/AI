def main():
    puzz = get_puzzle()


def get_puzzle():
    print('It is assumed that the file with the sudoku contains one sudoku and is on the Desktop.')
    sudoku_file_in = input('What is the file name of the sudoku?')
    file = '/Users/Liam/Desktop/%s' %sudoku_file_in

    mat = []
    with open(file, 'r') as matFile:
        for line in matFile:
            row = [int(num) for num in line.strip().split(',')]
            mat.append(row)

    for i in range(0, len(mat)):
        print(mat[i])

    return mat

main()
