import time


def main():
    t1 = time.time()
    i = 9
    while True:
        i += 2
        for radix in ['d', 'b', 'o']:
            if format(i, radix) != format(i, radix)[::-1]:
                break
        else:
            print("Result-> 10:{}, 2:{}, 8:{}".format(format(i, 'd'), format(i, 'b'), format(i, 'o')))
            break   # while終了
    t2 = time.time()
    print('Elapse-> {}'.format(t2 - t1))


if __name__ == '__main__':
    main()
