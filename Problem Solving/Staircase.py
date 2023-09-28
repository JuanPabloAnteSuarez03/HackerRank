def staircase(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        sharp = '#' * i
        print(spaces + sharp)
