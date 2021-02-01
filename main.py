# Python 3 Tutorial
# for CSC481/575 Artificial Intelligence
#
# This tutorial is based on Stuart Russell's python tutorial.


def for_each():
    fruits = ['apples', 'oranges', 'pears', 'bananas']
    for fruit in fruits:
        print(fruit + ' for sale')

    fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
    for fruit, price in fruitPrices.items():
        print('%s cost %f a pound' % (fruit, price))


def hello_world():
    # Returns the string 'Hello World!'
    return "Hello World!"


def list_comprehensions():
    nums = [1, 2, 3, 4, 5, 6]
    oddNums = [x for x in nums if x % 2 == 1]
    print(oddNums)
    oddNumsPlusOne = [x + 1 for x in nums if x % 2 == 1]
    print(oddNumsPlusOne)

    strings = ['Some string', 'Art', 'Music', 'Artificial Intelligence']
    print([x.lower() for x in strings if len(x) > 5])


def quickSort(lst):
    if len(lst) <= 1:
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quickSort(smaller) + [lst[0]] + quickSort(larger)


# If using pycharm: Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(hello_world())

    # list_comprehensions()

    # for_each()

    # lst = [2, 4, 5, 1]
    # print(quickSort(lst))
