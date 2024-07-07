from custom_list import Nil, NnList

def merge_sort(l: Nil | NnList) -> Nil | NnList:
    if l.len() <= 1:
        return l
    else:
        l1: Nil | NnList = Nil()
        l2: Nil | NnList = Nil()
        flag: bool = True
        while isinstance(l, NnList):
            if flag:
                l1 = l1.cons(l.head)
            else:
                l2 = l2.cons(l.head)
            l = l.tail
            flag = not flag
        return merge(merge_sort(l1), merge_sort(l2))

def merge(l1: Nil | NnList, l2: Nil | NnList) -> Nil | NnList:
    if isinstance(l1, Nil):
        return l2
    elif isinstance(l2, Nil):
        return l1
    else:
        if l1.head < l2.head:
            return NnList(l1.head, merge(l1.tail, l2))
        else:
            return NnList(l2.head, merge(l1, l2.tail))

l0: Nil = Nil()
l1: NnList = NnList(2,l0)
l2: NnList = NnList(6,l1)
l3: NnList = NnList(3,l2)
l4: NnList = NnList(0,l3)
l5: NnList = NnList(1,l4)
l6: NnList = NnList(5,l5)
l7: NnList = NnList(7,l6)
l8: NnList = NnList(4,l7)
print(str(l8))
print(str(merge_sort(l8)))
