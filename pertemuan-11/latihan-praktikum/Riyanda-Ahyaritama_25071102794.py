def radix_sort(data):
    radix_array = [[], [], [], [], [], [], [], [], [], []]
    max_val = max(data)
    exp = 1

    while max_val // exp > 0:
        while len(data) > 0:
            val = data.pop()
            radixIndex = (val // exp) % 10
            radix_array[radixIndex].append(val)

        for bucket in radix_array:
            while len(bucket) > 0:
                val = bucket.pop()
                data.append(val)

        exp *= 10
    
    return data


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def linear_search(data, target_val):
    for i in range(len(data)):
        if data[i] == target_val:
            return i
    return -1


def binary_search(data, target_val):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target_val:
            return mid

        if data[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    data = [
        78, 90, 65, 97, 882, 360, 21, 9, 1, 36,
        67, 99, 420, 510, 443, 38, 505, 123, 404, 45,
        5, 300, 250, 220, 15, 5, 33, 256, 10, 20,
        44, 421, 234, 42, 32, 37, 80, 0, 54, 14,
        71, 19, 121, 96, 126, 84, 155, 110, 18, 76,
        166, 2, 6, 51, 31, 59, 98, 55, 99, 280,
        303, 16, 25, 321
    ]

    print("Data sebelum diurutkan:", data, end="\n\n\n")
    radix_res = radix_sort(data.copy())
    merge_res = merge_sort(data.copy())
    print("Hasil Radix Sort:", radix_res, end="\n\n\n")
    print("Hasil Merge Sort:", merge_res, end="\n\n\n")

    x = int(input("Masukkan angka yang ingin dicari: "))
    linear_res = linear_search(radix_res, x)
    if linear_res != -1:
        print(f"Angka {radix_res[linear_res]} ditemukan di index: {linear_res}")
    else:
        print("Tidak ada")
    
    print()
    linear_res = linear_search(merge_res, x)
    if linear_res != -1:
        print(f"Angka {merge_res[linear_res]} ditemukan di index: {linear_res}")
    else:
        print("Tidak ada")
    
    print()
    binary_res = binary_search(radix_res, x)
    if binary_res != -1:
        print(f"Angka {radix_res[binary_res]} ditemukan di index: {binary_res}")
    else:
        print("Tidak ada")
    
    print()
    binary_res = binary_search(merge_res, x)
    if linear_res != -1:
        print(f"Angka {merge_res[binary_res]} ditemukan di index: {binary_res}")
    else:
        print("Tidak ada")


if __name__ == "__main__":
    main()