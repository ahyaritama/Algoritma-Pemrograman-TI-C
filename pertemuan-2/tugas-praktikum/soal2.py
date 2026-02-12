def bilangan_prima(n):
    if type(n) is not int or n <= 1:
        return
    
    prima = []
    for i in range(2, n+1):
        k = 0
        for j in range(1, i+1):
            if i % j == 0:
                k += 1
        if k == 2:
            prima.append(i)

    return prima