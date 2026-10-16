animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
    is_long = len(animal) > 5
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find('b')
    else:
        total += len(animal)
print(total)

#startswith()	指定した文字で始まるか調べる
#len()	文字数を数える
#find()	文字の位置を調べる（0から数える）
#and	両方の条件が True のとき成立
#not	条件を反転させる
#+=	値を加算して代入する
#break	繰り返しを途中で終了する