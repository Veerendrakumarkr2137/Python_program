def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    target = int(input("Enter the target value to search: "))
    print("\nOriginal Array:", arr)
    bubble_sorted = bubble_sort(arr.copy())
    print("Bubble Sorted Array:", bubble_sorted)
    selection_sorted = selection_sort(arr.copy())
    print("Selection Sorted Array:", selection_sorted)
    linear_index = linear_search(arr, target)
    print(f"Linear Search: Element {target} {'found at index ' + str(linear_index) if linear_index != -1 else 'not found'}")
    sorted_arr = bubble_sort(arr.copy())
    binary_index = binary_search(sorted_arr, target)
    print(f"Binary Search: Element {target} {'found at index ' + str(binary_index) if binary_index != -1 else 'not found'}")