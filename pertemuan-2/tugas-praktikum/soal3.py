def jumlah_digit(n):
    if type(n) is not int:
        return
    
    intLen = len(str(n))
    total = 0
    if intLen <= 1:
        return n
    else:
        total += n % 10
        total += jumlah_digit(n // 10)
        return total