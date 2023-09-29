def multiply(a, b):
    ans = 0
    rango = min(a, b)
    suma = max(a, b)
    aPositivo = abs(a)
    bPositivo = abs(b)

    for _ in range(abs(rango)):
        ans = ans + suma if a == aPositivo and bPositivo == b else ans - suma

    return ans
