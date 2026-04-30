data1 = [290, 1012, 731, 801, 992, 1395, 367, 519, 795, 1385, 274, 154, 219, 1410, 83, 589, 553, 362, 594, 851, 173,
        657, 581, 397, 543, 791, 226, 81, 1459, 126, 941, 491, 1207, 1093, 1473, 951, 267, 1371, 864, 953, 1119, 212, 1266,
        120, 723, 643, 205, 130, 9, 16, 1053, 507, 1381, 1122, 1323, 758, 713, 1219, 375, 951, 98, 1011, 642, 1099, 1098,
        453, 7, 1137, 53, 1352, 553, 380, 1324, 473, 519, 923, 13, 592, 10, 546, 65, 1440, 1002, 1444, 510, 1266, 901, 1444,
        691, 650, 373, 896, 681, 916, 943, 323, 783, 1385, 891, 621, 687, 1384, 268, 211, 708, 1067, 736, 1223, 990, 1145,
        448, 731, 486, 381, 1441, 312, 181, 785, 157, 793, 1029, 1273, 846, 1473, 57, 785, 588, 582, 920, 808, 644, 1182,
        1101, 579, 623, 556, 858, 59, 163, 1236, 310, 1308, 962, 356, 1005, 883, 582, 786, 958, 321]
data2 = data1.copy()


def bubble_sort(data):
    n = len(data)
    t = 0
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                t += 1
        if not swapped:
            break
    
    return data, t


def selection_sort(data):
    n = len(data)
    t = 0
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if data[j] > data[max_index]:
                max_index = j
        
        if max_index != i:
            data[i], data[max_index] = data[max_index], data[i]
            t += 1
    return data, t


bubble, total_b = bubble_sort(data1)
print("Bubble Sort (kecil → besar):", bubble)
print("Jumlah swap Bubble Sort:", total_b)
print()
sel, total_s = selection_sort(data2)
print("Selection Sort (besar → kecil):", sel)
print("Jumlah swap Selection Sort:", total_s)