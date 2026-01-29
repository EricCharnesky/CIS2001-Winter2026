import sys
from fixedSizeArray import FixedSizeArray

fixedSizeArray = FixedSizeArray()
for n in range(100):
    print(f'with{n} items, size is: {sys.getsizeof(fixedSizeArray._data)}')
    fixedSizeArray.append(n)



numbers = []

# on average O(1) for adding items
for n in range(100):
    print(f'with{n} items, size is: {sys.getsizeof(numbers)}')
    numbers.append(n)

# on average O(n) - throw away the coefficient
numbers.remove(0)

# on average for finding O(n)
numbers.index(5)

# access item by index O(1)
print(numbers[10])



