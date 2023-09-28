def miniMaxSum(arr):
    mini = 0
    maxi = 0
    sort_arr = sorted(arr)
    for i in range(4):
        mini += sort_arr[i]
    for j in range(1, 5):
        maxi += sort_arr[j]
    print(mini , maxi)
