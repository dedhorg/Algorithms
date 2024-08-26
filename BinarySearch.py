def sort_numbers(list_numbers: list[int]) -> list[int]:
    list_sort_numbers = sorted(list_numbers)
    return list_sort_numbers

def binary_search_preparation(list_numbers: list[int], search_num: int) -> str:
    """The function performs a binary search.
    Input data: a list of items: -> list_numbers, and a searched number -> search_num.
    Output data: index of the searched number (str)
    """
    
    list_sort_numbers = sort_numbers(list_numbers)
    min_num = 0
    max_num = len(list_sort_numbers) - 1

    def binary_search(list_sort_numbers: list[int], min_num: int, max_num: int, search_num: int) -> int:
        if max_num >= min_num:
            mid = (min_num + max_num) // 2
            if list_sort_numbers[mid] == search_num:
                return mid
            elif list_sort_numbers[mid] > search_num:
                return binary_search(list_sort_numbers, min_num, mid - 1, search_num)
            else:
                return binary_search(list_sort_numbers, mid + 1, max_num, search_num)
        else:
            return None

    result = binary_search(list_sort_numbers, min_num, max_num, search_num)
    if result == None:
        return "Search number not found."
    else:
        return f"Search number found at index {result}."

input_list = list(map(int, input("Enter a list of items separated by a space: ").split()))
input_number = int(input("Enter a searched value: "))

print("Sorted list of items: ",*sort_numbers(input_list))
print(binary_search_preparation(input_list, input_number))