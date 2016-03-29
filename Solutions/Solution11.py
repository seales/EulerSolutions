def initialize(file_p):
    arr = []
    for line in file_p:
        line = line.split()
        for num in range(len(line)):
            line[num] = int(line[num])
        arr.append(line)
    return arr

def find_max_product(numbers, element_count):

    elements_one = [0] * element_count
    elements_two = [0] * element_count
    max_product = -1
    product, index = 0, 0
    length = len(numbers)

    for i in range(length):
        for j in range(length):
            # horizontal
            elements_one[index % element_count] = numbers[i][j]
            product_one = array_product(elements_one)
            
            # vertical
            elements_two[index % element_count] = numbers[j][i]
            product_two = array_product(elements_two)
            
            if product_one > product_two:
                product = product_one
            else:
                product = product_two
            
            if product > max_product:
                max_product = product
        index += 1

    index = 0
    elements_one = [0] * element_count

    # NOTE: further reuse is possible, but it seems to take away clarity

    # search through right-diagonal
    for j in range(length):
        for i in range(length):
            if i+element_count <= length and j+element_count <= length:
                for k in range(element_count):
                    elements_one[index % element_count] = numbers[k+j][k+i]
                    product = array_product(elements_one)
                    index += 1
                if product > max_product:
                    max_product = product
            else:
                break

    index = 0
    elements_one = [0] * element_count

    # search through left-diagonal
    for j in range(length-1, -1, -1):
        for i in range(0, length):
            if i+element_count <= length and j >= element_count:
                for k in range(element_count):
                    elements_one[index % element_count] = numbers[j-k][k+i]
                    product = array_product(elements_one)
                    index += 1
                if product > max_product:
                    max_product = product
            else:
                break

    return max_product


def array_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


f = open('Problem11.txt')
number_grid = initialize(f)

assert find_max_product(number_grid, 4) == 70600674