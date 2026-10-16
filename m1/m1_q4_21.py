num = 12
list_s = []
s = 2
while s <= num:
    if num % s == 0:
        num //= s
        if s not in list_s:
            list_s.append(s)
        else:
            s += 1
print(list_s) #ウ

# num = 12	素因数分解する数字を12にする
# list_s = []	素数を保存する空リストを作る
# s = 2	割る数字を2に設定する
# while s <= num:	s が num 以下の間、繰り返す
# num % s == 0	num が s で割り切れるか調べる
# num //= s	num を s で割る
# s not in list_s	s がリストに入っていないか調べる
# list_s.append(s)	s をリストに追加する
# s += 1	s を1増やす
# print(list_s)	リストの内容を表示する