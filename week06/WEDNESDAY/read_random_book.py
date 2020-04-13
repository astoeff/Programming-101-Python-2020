from book_generator import generate_book
from book_reader import read_book, chapter_generator
import subprocess


def read_random_book_while_it_is_still_generated(book, chapters):
    next(book)
    next(book)
    curr = chapter_generator()
    print(next(curr))
    next(book)
    print(next(curr))
    next(book)
    print(next(curr))
    print(next(curr))
    # next(book)
    # curr = chapter_generator()
    # print(next(curr))
    # chs = 0
    # while True:
    #     if chs == chapters - 1:
    #         break
    #     next(book)
    #     print(next(curr))
    #     chs += 1


    # for chapter in book:
    #     # curr = chapter_generator()
    #     print(next(curr))
    # curr = chapter_generator()
    # next(book)
    # print(next(curr))
    # next(book)
    # print(next(curr))
    # # # next(book)
    # # for chapter in book:
    # #     print('Hello')
    # #     print(next(chapters))
    # chapters_passed = 0
    # while True:
    #     if chapters_passed == chapters:
    #         break
    #     next(book)
    #     print(next(curr))

    # next(book)
    # next(book)
    # # next(book)
    # # subprocess.call(['cat', 'book.txt'])
    # chapters = chapter_generator()
    # print(next(chapters))
    # print(next(chapters))
    # print(next(chapters))



if __name__ == '__main__':
    book = generate_book('My first book', 4, 3)
    read_random_book_while_it_is_still_generated(book, 4)
