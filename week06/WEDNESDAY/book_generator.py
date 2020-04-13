import random


def generate_book(title, chapters_count, words_count):
    with open('book.txt', 'w') as f:
        f.write(title + '\n\n')
    for chapter_number in range(chapters_count):
        with open('book.txt', 'a') as f:
            f.write('# Chapter ' + str(chapter_number + 1) + '\n')
            words = open('words.txt').read().splitlines()
            words_passed = 0
            words_before_dot = random.randint(2, 10)
            for word_number in range(words_count):
                word = random.choice(words)
                if words_passed == 0:
                    word = word[0].upper() + word[1:]
                f.write(word + ' ')
                if words_passed == words_before_dot:
                    f.write('\b. ')
                    words_passed = 0
                    words_before_dot = random.randint(2, 10)
                else:
                    words_passed += 1
            f.write('\b.')
            f.write('\n\n')
            f.close()
            print('BASTUN')
            yield


if __name__ == '__main__':
    title = 'Random book'
    chapters_count = 20
    words_count = 2
    gen = generate_book(title, chapters_count, words_count)
    next(gen)
    next(gen)
    next(gen)
