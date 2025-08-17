def selection_sort_first_n_steps(arr, n_steps):
    arr_copy = arr.copy()
    print(f"Başlangıç: {arr_copy}")
    
    for i in range(min(n_steps, len(arr_copy))):
        min_idx = i
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        
        print(f"Adım {i + 1}: {arr_copy}")
    
    return arr_copy

if __name__ == "__main__":
    array = [7, 3, 5, 8, 2, 9, 4, 15, 6]
    selection_sort_first_n_steps(array, 4)