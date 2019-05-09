import time


def main():
    t1 = time.time()
    i = 9
    while True:
        i += 2
        if format(i, 'd') != format(i, 'd')[::-1]:
            continue
        if format(i, 'b') != format(i, 'b')[::-1]:
            continue
        if format(i, 'o') != format(i, 'o')[::-1]:
            continue
        print("Result-> 10:{}, 2:{}, 8:{}".format(format(i, 'd'), format(i, 'b'), format(i, 'o')))
        break
    t2 = time.time()
    print('Elapse-> {}'.format(t2 - t1))


if __name__ == '__main__':
    main()
