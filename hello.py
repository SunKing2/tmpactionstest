from adder import add_me


def do_main():
    result = add_me(7, 2)
    # spew short message and a addition result
    print('Hello World! The result of 7 + 2 is: ', result)


# dunder
if __name__ == '__main__':
    do_main()
