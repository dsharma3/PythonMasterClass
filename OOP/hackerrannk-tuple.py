if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    mylist = []
    for i in integer_list:
        mylist.append((i))
    print(hash(tuple(mylist)))