def lonelyinteger(a):
    if(len(a) == 1):
        return a[0]
    sorted_a = sorted(a)
    if(sorted_a[0] != sorted_a[1]):
        return sorted_a[0]
    if(sorted_a[len(a)-1] != sorted_a[len(a)-2]):
        return sorted_a[len(a)-1]
    for i in range(2, len(a) - 1, 2):
        if(sorted_a[i] != sorted_a[i+1]):
            return sorted_a[i]
