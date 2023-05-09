numbers = [5, 2, 7]
numbers.append(100)
numbers.insert(1, True)

b = [5, 3, 6, 8]
numbers.extend(b)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.pop(0)
print(numbers)

print(numbers.count(5))
print(len(numbers))

numbers.clear()
print(numbers)