mlist = []
c = 10
for i in range(c):
    mlist.append(float(input(i)))
print('Начальный список = ',mlist)
print('Минимальный элемент = ',min(mlist),' его индекс = ',mlist.index(min(mlist)))

minimal = []
for i in mlist:
    if i < 0:
        minimal.append(mlist.index(i))
print(minimal)
for i in minimal:
    if minimal.index(i) != 0 and minimal.index(i) != 1:
        minimal.remove(i)
minimal.pop()
start = minimal[0]
end = minimal[1]
print('Промежуток = ',minimal,' сумма данного промежутка = ',sum(mlist[start+1:end]))

abs1=[]
for i in mlist:
    if abs(i) <= 1:
        abs1.append(i)
other = []
for i in mlist:
    if abs(i) > 1:
        other.append(i)
result = abs1 + other
print('Преобразованный список = ', result)