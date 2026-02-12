def rata_rata(nilai):
    if type(nilai) is not list:
        return
    
    if len(nilai) < 1:
        return "Data kosong"
    
    total = 0
    for i in nilai:
        total += i
    return total / len(nilai)