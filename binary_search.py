'''
    Binary Search
'''


def binary_search(item_list, item):
    item_list.sort()
    first = 0
    last = len(item_list)-1
    found = False
    while(first <= last and not found):
        mid = (first + last)//2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


nlist = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]
searchItem = int(input('Enter a number to search for: '))
result = binary_search(nlist, searchItem)
if result:
    print(f"{searchItem} is found in given list")
else:
    print(f"{searchItem} is not found in given list")
