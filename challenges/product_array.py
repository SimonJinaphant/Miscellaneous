def product_array(numbers):
    results = []
    product = 1
    for num in numbers[1:]:
        product *= num

    for i in xrange(len(numbers)-1):
        results.append(product)
        product *= numbers[i]
        product /= numbers[i+1]

    results.append(product)

    return results

print product_array([2, 1, 3, 4, 1, 2])