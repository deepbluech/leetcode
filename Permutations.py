def swap(mylist, i, j):
    tmp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = tmp

def perm(mylist, i, n):
    if i == n:
        print mylist
    for j in range(i, n):
        swap(mylist, i, j)
        perm(mylist, i+1, n)
        swap(mylist, i, j)

mylist = [0,1,2,3,4]
perm(mylist, 0, len(mylist))