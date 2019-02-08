import sys

def binarySearch(strlist, p, r, target):
    if p > r:
        return -1
    q = int((p+r)/2)
    if target == strlist[q]:
        return q
    elif target < strlist[q]:
        return binarySearch(strlist, p, q-1, target)
    return binarySearch(strlist, q+1, r, target)


def mergeSort(strlist, intlist, p, r):
    if p < r:
        q = int((p+r)/2)
        mergeSort(strlist, intlist, p, q)
        mergeSort(strlist, intlist, q+1, r)
        merge(strlist, intlist, p, q, r)

def merge(strlist, intlist, p, q, r):
    n1 = q-p+1
    n2 = r-q
    strlist_left = []
    strlist_right = []
    intlist_left = []
    intlist_right = []
    i = 0
    j = 0
    k = 0
    while i < n1:
        strlist_left.append(strlist[p+i])
        intlist_left.append(intlist[p+i])
        i+=1
    while j < n2:
        strlist_right.append(strlist[q+j+1])
        intlist_right.append(intlist[q+j+1])
        j+=1
    k = p
    i = 0
    j = 0
    while k <= r:
        if i < n1 and j < n2:
            if strlist_left[i] < strlist_right[j]:
                strlist[k] = strlist_left[i]
                intlist[k] = intlist_left[i]
                i+=1
            else:
                strlist[k] = strlist_right[j]
                intlist[k] = intlist_right[j]
                j+=1
        elif i < n1:
            strlist[k] = strlist_left[i]
            intlist[k] = intlist_left[i]
            i+=1
        else:
            strlist[k] = strlist_right[j]
            intlist[k] = intlist_right[j]
            j+=1
        k+=1

def usage():
    print('Usage: python3 test6.py infile.txt word1 [word2...]')
    sys.exit(-1)

def main():
    print('len(sys.argv): %d' % len(sys.argv))
    argv_len = len(sys.argv)
    if argv_len < 3:
        usage()
    filename = sys.argv[1]
    search_list = []
    i = 2
    while i < argv_len:
        search_list.append(sys.argv[i])
        i+=1
    word_list = []
    line_number_list = []
    # Open infile
    with open(filename,'r') as infile:
        line_count = 0
        lines = infile.readlines()
        # for each line
        while line_count < len(lines):
            # for each word in the line
            for word in lines[line_count].split():
                # add the word and its line_number
                word_list.append(word)
                line_number_list.append(line_count)
            line_count += 1
        
    mergeSort(word_list, line_number_list, 0, len(word_list)-1)
    for search_word in search_list:
        index = binarySearch(word_list, 0, len(word_list), search_word)
        if index == -1:
            print('%s not found' % search_word)
        else:
            print('%s found on line %d' % (search_word, line_number_list[index]))

if __name__=='__main__':
    main()

