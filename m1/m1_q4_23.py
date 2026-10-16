ip_address = '192.168.3.1'
ip_sql = ip_address.split('.')
bin_exp = ''

for num in ip_sql:
    bin_exp += bin(int(num))[2:] + '.'

print(bin_exp[:-1]) #ウ

# ip_address = '192.168.3.1'	IPアドレスを文字列で保存する
# split('.')	. で文字列を分割する
# bin_exp = ''	変換結果を保存する空の文字列を作る
# for num in ip_sql:	リストの数字を1つずつ取り出す
# int(num)	文字列を整数に変換する
# bin()	整数を2進数に変換する
# [2:]	先頭の 0b を取り除く
# +=	文字列をつなげる
# [:-1]	最後の余分な . を取り除く
# print()	結果を表示する