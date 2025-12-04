import numpy as np

# ================================
# INPUT DINAMIS
# ================================
n = int(input("Masukkan jumlah node: "))

nodes = []
print("\nMasukkan nama node satu per satu:")
for i in range(n):
    nama = input(f"Node {i+1}: ")
    nodes.append(nama)

print("\nMasukkan matriks jarak:")
print("(Gunakan 0 jika tidak ada jalur)")
A = []

for i in range(n):
    row = []
    print(f"\nBaris untuk node {nodes[i]}:")
    for j in range(n):
        val = float(input(f"Jarak {nodes[i]} -> {nodes[j]}: "))
        row.append(val)
    A.append(row)

A = np.array(A)

# ================================
# INPUT NODE AWAL & TUJUAN
# ================================
print("\nDaftar node:", nodes)
start = input("Masukkan node awal: ")
end = input("Masukkan node tujuan: ")

# Validasi
if start not in nodes or end not in nodes:
    print("Node tidak ditemukan!")
    exit()

start_idx = nodes.index(start)
end_idx = nodes.index(end)

# ================================
# ALGORITMA GREEDY SEPERTI PADA GAMBAR
# ================================
visited = [start_idx]
path = [start]
total = 0

while True:
    curr = visited[-1]

    if curr == end_idx:
        break  # tujuan tercapai

    min_weight = float('inf')
    next_node = None

    for j in range(len(nodes)):
        if A[curr][j] != 0 and j not in visited and A[curr][j] < min_weight:
            min_weight = A[curr][j]
            next_node = j

    if next_node is None:
        print("\nTidak ada jalur menuju tujuan!")
        break

    visited.append(next_node)
    path.append(nodes[next_node])
    total += min_weight

# ================================
# OUTPUT
# ================================
print("\nLintasan:", " -> ".join(path))
print("Jarak total:", total)