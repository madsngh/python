from itertools import permutations,combinations,combinations_with_replacement
print("Permutation")
perms = [''.join(p) for p in permutations('ab')]
print(list(set(perms)))
print("combination")
print(list((combinations_with_replacement("ab",2))))
print("combination without replacement")
print(list(combinations('ab',2)))
