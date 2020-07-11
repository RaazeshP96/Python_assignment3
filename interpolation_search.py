'''
    Interpolation Search

'''


def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + \
        (upper_bound_index - lower_bound_index) * \
        (search_value - input_list[lower_bound_index]) // \
        (input_list[upper_bound_index] - input_list[lower_bound_index])


def interpolation_search(nlist, term):
    ordered_list = sorted(nlist)
    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(
            ordered_list, index_of_first_element, index_of_last_element, term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return None


nlist = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]
searchItem = int(input('Enter a number to search for: '))
result = interpolation_search(nlist, searchItem)
if result:
    print(f"{searchItem} is found in {result} index of sorted")
else:
    print(f"{searchItem} is not found in given list")
