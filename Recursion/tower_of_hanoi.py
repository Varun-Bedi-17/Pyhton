def toi(n, from_rod, to_rod, aux):
    if n == 0:
        return
    toi(n-1,from_rod, aux, to_rod)
    print(f"Move {n} disc from {from_rod} to {to_rod}")
    toi(n-1,aux,to_rod,from_rod)

toi(4,"A", "C", "B")
