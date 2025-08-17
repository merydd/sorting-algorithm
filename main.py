from insertion_sort import insertion_sort_steps
from selection_sort import selection_sort_first_n_steps

def analyze_search_case(sorted_array, target):
    n = len(sorted_array)
    position = None
    
    for i, num in enumerate(sorted_array):
        if num == target:
            position = i
            break
    
    if position == 0:
        return "Best case"
    elif position == n - 1:
        return "Worst case"
    else:
        return "Average case"

if __name__ == "__main__":
    # [22,27,16,2,18,6] -> Insertion Sort aşamaları
    array1 = [22, 27, 16, 2, 18, 6]
    print("Insertion Sort Aşamaları:")
    sorted_array = insertion_sort_steps(array1)
    
    # Big-O gösterimi
    print("\nTime Complexity:")
    print("Best case: O(n)")
    print("Average case: O(n²)")
    print("Worst case: O(n²)")
    
    # 18 sayısının case analizi
    case_result = analyze_search_case(sorted_array, 18)
    print(f"\n18 sayısı: {case_result}")
    
    # [7,3,5,8,2,9,4,15,6] -> Selection Sort ilk 4 adım
    print("\n" + "="*50)
    array2 = [7, 3, 5, 8, 2, 9, 4, 15, 6]
    print("Selection Sort İlk 4 Adım:")
    selection_sort_first_n_steps(array2, 4)