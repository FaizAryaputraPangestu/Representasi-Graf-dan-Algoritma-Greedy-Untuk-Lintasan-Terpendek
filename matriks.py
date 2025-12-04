import numpy as np
M1 = np.array([[1,2],[3,4]])
M2 = np.array([[5,6],[7,8]])
m_tambah = M1 + M2
print("Penjumlahan Matriks:\n", m_tambah)
m_kurang = M1 - M2
print("Pengurangan Matriks:\n", m_kurang)
m_kali = np.dot(M1,M2)
m_kali1 = M1 @ M2
print("Perkalian Matriks:\n", m_kali)
print("Perkalian Matriks1:\n", m_kali1)
m_transpose = M1.T
print("Transpose Matriks:\n", m_transpose)
print("Mengakses Elemen Matriks:\n", M1[0][1])
Z = np.zeros((3,3))
print("Matriks Berisi Nol:\n", Z)
I = np.eye(3)
print("Matriks Identitas:\n", I)