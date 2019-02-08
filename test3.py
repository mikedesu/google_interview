def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print('%d ' % col, end='')
        print()

def main():
    print('hello, world!')
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print('printing matrix...')
    print_matrix(matrix)
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print('printing transposed...')
    print_matrix(transposed)
    zipped = list(zip(*matrix)) # apparently zip does something similar...
    print('printing zipped...')
    print_matrix(zipped)

if __name__ == '__main__':
    main()

