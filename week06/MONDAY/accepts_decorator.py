def accepts(*args1):
    def inner(func):
        def accepted(*args2):
            for elem1, elem2 in zip(args1, args2):
                if elem1 != type(elem2):
                    raise TypeError('Argument {e2} of {fn} is not {e1_name}!'.format(e2=elem2,
                                    fn=func.__name__, e1_name=elem1.__name__))
            return func(*args2)
        return accepted
    return inner


if __name__ == '__main__':
    @accepts(str)
    def say_hello(name):
        return "Hello, I am {}".format(name)
    say_hello(4)

    @accepts(str, int)
    def deposit(name, money):
        print("{} sends {} $!".format(name, money))
    deposit("Marto", 10)
