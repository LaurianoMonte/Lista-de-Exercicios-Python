l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
l3 = []

l3 = l1[:1] + l2[1::2]

print("listas originais: \n",l1 ,"\n", l2)
print("lista modificada: ", l3)