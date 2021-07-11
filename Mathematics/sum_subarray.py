#Sub array

def sum_subarray(input):
    sub_array = []
    for j in range(len(input)):
        for i in range(j, len(input)):
            sub_array.extend(input[j : i + 1])

    print(sub_array)
    return sum(sub_array)

def sum_subarray_fast(input):
    total = 0
    for index, value in enumerate(input):
        total += value * (index + 1) * (len(input) - index)

    return total

print(sum_subarray_fast([1, 3, 7]))
