import itertools

#     Brief of these four functions
print(*itertools.product('ABCD', repeat=2))  #  AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

print(*itertools.permutations('ABCD', 2))  #  AB AC AD BA BC BD CA CB CD DA DB DC

print(*itertools.combinations('ABCD', 2))  #  AB AC AD BC BD CD

print(*itertools.combinations_with_replacement('ABCD', 2))  #  ('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'C') ('C', 'D') ('D', 'D')


# --------------------------------------------------------------------------------------


# 1. Product(*iterables, repeat = 1) - 
# print(*itertools.product("AABC","DEF"))  #  ('A', 'D') ('A', 'E') ('A', 'F') ('A', 'D') ('A', 'E') ('A', 'F') ('B', 'D') ('B', 'E') ('B', 'F') ('C', 'D') ('C', 'E') ('C', 'F')
# print(*itertools.product("AABc", repeat = 2))  #  ('A', 'A') ('A', 'A') ('A', 'B') ('A', 'c') ('A', 'A') ('A', 'A') ('A', 'B') ('A', 'c') ('B', 'A') ('B', 'A') ('B', 'B') ('B', 'c') ('c', 'A') ('c', 'A') ('c', 'B') ('c', 'c')
# print(*itertools.product([1,2,3], "fg"))  #  (1, 'f') (1, 'g') (2, 'f') (2, 'g') (3, 'f') (3, 'g')
# print(*itertools.product(["BCd","tyu"],[1,2]))  #  ('BCd', 1) ('BCd', 2) ('tyu', 1) ('tyu', 2)
# print(*itertools.product(["afd", "yui"], repeat = 2))  #  ('afd', 'afd') ('afd', 'yui') ('yui', 'afd') ('yui', 'yui')
# print(*itertools.product("AB","CD","EF"))  #  ('A', 'C', 'E') ('A', 'C', 'F') ('A', 'D', 'E') ('A', 'D', 'F') ('B', 'C', 'E') ('B', 'C', 'F') ('B', 'D', 'E') ('B', 'D', 'F')


# 2. Permutations(iterable, r = none) - if r isnot specified, it is equal to the length
# print(*itertools.permutations("ABCD",2))  #  ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C')
# print(*itertools.permutations("AB"))  #  ('A', 'B') ('B', 'A')
# print(*itertools.permutations(["1","b"], 2))  #  ('1', 'b') ('b', '1')

# 3. combinations(iterable, r) - Return all possible comb. without replacement in sorted order
# print(*itertools.combinations("ABC"))  #  Missing r
# print(*itertools.combinations("ABC",2))  #  ('A', 'B') ('A', 'C') ('B', 'C')
# print(*itertools.combinations("ABC", 3))  #  ('A', 'B', 'C')
# print(*itertools.combinations((11, "geeks", 24.0), 2))  #  (11, 'geeks') (11, 24.0) ('geeks', 24.0)

# 4. combinations_with_replacement(iterable, r) - 
# print(*itertools.combinations_with_replacement("ABC", 2))  #  ('A', 'A') ('A', 'B') ('A', 'C') ('B', 'B') ('B', 'C') ('C', 'C')
# print(*itertools.combinations_with_replacement(range(2), 1))  #  (0,) (1,)


