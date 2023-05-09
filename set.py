data = {5,4,6,5,5}

data.add(7)
data.update(['23',False,11])
data.remove(False)
data.pop()
print(data)

nums = [4,5,6,7,3,4]
newNums = set(nums)
print(newNums)

newSet = frozenset([5,6,7,3,5]) # имеет также свойства картежа, тоесть не изменяется
print(newSet)