def bubble(lst):
    i = 0
    for n in range(len(lst)-1):
        if lst[n] > lst[n+1]:
            k = lst[n]
            lst[n] = lst[n+1]
            lst[n+1] = k
            i += 1
    if i == 0:
        return lst
    else:
        return bubble(lst)

def main():
    lst = [5, 9, 10, 23, 0, -6, -46, 15, -2]
    print("Unsorted list:", lst)
    print("List sorted with bubble sort:", bubble(lst))

if __name__=="__main__":
    main()
