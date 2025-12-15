Mytuple = (1, 2, 4, 3, 6, 8, 5)
print(Mytuple)
last = -1
for i in range(len(Mytuple) - 1):
    if Mytuple[i] % 2 == 0 and Mytuple[i + 1] % 2 == 0:
        last = i

if last != -1:
    result = Mytuple[:last]
    if result:
        print("Элементы, предшествующие последней паре соседних чётных чисел:",*result)
    else:
        print("Перед последней парой нет элементов.")
else:
    print("В массиве нет пары соседних чётных чисел.")