def find_biggest_number_in_sorted_list_less_than_given_number_and_swap_them(arr, n):
    prev = -1
    for el in arr:
        if el > n:
            break
        prev += 1
    if prev != -1:
        # swap_variable = arr[prev]
        # arr[prev] = n
        # n = swap_variable
        # arr[prev], n = n, arr[prev]
        return prev
    return prev


def find_least_number_in_sorted_list_bigger_than_given_number_and_swap_them(arr, n):
    prev = 0
    for el in arr:
        if el > n:
            break
        prev += 1
    if prev != len(arr):
        # arr[prev], n = n, arr[prev]
        # return (arr, n)
        return prev
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3]
    n = 4
    print(find_least_number_in_sorted_list_bigger_than_given_number_and_swap_them(arr, n))
    #print(find_biggest_number_in_sorted_list_less_than_given_number_and_swap_them(arr, n))
