a = []
b = 10
for i in range(b):
    a.append(int(input(i)))
print(a)
c = []
for i in a:
    if i < 0:
        c.append(i)
print(c)
print(sum(c))