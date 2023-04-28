def pairing(n):
    if n == 0 or n == 1 or n == 2:
        return n
    return pairing(n-1) + pairing(n-2)*(n-1)

print(pairing(5))