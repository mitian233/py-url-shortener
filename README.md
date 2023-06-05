![py-url-shortener](https://socialify.git.ci/mitian233/py-url-shortener/image?description=1&language=1&name=1&owner=1&stargazers=1&theme=Light)

[日本語](https://github.com/mitian233/py-url-shortener/blob/master/README_ja.md)

You can deploy it on any PaaS provider like Heroku, Vercel, etc.
 
## Get started

### Self-host

Clone this repository and install the dependencies.

```shell
git clone https://github.com/mitian233/py-url-shortener.git
cd py-url-shortener
pip install -r requirements.txt
```

**This project uses [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) as the database, so you need to create a MongoDB Atlas account and a database cluster.**

Copy the `.env.example` file to `.env` and fill in the environment variables.

```shell
cp .env.example .env
```

The `.env` file should look like this:

```text
MONGO_URL = mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority
MONGO_DB = Cluster0
MONGO_COLLECTION = ShortenedURLs
URL_LENGTH = 5
SITE_URL = https://s.mikan.ac.cn
```

Then run the following command to start the server.

```shell
gunicorn -b 0.0.0.0:5000 index:app
```

Set up your reverse proxy like Nginx to forward requests to the server.

✨Your site is on live now!

### Vercel

Click the button below to deploy it on Vercel.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/mitian233/py-url-shortener)

Following the introduction of the environment variables descriped above and edit the Environment Variables in the Vercel dashboard.

![image.png](https://s2.loli.net/2023/06/05/62VYnTwGkiyIEU7.png)

**⚠️Once you change the environment variables, you need to redeploy your project!**

Live demo: https://s.mikan.ac.cn/NmPlq