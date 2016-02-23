def odd_even_occurrence(numbers):
    real_total = sum(numbers)
    total = real_total

    for num in numbers:
        total = total ^ num
        print total

    return abs(total - real_total)


print odd_even_occurrence([3,3,1,0,0,5,1,0,8,8,0])