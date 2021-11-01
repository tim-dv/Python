# 1) Создать переменную типа String
s = "Hi!"
print(type(s), s)
# 2) Создать переменную типа Integer
i = 379
print(type(i), i)
# 3) Создать переменную типа Float
f = 31.79
print(type(f), f)
# 4) Создать переменную типа Bytes
b = bytes(13)
print(type(b), b)
# 5) Создать переменную типа List
l = ['inq', 290, 67, ['df57'], 13]
print(type(l), l)
# 6) Создать переменную типа Tuple
t = ("dfg", 97, "fgh56")
print(type(t), t)
# 7) Создать переменную типа Set
set = set("friday")
print(type(set), set)
# 8. Создать переменную типа Frozen set
frs = frozenset("qwerty")
print(type(frs), frs)
# 9) Создать переменную типа Dict
dct = {"age": 36,
       "name": "Tim"}
print(type(dct), dct)
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные.
# Вывести в консоль.
c = "Hello, "
d = "everyone"
e = c + d
print(e)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
name = "Tim"
age = 36
print(name + ", " + str(age))
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
first = "five"
second = 24
print(first + " + " + str(second))