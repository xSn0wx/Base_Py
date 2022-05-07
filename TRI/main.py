import random

def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        # in-place
        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min
    return l

def generate_random_list(n, min, max):
    l= []
    for i in range(n):
        a = random.randint(min, max)
        l.append(a)
    # sorted / unsorted
    # O(N^2)
    return l

l = generate_random_list(100, 0, 1000)
print('Unsorted:', l)
print()
print("Sorted:  ", selection_sort(l))