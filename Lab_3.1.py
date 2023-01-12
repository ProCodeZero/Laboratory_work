# Lab_3.1
inputString = str(input("Введите предложение, в котором хотите перевернуть слова: "))

list1 = inputString.split(" ")

for index, item in enumerate(list1):
    list1[index] = item[::-1]

outString = " ".join(list1)

print(outString)
