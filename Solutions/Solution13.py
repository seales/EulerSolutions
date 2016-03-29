f = open("500digits.txt")


def initialize(file_p):
    arr = []
    for line in file_p:
        arr.append(int(line))
    return arr


def summation(numbers):
    count = 0

    for number in numbers:
        count += number

    return count

nums = initialize(f)

assert summation(nums) == 5537376230390876637302048746832985971773659831892672

#NOTE: only the first ten digits are necessary for solution