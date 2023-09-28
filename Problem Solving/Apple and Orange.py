def countApplesAndOranges(s, t, a, b, apples, oranges):
    m = len(apples)
    n = len(oranges)
    apple_counter = 0
    orange_counter = 0
    for i in range(m):
        if(a + apples[i] >= s and a + apples[i] <= t):
            apple_counter += 1
    
    for j in range(n):
        if(b + oranges[j] >= s and b + oranges[j] <= t):
            orange_counter += 1
    print(apple_counter)
    print(orange_counter)
