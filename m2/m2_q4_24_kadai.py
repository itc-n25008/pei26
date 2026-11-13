def func(x, y):
    return bool(x and y)

a = func(-5, -6)

z = []
z.append(a)

print(z)

# bool()関数は、値をTrueまたはFalseに変換する関数。
# 0や空の文字列などはFalse、それ以外の数値などはTrueになる。