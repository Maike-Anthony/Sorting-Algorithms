def merge(lst):
    l = len(lst)
    if len(lst) <= 1:
        return lst
    else:
        left = merge(lst[:(l // 2)])
        right = merge(lst[(l // 2):])
        result = []
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

def main():
    lst = [5, 9, 10, 23, 0, -6, -46, 15, -2]
    print("Unsorted list:", lst)
    print("List sorted with merge sort:", merge(lst))

if __name__=="__main__":
    main()
