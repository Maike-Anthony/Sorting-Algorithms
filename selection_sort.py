def selection(lst, ordered = []):
    if lst == []:
        return ordered
    else:
        i = 0
        for n in range(len(lst)):
            if lst[n] < lst[i]:
                i = n
        ordered.append(lst[i])
        lst.pop(i)
        return selection(lst, ordered)

def main():
    lst = [5, 9, 10, 23, 0, -6, -46, 15, -2]
    print("Unsorted list:", lst)
    print("List sorted with selection sort:", selection(lst))

if __name__=="__main__":
    main()

