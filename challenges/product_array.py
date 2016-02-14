def product_array(numbers):
    """Generate the product array from the given list of integers

    :param numbers: The list of integers, where each element is >= 1
    :return: An list where the i-th element is the product of
    the entire numbers list excluding the element at index i
    """
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