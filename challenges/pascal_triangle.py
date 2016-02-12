def pascal_triangle(n):
    """Generate a 2D list corresponding to a pascal's triangle of height n
    :param n: The height of the triangle
    :return: Pascal's triangle as a 2D list
    """
    triangle = [[1]]

    for height in xrange(1, n):
        row = [1]
        for cell in xrange((height-1)/2):
            row.append(triangle[height-1][cell] + triangle[height-1][cell+1])

        mirrored = reversed(row)

        if height % 2 == 0:
            row.append(triangle[height-1][height/2-1] + triangle[height-1][height/2])

        row.extend(mirrored)
        triangle.append(row)

    return triangle

for row in pascal_triangle(11):
    print row