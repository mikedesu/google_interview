# Tuples

def main():
    t0 = 1, 2, 3
    t1 = tuple([4,5,[6,7,8]])
    print('printing t0...')
    print(t0)
    print('printing t1...')
    print(t1)
    
    try:
        t0[0] = 2
    except TypeError as e:
        print('TypeError: %s' % e)

    try:
        t1[2][0] = 2
    except TypeError as e:
        print('TypeError: %s' % e)

    print('printing t1...')
    print(t1)
    print('----------')


if __name__=='__main__':
    main()
