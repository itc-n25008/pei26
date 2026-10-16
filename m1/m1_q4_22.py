a = 17
b = 5
dm = divmod(a, b)
p = pow(dm[0], dm[1])
all_num = [a, b, dm[0], dm[1], p]
min_all = min(all_num)
max_all = max(all_num)
sum_all = sum(all_num)
print(f'{min_all}, {max_all}, {sum_all}') #イ

# a = 17	変数 a に17を代入する
# b = 5	変数 b に5を代入する
# divmod(a, b)	割り算の商と余りを求める
# dm[0]	商の3を取り出す
# dm[1]	余りの2を取り出す
# pow(dm[0], dm[1])	3の2乗を計算して9を求める
# min(all_num)	リストの最小値を求める
# max(all_num)	リストの最大値を求める
# sum(all_num)	リストの合計を求める
# print()	計算結果を表示する
