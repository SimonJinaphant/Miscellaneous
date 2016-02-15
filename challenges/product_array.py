import unittest


def product_array(numbers):
    """Given an numerical array, construct a product array

    :param numbers: A list of integers where each element >= 1
    :return: An integer array of the same size where the element at
    index i is the product of all elements in numbers except numbers[i]
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


def product_array_no_div(numbers):
    """Given an numerical array, construct a product array

    :param numbers: A list of integers where each element >= 1
    :return: An integer array of the same size where the element at
    index i is the product of all elements in numbers except numbers[i]
    """
    results = []
    product = 1

    for num in numbers:
        results.append(product)
        product *= num

    product = 1
    for i in xrange(len(numbers)-1, -1, -1):
        results[i] *= product
        product *= numbers[i]

    return results


class TestProductArray(unittest.TestCase):
    def test_normal(self):
        self.assertEquals(product_array([2, 1, 3, 4, 1, 2]), [24, 48, 16, 12, 48, 24])
        self.assertEqual(product_array([10, 3, 5, 6, 2]), [180, 600, 360, 300, 900])

    def test_no_div_normal(self):
        self.assertEquals(product_array_no_div([2, 1, 3, 4, 1, 2]), [24, 48, 16, 12, 48, 24])
        self.assertEqual(product_array_no_div([10, 3, 5, 6, 2]), [180, 600, 360, 300, 900])

if __name__ == "__main__":
    unittest.main