# Lab_3.2
def makeArrayElementsInt(Array):
    for index, item in enumerate(Array):
        Array[index] = int(item)


array1 = input("Введите числа массива через пробел: ").split(" ")
print("Вы ввели массив:", end=" ")
print(array1)

makeArrayElementsInt(array1)
array1.sort()
print("Ваш отсортированный массив выглядит так:", end=" ")
print(array1)
newElement = input("Введите новый элемент массива: ")
array1.append(newElement)
makeArrayElementsInt(array1)
array1.sort()
print("Так выглядит ваш массив после включения в него нового элемента: ", end=" ")
print(array1)
