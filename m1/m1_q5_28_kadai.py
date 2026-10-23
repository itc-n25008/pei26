days = ['月', '月', '火', '水', '木', '金', '金']

days.remove('月')  # 重複している「月」を1つ削除
days.remove('金')  # 重複している「金」を1つ削除

days.insert(0, '日')  # リストの先頭に「日」を追加
days.insert(6, '土')  # インデックス6に「土」を追加

print(days)