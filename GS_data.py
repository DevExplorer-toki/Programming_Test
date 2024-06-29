import requests
from bs4 import BeautifulSoup
import sqlite3

# スクレイピングするURL
url = 'https://mhworld.kiranico.com/ja/weapons?type=0'

# Webページの内容を取得
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # 必要なデータを抽出（例として、全ての<tr>タグのテキストを取得）
    data = []
    for link in soup.find_all('tr'):
        data.append(link.get_text().strip())

    # SQLiteデータベースに接続（なければ新規作成）
    conn = sqlite3.connect('GS_data.db')
    cursor = conn.cursor()

    # テーブルを作成（すでに存在する場合はスキップ）
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weapons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL
    )
    ''')

    # データを挿入
    for item in data:
        cursor.execute('INSERT INTO weapons (text) VALUES (?)', (item,))

    # コミットして接続を閉じる
    conn.commit()
    conn.close()

    print('データベースにデータを保存しました。')

else:
    print('Webページの取得に失敗しました。')


def search_weapon(weapon_name):
    # データベースに接続
    conn = sqlite3.connect('GS_data.db')
    cursor = conn.cursor()

    # 武器名を検索
    cursor.execute('SELECT * FROM weapons WHERE text LIKE ?', ('%' + weapon_name + '%',))
    results = cursor.fetchall()

    # 接続を閉じる
    conn.close()

    # 結果を返す
    if results:
        return results
    else:
        return "指定の武器は見つかりませんでした。"


# 例として、特定の武器名を検索
weapon_name = input("武器名を入れてください：")
search_results = search_weapon(weapon_name)

print(search_results)
