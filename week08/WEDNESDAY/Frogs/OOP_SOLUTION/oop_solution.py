from pond import Pond


if __name__ == '__main__':
    frogs_pers_side = int(input('Enter number of frogs per side: '))
    pond = Pond(frogs_pers_side)
    pond.set_pond_string()
    print(pond)
    while not pond.is_arranged():
        pond.move_frog()
        print(pond)


print('\nResult:', pond.pond_string)
print('Solved in: ', pond.steps_count)
