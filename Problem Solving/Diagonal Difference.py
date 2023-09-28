def diagonalDifference(arr):
    # Write your code here
    a = 0
    b = 0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[(len(arr)-1)-i][i]
    return abs(a-b)
