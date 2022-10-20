import flask
import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
key = os.getenv("API_KEY")

query_strings = [
    "far from the tree andrew solomon",
    "they can't kill us until hanif abdurraqib",
    "misery stephen king",
    "a gentleman in moscow",
    "we are the weather johnathan safran foer"
]
titles = []
images = []

for query_string in query_strings:
    response = requests.get(
        # We technically don't need the API key. Apparently Google doesn't actually
        # require that, even though their documentation claims they do
        "https://www.googleapis.com/books/v1/volumes", params={"q": query_string, "key": key}
    )

    response = response.json()
    titles.append(response["items"][0]['volumeInfo']['title'])
    images.append(response["items"][0]['volumeInfo']["imageLinks"]['thumbnail'])

app = flask.Flask(__name__)

books = ["Far From the Tree", "They Can't Kill Us Until They Kill Us", "Misery", "A Gentleman in Moscow", "We Are the Weather"]

@app.route("/")
def index():
    return flask.render_template("index.html", titles=titles, images=images)

app.run(debug=True)