def max_subarray(numbers):

    lookup = [None] * len(numbers)
    lookup[0] = numbers[0]

    end = 0
    for i in xrange(1, len(numbers)):
        lookup[i] = numbers[i] + lookup[i-1]
        if lookup[i] > lookup[end]:
            end = i


    start = lookup.index(min(lookup)) + 1

    return numbers[start:end+1]

print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print max_subarray([-2, -3, 4, -1, -2, 1, 5, -3])