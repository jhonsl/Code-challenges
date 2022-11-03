array = [2, 1, 2, 3, 3, 4, 2, 4]
longitud = len(array)
cantidad = 0

for i in range(longitud):
    if (i + 2) > (longitud - 1): break

    if(array[i] == array[i + 2] and array[i] != array[i + 1]):
        cantidad += 1
        print(array[i], array[i + 1], array[i + 2])

print("hay", cantidad, "bumerangs")