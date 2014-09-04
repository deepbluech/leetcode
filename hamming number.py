__author__ = 'samsung'

def hamming_num(n):
    count = 0
    h = list()
    h.append(1)
    i = j = k = 0
    x2 = 2
    x3 = 3
    x5 = 5
    while count < n:
        h.append(min(x2, x3, x5))
        if x2 == h[-1]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[-1]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[-1]:
            k += 1
            x5 = 5 * h[k]
        count += 1
    return h

print hamming_num(15)



