import unittest


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


def product_array_no_div(numbers):
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