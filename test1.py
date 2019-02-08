from collections import deque

# https://docs.python.org/3/tutorial/datastructures.html
# queues
# stacks
# hashmaps / dicts

def main():
    print('hello, world!')
    aList = []        # creates a new list
    #aList = list()    # creates a new list
    aList.append('a') # to add to end of list
    aList+='b'        # also appends to end of list 
    print('printing contents of aList...')
    for c in aList:
        print(c)
    # lists can also
    #   append(x)
    #   extend(iterable)
    #   insert(i,x)
    #   remove(x)
    #   pop([i])
    #   clear()
    #   index(x, [start], [end])
    #   count(x)
    #   sort(key=None, reverse=False)
    #   copy()

    # Using lists as stacks
    stack = [3,4,5]
    stack.append(6)
    stack.append(7)
    print('printing stack...')
    print(stack)
    print('popping stack...')
    print(stack.pop())
    print('printing stack...')
    print(stack)
    print('popping stack...')
    print(stack.pop())
    print('printing stack...')
    print(stack)

    # Using lists as queues
    queue = deque(['Mike', 'John', 'Adrian'])
    queue.append('Terry')
    #queue+='Harry'
    print('printing queue...')
    print(queue)
    print('dequeing queue...')
    print(queue.popleft())
    print('printing queue...')
    print(queue)
    print('dequeing queue...')
    print(queue.popleft())
    print('printing queue...')
    print(queue)

if __name__ == '__main__':
    main()

