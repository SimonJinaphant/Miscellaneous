

def print_combination_paren(n):
    for paren in combination_paren(n):
        print paren


def combination_paren(n):
    results = set([])

    if n == 1:
        results.add("()")
    else:
        for paren in combination_paren(n-1):
            results.add("()"+paren)
            results.add("("+paren+")")
            results.add(paren+"()")

    return results

print_combination_paren(3)