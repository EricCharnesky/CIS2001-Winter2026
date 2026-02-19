name = 'Eric'

for index, letter in enumerate(name):
    print(f'{letter} {ord(letter)} {chr( ord(letter) + index)}' )

def _shift_recursive(some_string, index):
    if index < len(some_string) - 1:
        return chr(ord(some_string[index])+index) + _shift_recursive(some_string, index+1)
    return chr(ord(some_string[index])+index)

def shift_recursive(some_string):
    return _shift_recursive(some_string, 0)

print(shift_recursive("Eric"))