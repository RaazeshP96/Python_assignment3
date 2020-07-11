'''
Bubble Sort

'''


def bubbleSort(list1):
    n = len(list1)
    for ind, _ in enumerate(list1):
        for j in range(0, n-ind-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]


list1 = [75, 14, 46, 43, 27, 57, 41, 45, 21, 70, 5]
bubbleSort(list1)
print(list1)
