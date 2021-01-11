import random

def binary_search(data, target, low_index, high_index):
    if low_index > high_index:
        return False

    mid = (low_index + high_index) // 2
    
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low_index, mid -1)
    else:
        return binary_search(data, target, mid + 1, high_index)



if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(20)]


data.sort()
# data.sort() lo ordena y lo deja en la misma
# de esta forma lo ordena y lo deja en una nueva lista
#data_sorted = sorted(data)

print(data)

target = int(input('What number would you like to find? '))
found = binary_search(data, target, 0, len(data) - 1)

print(found)