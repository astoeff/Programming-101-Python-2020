import subprocess
import sys
import time
from help_library import get_character


def wait_until_symbol_from_list_of_symbols_is_read_from_console(symbols, message):
    pressed = None
    print(message)
    while True:
        correct_symbol_read = False
        for symbol in symbols:
            if pressed == symbol:
                correct_symbol_read = True
                break
        if correct_symbol_read is True:
            return pressed
            break
        if pressed is not None:
            print(str(pressed), end='\r')
        pressed = str(get_character())[2]
        pressed = pressed.lower()


def wait_for_continue_command():
    symbol = ' '
    message = 'Press space for continue ...'
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)


def print_symbol_by_symbol_with_given_sleep(text, sleep=0.5):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00001)


def chapter_generator():
    file_number = 1
    chapter_content = ''
    while True:
        # try:
            # with open('Great Expectations/00' + str(file_number) + '.txt', 'r') as f:
            with open('book.txt', 'r') as f:
                for line in f.readlines():
                    if '# Chapter' in line:
                        yield chapter_content
                        chapter_content = line
                    else:
                        chapter_content += line
                yield chapter_content
                break
        # except Exception:
        #     yield chapter_content
        #     break
        # file_number += 1


def read_book(gen):
    for chapter in gen:
        if chapter != '':
            print(chapter)
            wait_for_continue_command()
            subprocess.call('clear')
    print('The book is read!')


if __name__ == '__main__':
    gen = chapter_generator()
    read_book(gen)
    # print(next(gen))
    # wait_for_continue_command()
    # subprocess.call('clear')
    # print(next(gen))
    # wait_for_continue_command()
    # subprocess.call('clear')
    # print(next(gen))
    # wait_for_continue_command()
    # subprocess.call('clear')
    # print(next(gen))
    # wait_for_continue_command()
    # subprocess.call('clear')
    # print(next(gen))
