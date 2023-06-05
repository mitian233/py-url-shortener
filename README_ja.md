![py-url-shortener](https://socialify.git.ci/mitian233/py-url-shortener/image?description=1&language=1&name=1&owner=1&stargazers=1&theme=Light)
Python でかかれた URL 短縮サービス

Heroku や Vercel などの PaaS プラットフォームにデプロイすることができます。

## デプロイ手順

### 自構築サーバー

このリポジトリを Clone して、依存関係をインストールします。

```shell
git clone https://github.com/mitian233/py-url-shortener.git
cd py-url-shortener
pip install -r requirements.txt
```

**このプロジェクトでは、[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)はデータベースとして使用しているため、MongoDB Atlasのアカウントとデータベースクラスターを作成する必要があります。**

`.env.example` ファイルを `.env` にコピーして、環境変数を埋めます。

```shell
cp .env.example .env
```

こんなふうに `.env` ファイルを編集します：

```text
MONGO_URL = mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority
MONGO_DB = Cluster0
MONGO_COLLECTION = ShortenedURLs
URL_LENGTH = 5
SITE_URL = https://s.mikan.ac.cn
```

以下のコマンドを実行してサーバーを起動できます：

```shell
gunicorn -b 0.0.0.0:5000 index:app
```

Nginx などのリバースプロキシを設定して、リクエストをサーバーに転送できるになります。

✨サイトは現在公開されています！

### Vercel

以下のボタンをクリックして、Vercel 上に展開できます。

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/mitian233/py-url-shortener)

上記の環境変数の説明に従って、Vercel ダッシュボードで環境変数を編集します。

![image.png](https://s2.loli.net/2023/06/05/62VYnTwGkiyIEU7.png)

**⚠️毎度環境変数が変更された場合、Vercel ダッシュボードで再デプロイすることが必要です。**

Live demo: https://s.mikan.ac.cn/NmPlq