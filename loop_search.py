import random

def loop_search(target, data):
    found = False
    
    for i in data:
        if i == target:
            found = True

    return found


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(20)]
    data.sort()
    print(data)

    target = int(input('What number would you like to find? '))

    found = loop_search(target, data)

    print(found)