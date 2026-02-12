def pangkat_rekursif(a, b):
    if type(a) is not int and type(b) is not int:
        return
    
    total = 1
    if b <= 1:
        return a
    else:
        total *= a
        total *= pangkat_rekursif(a, b - 1)
        return total