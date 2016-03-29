ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def count_letters(begin, end):
    if end > 9999 or begin < 1:
        return -1  # beyond defined interval
    word_count = 0
    for i in range(begin, end+1):  # iterate through interval
        number = str(i)
        length = len(number)
        for i in range(length):
            place = length - i - 1  # consider largest first
            if int(number[i]) == 0:
                pass  # do nothing
            elif place == 3:
                word_count += len(ones[int(number[i])]) + 8  # thousand word count
                if int(number[i+1]) == 0 == int(number[i+2]) == int(number[i+3]):
                    break  # complete
            elif place == 2:
                word_count += len(ones[int(number[i])]) + 7  # hundred word count
                if int(number[i+1]) == 0 == int(number[i+2]):
                    break  # complete
                else:
                    word_count += 3  # and word count
            elif place == 1:
                if int(number[i]) == 1 and int(number[i+1]) != 0:
                    word_count += len(teens[int(number[i+1])-1])
                    break  # complete
                else:
                    word_count += len(tens[int(number[i])-1])
            elif place == 0:
                word_count += len(ones[int(number[i])])
    return word_count

assert count_letters(1, 1000) == 21124
assert count_letters(1, 5) == 19
assert count_letters(342, 342) == 23
assert count_letters(115, 115) == 20
