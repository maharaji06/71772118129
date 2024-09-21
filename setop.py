a = {0, 2, 4, 6, 8}
b = {1, 2, 3, 4, 5}

# Union of sets a and b
union_set = a.copy()
union_set.update(b)
print("Union of sets a and b:", union_set)

# Intersection of sets a and b
intersection_set = {x for x in a if x in b}
print("Intersection of sets a and b:", intersection_set)

# Difference between set a and set b (elements in a but not in b)
difference_set = {x for x in a if x not in b}
print("Difference of set a and set b:", difference_set)

# Symmetric difference between set a and set b (elements in a or b but not in both)
symmetric_difference_set = {x for x in a.union(b) if x not in a.intersection(b)}
print("Symmetric difference of set a and set b:", symmetric_difference_set)
