'''

    Linear Search

'''


def linear_search(nlist, searchItem):
    found = False
    for index, item in enumerate(nlist):
        if item == searchItem:
            found = True
            print(searchItem, ' was found in the list at index ', index)
            break
    if found == False:
        print(searchItem, ' was not found in the list!')


nlist = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]
searchItem = int(input('Enter a number to search for: '))

linear_search(nlist, searchItem)
