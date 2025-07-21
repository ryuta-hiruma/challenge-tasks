from datetime import datetime
import json
import sys

# jsonファイル名定義
filename = 'user_age.json'

# jsonファイルの読み込み
try:
    with open(filename, 'r') as json_open:
        json_data = json.load(json_open)
        # print("Json_type:" + str(type(json_data)))
except json.JSONDecodeError:
    print(f'###エラー：ファイル{filename}は正しいJSON形式ではありません###')
    sys.exit()
except FileNotFoundError:
    print(f'###エラー：ファイル{filename}が見つかりません###')
    sys.exit()

# JSONファイルの内容表示
# print(json_data)

# 辞書配列の定義
# user_dict = [
#     {'name': 'Alice', 'birthday': '1995-07-01'},
#     {'name': 'Bob', 'birthday': '2005-12-24'},
#     {'name': 'Charlie', 'birthday': '1965-03-15'}
#     ]
# 辞書配列の表示
# print(f'配列の出力{user_dict}')

# 現在日時
day_now = datetime.now()
print(f'現在の日時は{day_now}')

# 辞書配列より値を取得
for user_data in json_data:
    age = 0
    cat = ''
# 誕生日　文字型＝＞を日付型へ変換
    birth = datetime.strptime(user_data['birthday'], '%Y-%m-%d')
# 年齢を計算する(年齢 ＝ 現在年 ー 誕生年 ー 現在日より誕生日の方が後ならTrue(1)を引く)
    age = day_now.year - birth.year - ((day_now.month, day_now.day) < (birth.month, birth.day))
# カテゴリの判定
    if age <= 12:
        cat = 'こども'
    elif 13 <= age <= 19:
        cat = 'ティーン'
    elif 20 <= age <= 64:
        cat = 'おとな'
    else:
        cat = 'シニア'
# 名前、年齢、カテゴリの出力
    print(f'{user_data['name']}さんは {age}歳 です。→ カテゴリ：{cat}')
