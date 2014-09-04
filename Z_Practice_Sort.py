__author__ = 'Administrator'
#coding=utf-8
#/usr/bin/python

import random
def quicksort(num, left, right):

    if left > right:
        return
    i = left
    j = right
    while i < j:
        while i < j and num[i] < num[j]:
            j -= 1
        if i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
        while i < j and num[i] < num[j]:
            i += 1
        if i < j:
            num[i], num[j] = num[j], num[i]
            j -= 1
    quicksort(num, left, i-1)
    quicksort(num, i+1, right)


if __name__ == '__main__':
    n = 10
    num = list()
    for i in xrange(n):
        num.append(int(random.random() * 100))
    print 'original : %s' % str(num)
    quicksort(num, 0, len(num)-1)
    print 'sort : %s' % str(num)