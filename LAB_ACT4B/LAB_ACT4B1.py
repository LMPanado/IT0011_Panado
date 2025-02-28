A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print("Elements in A and B:", A | B, "| Count:", len(A | B))
print("Elements in B but not in A and C:", B - (A | C), "| Count:", len(B - (A | C)))
print("\n[h, i, j, k]:", C - (A | B))
print("[c, d, f]:", (A & C) - B)
print("[b, c, h]:", B & C)
print("[d, f]:", (A & C) - B)
print("[c]:", A & B & C)
print("[l, m, o]:", B - (A | C))
