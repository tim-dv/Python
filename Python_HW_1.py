# 1) Создать переменную типа String
var_string = "Hi!"
print(type(var_string), var_string)
# 2) Создать переменную типа Integer
var_integer = 379
print(type(var_integer), var_integer)
# 3) Создать переменную типа Float
var_float = 31.79
print(type(var_float), var_float)
# 4) Создать переменную типа Bytes
var_bytes = bytes(13)
print(type(var_bytes), var_bytes)
# 5) Создать переменную типа List
var_list = ["inq", 290, 67, ["df57"], 13]
print(type(var_list), var_list)
# 6) Создать переменную типа Tuple
var_tuple = ("dfg", 97, "fgh56")
print(type(var_tuple), var_tuple)
# 7) Создать переменную типа Set
var_set = set("friday")
print(type(var_set), var_set)
# 8. Создать переменную типа Frozen set
var_frozenset = frozenset("qwerty")
print(type(var_frozenset), var_frozenset)
# 9) Создать переменную типа Dict
var_dict = {"age": 36,
            "name": "Tim"}
print(type(var_dict), var_dict)
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные.
# Вывести в консоль.
var_1 = "Hello, "
var_2 = "everyone"
e = var_1 + var_2
print(e)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
name = "Tim"
age = 36
print(name, (age))
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
first = "five"
second = 24
print(first + str(second))