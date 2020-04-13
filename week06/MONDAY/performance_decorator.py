import time


def performance(file_name):
        def inner(func):
            with open(file_name, 'a') as f:
                f.write(func.__name__ + ' was called\n')
            return func
        return inner


if __name__ == '__main__':
    @performance('log.txt')
    def something_heavy():
        time.sleep(2)
        return "I am done!"

    something_heavy()
    something_heavy()
