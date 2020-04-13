def compress(iterable, mask):
    for pos in range(len(mask)):
        if mask[pos] is True:
            yield iterable[pos]


print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
compress_gen = compress(["Ivo", "Rado", "Panda"], [False, False, True])
print(next(compress_gen))
