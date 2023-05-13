def heap(arr, n, i):

    # Set the root node as the largest
    largest = i

    # Find the left and right child indices of the root node
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child exists and if it is larger than the root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if the right child exists and if it is larger than the root or left child
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If the largest element is not the root, swap the root with the largest element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heap(arr, n, largest)


def heapsort(arr):

    n = len(arr)

    # Build a max heap from the given array
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

    # Extract elements from the heap one by one and place them at the end of the array
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
