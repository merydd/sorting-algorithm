def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"Adım {i}: {arr}")
    
    return arr

def insertion_sort_steps(arr):
    print(f"Başlangıç: {arr}")
    result = insertion_sort(arr.copy())
    return result

if __name__ == "__main__":
    array = [22, 27, 16, 2, 18, 6]
    insertion_sort_steps(array)