# Crossref APIを使うためのライブラリをインポート
import requests
# CSVファイルを扱うためのライブラリをインポート
import csv

# ジャーナル名を指定
journal = "0165-0114"

# ページサイズを指定
rows = 20

# カーソルを初期化
cursor = "*"

# 論文の数をカウントする変数を初期化
count = 0

# CSVファイルを書き込みモードで開く（UTF-8を指定）
with open("papers.csv", "w", encoding="utf-8") as csvfile:
    # CSVファイルに書き込むオブジェクトを作成
    writer = csv.writer(csvfile)
    # ヘッダー行を書き込む
    writer.writerow(["DOI", "Title", "Authors", "Publication Date", "Abstract"])

    # 繰り返し処理
    while True:
        # Crossref APIのURLを作成（sortとorderパラメータを追加）
        url = f"https://api.crossref.org/journals/{journal}/works?rows={rows}&cursor={cursor}&sort=issued&order=desc"

        # APIにリクエストを送り、レスポンスを受け取る
        response = requests.get(url)

        # レスポンスが正常に受け取れたか確認
        if response.status_code == 200:
            # レスポンスのJSONデータを取得
            data = response.json()
            # 論文のリストを取得
            items = data["message"]["items"]
            # 論文ごとに処理
            for item in items:
                # DOIを取得
                doi = item["DOI"]
                # タイトルを取得（リスト型なので最初の要素だけ取る）
                title = item["title"][0]
                # 著者名を取得（複数いる場合はカンマで区切る）
                # authorキーが存在するかチェックする
                if "author" in item:
                    authors = ", ".join([author["family"] for author in item["author"]])
                else:
                    # authorキーがない場合は空文字列にする（Noneや"Unknown"などでも可）
                    authors = ""
                # 出版日を取得（年月日の順に並べる）
                date_parts = item["issued"]["date-parts"][0]
                date = "-".join([str(part) for part in date_parts])
                # 概要文を取得
                # abstractキーが存在するかチェックする
                if "abstract" in item:
                    abstract = item["abstract"]
                else:
                    # abstractキーがない場合は空文字列にする（Noneや"Not available"などでも可）
                    abstract = ""
                # CSVファイルに書き込む
                writer.writerow([doi, title, authors, date, abstract])
                # 論文の数をカウントアップ
                count += 1

                # コンソールにログとして出力する（必要な情報だけ表示）
                print(f"DOI: {doi}")
                print(f"Title: {title}")
                print(f"Authors: {authors}")
                print(f"Publication Date: {date}")
                print("-" * 80)  # 区切り線

            # 次のカーソルがあれば更新する
            if data["message"].get("next-cursor"):
                cursor = data["message"]["next-cursor"]
            else:
                break  # 次のカーソルがなければ終了する

        else:
            # エラーメッセージを表示して終了する
            print(f"Error: {response.status_code}")
            break

# 最終的な論文の数を表示する
print(f"Found {count} papers in {journal}")
