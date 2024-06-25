from custom_list import Nil, NnList
from typing import Union

def qsort(lst):
    if lst.len() <= 1:
        return lst
    else:
        pair = partition(lst.head,lst.tail)
        return qsort(pair[0]).append(qsort(pair[1]).cons(lst.head))

def partition(pvt,lst):
    pair = (Nil(), Nil())
    while isinstance(lst,NnList):
        e = lst.head
        lst = lst.tail
        fl = pair[0]
        sl = pair[1]

        if e < pvt:
            pair = (fl.cons(e), sl)
        else:
            pair = (fl, sl.cons(e))
    return pair


l0 = Nil()
l1 = NnList(2, l0)
l2 = NnList(6, l1)
l3 = NnList(3, l2)
l4 = NnList(0, l3)
l5 = NnList(1, l4)
l6 = NnList(5, l5)
l7 = NnList(7, l6)
l8 = NnList(4, l7)
print(str(l8))
print(str(qsort(l8)))
