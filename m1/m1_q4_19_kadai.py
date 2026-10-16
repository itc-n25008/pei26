a = [1, 2, 3, 4]
id_a = id(a)
b = a.copy()
id_b = id(b)
if id_a == id_b:
    result ='A'
elif id(a) == id(b):
    result = 'B'
elif id_a == id(a):
    result = 'C'
else:
    result = 'D'
print(result)
print(id(a))  #変数 a のIDを表示する。
print(id_a)  #変数 id_a に保存したIDを表示るる
print(type(id_a))  #id_a のデータ型を表示する