from bill import Bill


class BillBatch:
    def __init__(self, batch):
        if type(batch) != list:
            raise TypeError('Invalid argument given, argument needs to be of type list!')
        else:
            for bill in batch:
                if type(bill) != Bill:
                    raise TypeError('Invalid element of list given, argument needs to be list of elements of type Bill!')
        self.batch = batch

    def __len__(self):
        return len(self.batch)

    def __getitem__(self, index):
        if index in range(len(self)):
            return self.batch[index]
        else:
            raise IndexError('Index out of boundary!')

    def total(self):
        return sum(self.batch)


if __name__ == '__main__':
    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    for bill in batch:
        print(bill)

    print(sum(batch))

# A 10$ bill
# A 20$ bill
# A 50$ bill
# A 100$ bill
