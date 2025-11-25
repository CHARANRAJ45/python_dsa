# Bubble Sort in Python
def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop for passes
    for i in range(n - 1):
        # Inner loop for comparisons
        for j in range(n - i - 1):
            # Swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                # Python tuple unpacking for swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Usage example
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", unsorted_array)
sorted_array = bubble_sort(unsorted_array)
print("Sorted array:", sorted_array)
