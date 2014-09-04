__author__ = 'Administrator'
def print_n_bit(n, i, s):
    if i == n :
        print_number(s)
        return
    for j in range(10):
        print_n_bit(n, i+1, s+ str(j))

def print_number(s):
    if s == '000':
        print 0
        return
    i = 0
    while i < len(s) and s[i] == '0':
        i += 1
    print s[i:]

print_n_bit(3, 0, '')