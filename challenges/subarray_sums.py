def subarray_sums(numbers, sum):
    lookup = [-1] * len(numbers)
    lookup[0] = numbers[0]

    end = None
    for i in xrange(1, len(numbers)):
        lookup[i] = numbers[i] + lookup[i-1]
        if lookup[i] >= sum: 
            end = i
            break
  
    assert end is not None, "Sum is larger than given numbers"
  
    start = lookup.index(lookup[end]-sum)
    
    return numbers[start+1:end+1]

print subarray_sums([1,4,20,3,10,5], 33)
print subarray_sums([1,4,0,0,3,10,5], 7)
print subarray_sums([1,4], 0)
