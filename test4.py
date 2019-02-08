

def printarray(a):
    for n in a:
        print('%d ' % n,end='')
    print()


def main():
    print('hello, world!')
    a = [0,1,2,3,4,5,6,7,8,9]
    print('printing a...')
    printarray(a)
    # delete first cell
    print('deleting first cell...')
    del a[0]
    printarray(a)
    print('deleting slice a[2:4]...')
    del a[2:4]
    printarray(a)
    print('delete whole list...')
    del a[:]
    printarray(a)


if __name__=='__main__':
    main()
