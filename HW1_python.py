# 1) Создать переменную типа String
a = "Tom"

# 2) Создать переменную типа Integer
b = 5

# 3) Создать переменную типа Float
c = 5.1213

# 4) Создать переменную типа Bytes
d = bytes([50])

# 5) Создать переменную типа List
e = list('router')

# 6) Создать переменную типа Tuple
f = tuple('course')

# 7) Создать переменную типа Set
g = {10, 20, 30, 40, 50, 100, 10}

# 8. Создать переменную типа Frozen set
k = frozenset('software')

# 9) Создать переменную типа Dict
h = dict(name = 'London', location = 'London Str')

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(k, type(k))
print(h, type(h))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
first = "Great "
last = "Britain"
name = first + last
print(name)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(a,b, sep=',')

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(a,b, sep='+')
