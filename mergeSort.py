def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid
        mid = len(arr) // 2

        # Dividing the array
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call
        mergeSort(left)
        mergeSort(right)

        # Compare elements and merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

    # Check for any remaining elements in left and right
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
# Test | Output
arr = [7, 4, 3, 1]
print("array ก่อนเรียงลำดับ:", arr)
mergeSort(arr)
print("array หลังจากเรียงลำดับแล้ว:", arr)

# # Output
# array ก่อนเรียงลำดับ: [7, 4, 3, 1]
# array หลังจากเรียงลำดับแล้ว: [1, 3, 4, 7]