# INSERTION SORTING

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        insert_index = i
        current_value = array.pop(i)
        for j in range(i - 1, -1, -1):
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value)
    
    return array



# QUICK SORTING

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)
    
    return array


# COUNTING SORT

def counting_sort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)

    while len(array) > 0:
        num = array.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1

    return array


def main():
    array = []
    n = 0
    while True:
        try:
            n = int(input("Masukkan jumlah angka: "))
        except KeyboardInterrupt:
            print()
            return
        except:
            print("Angka salah!", end=" ")
            continue
        break

    for _ in range(n):
        angka = 0
        while True:
            try:
                angka = int(input("Masukkan angka positif: "))
            except KeyboardInterrupt:
                print()
                return
            except:
                print("Angka salah!", end=" ")
                continue
            break
        array.append(angka)

    insertion_res = insertion_sort(array.copy())
    quick_res = quick_sort(array.copy())
    counting_res = counting_sort(array.copy())

    print()
    print("Insertion Sorting (Sebelum):", array)
    print("Insertion Sorting (Sesudah):", insertion_res, end="\n\n")
    print("Quick Sorting (Sebelum):", array)
    print("Quick Sorting (Sesudah):", quick_res, end="\n\n")
    print("Counting Sorting (Sebelum):", array)
    print("Counting Sorting (Sesudah):", counting_res)


if __name__ == "__main__":
    main()