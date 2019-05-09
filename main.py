def main():
    i = 10
    while True:
        i += 1
        str_2 = format(i, 'b')
        str_8 = format(i, 'o')
        str_10 = format(i, 'd')

        if str_2 == str_2[::-1] and str_8 == str_8[::-1] and str_10 == str_10[::-1]:
            print("10:{}, 2:{}, 8:{}".format(str_10, str_2, str_8))
            break


if __name__ == '__main__':
    main()
