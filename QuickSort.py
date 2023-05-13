def quicksort(arr):
    # Define a helper function to partition the array
    def partition(start, end):
        pivot_index = start
        pivot = arr[pivot_index]

        # Swap the pivot with the last element in the subarray
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

        for i in range(start, end):
            # If the current element is less than the pivot, swap it with the leftmost larger element
            if arr[i] < pivot:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1

        # Swap the pivot back to its final position
        arr[end], arr[start] = arr[start], arr[end]

        return start

    # Define the recursive quicksort function
    def sort(start, end):
        if start < end:
            # Partition the array and get the pivot index
            pivot_index = partition(start, end)

            # Recursively sort the left and right subarrays
            sort(start, pivot_index - 1)
            sort(pivot_index + 1, end)

    # Call the quicksort function on the entire array
    sort(0, len(arr) - 1)
