data = (4,6,8,2,True,'hey')
print(data[1:5])
print(data.count(2))
print(len(data))

numbers = 1,54,6
print(numbers)

for i in data:
    print(i)

newData = [4,4,5,6]
newDataT = tuple(newData)
word = tuple('Hello world')
print(newDataT, word)