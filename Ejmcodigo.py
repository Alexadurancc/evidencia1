# Definimos dos conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# Unión de conjuntos
union = conjunto_a.union(conjunto_b)
print("Unión:", union)

# Intersección de conjuntos
interseccion = conjunto_a.intersection(conjunto_b)
print("Intersección:", interseccion)

# Diferencia de conjuntos
diferencia = conjunto_a.difference(conjunto_b)
print("Diferencia (A - B):", diferencia)

# Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print("Diferencia Simétrica:", diferencia_simetrica)

# Verificar si un elemento está en un conjunto
existe = 3 in conjunto_a
print("¿El 3 está en conjunto_a?:", existe)
