from custom_list import Nil, NnList

def quick_sort(l: NnList) -> Nil | NnList:
    if l.len() <= 1:
        return l
    else:
        pair = partition(l.head, l.tail)
        return quick_sort(pair[0]).append(quick_sort(pair[1]).cons(l.head))

def partition(pivot: int, l: NnList | Nil) -> tuple[NnList, NnList]:
    pair: tuple = (Nil(), Nil())
    while isinstance(l, NnList):
        e = l.head
        l = l.tail
        first_list = pair[0]
        second_list = pair[1]

        if e < pivot:
            pair = (first_list.cons(e), second_list)
        else:
            pair = (first_list, second_list.cons(e))
    return pair


l0: Nil = Nil()
l1: NnList = NnList(2, l0)
l2: NnList = NnList(6, l1)
l3: NnList = NnList(3, l2)
l4: NnList = NnList(0, l3)
l5: NnList = NnList(1, l4)
l6: NnList = NnList(5, l5)
l7: NnList = NnList(7, l6)
l8: NnList = NnList(4, l7)
print(str(l8))
print(str(quick_sort(l8)))
