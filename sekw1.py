a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print('Dwa środkowe:', a[3:5])
# print('Wszystkie poza skrajnymi:', a[1:7])
assert a[:5] == a[0:5]
assert a[5:] == a[5:(len(a))]
# print(a[:])
# print(a[:-1])
# print(a[2:-1])
# print(a[-3:-1])

b = a[3:]
print('Przed:    ', b)
b[1] = 99
print('Po:    ', b)
print('Bez zmian:   ',a)
