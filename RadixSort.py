def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_number = max(arr)

    # Do counting sort for every digit. Note that instead of passing the actual
    # digit number, the digits are compared using their place value.
    exponent = 1
    while max_number // exponent > 0:
        counting_sort(arr, exponent)
        exponent *= 10

def counting_sort(arr, exponent):
    n = len(arr)

    # The output array that will have sorted arr
    output = [0] * n

    # Initialize count array
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        digit = (arr[i] // exponent) % 10
        count[digit] += 1

    # Change count[i] so that it now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        digit = (arr[i] // exponent) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]
