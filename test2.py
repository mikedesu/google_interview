# List comprehensions

def main():
    print('hello world')
    squares = []
    for x in range(10):
        squares.append(x**2) # pow(x,2)
    for n in squares:
        print('%d ' % n,end='')

if __name__=='__main__':
    main()
