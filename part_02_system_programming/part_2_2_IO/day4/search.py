def search(list_, key):
    low, high = 0, len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_[mid] < key:
            low = mid + 1
        elif list_[mid] > key:
            high = mid - 1
        else:
            return mid


l = [1, 2, 3, 4, 5, 6,  7, 8, 9, 10]

print("key index =", search(l, 1))
print("key index =", search(l, 10))
print("key index =", search(l, 6))
print("key index =", search(l, 0))
