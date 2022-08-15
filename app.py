def max_num(*nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max

print(max_num(1, 5, 7, 3))

def mult_all(*nums):
    product = 1
    for num in nums:
        product *= num
    return product

print(mult_all(2, 4, 8))

def rev_string(string, reverse = ''):
    if len(string) > 0:
        return rev_string(string[0:-1], reverse + string[-1])
    else:
        return reverse

print(rev_string('awesome'))

def in_range(num, range = range(0, 100)):
    if num > range[0] and num < range[-1]:
        return True
    else:
        return False

print(in_range(5, range(6, 50)))

def pascal(num, triangle = [[1], [1, 1]]):
    if num < 1:
        print("Invalid number of rows")
    elif num == 1:
        print(triangle[0])
    else:
        row_num = 2
        while len(triangle) < num:
            row = []
            row_prev = triangle[row_num - 1]

            length = len(row_prev) + 1

            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_num - 1][i - 1]+triangle[row_num - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_num += 1

        for row in triangle:
            print(row)

pascal(7)