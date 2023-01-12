# Lab_2
number = str(input("Введите целое неотрицательное число: "))
list1 = list()
list2 = list()

for i in number:
    list1.append(i)

list2 = list.copy(list1)
list2.reverse()

if list1 == list2:
    print("Число " + str(number) + " является полиндромом")
else:
    print("Число " + str(number) + " не является полиндромом")
