import flask
from books import book_search
from dotenv import find_dotenv, load_dotenv

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
    response = book_search(query_string)
    titles.append(response["items"][0]['volumeInfo']['title'])
    images.append(response["items"][0]['volumeInfo']["imageLinks"]['thumbnail'])

app = flask.Flask(__name__)

books = ["Far From the Tree", "They Can't Kill Us Until They Kill Us", "Misery", "A Gentleman in Moscow", "We Are the Weather"]

@app.route("/")
def index():
    query = flask.request.args.get("query")
    search_results = []  # search_results will be a list of dictionaries, where one dictionary = one search result
    if query is not None:  # query will be None if there was no form submission, i.e. first time we load the page
        response = book_search(query)
        for item in response["items"][:5]:  # Python shorthand for getting up to the first five elements of a list (but fewer if the list length is shorter)
            res = {}
            res["title"] = item['volumeInfo']['title']

            # .get() because there may be no subtitle
            res["subtitle"] = item['volumeInfo'].get('subtitle')

            # there may be multiple authors, there may be no author
            res["author"] = ", ".join(item['volumeInfo'].get('authors', []))

            # this is an inline if statement for Python. "x if A else y" evaluates to "x" if the expression "A" is true, and "y" otherwise
            res["image"] = item['volumeInfo']["imageLinks"]['thumbnail'] if "imageLinks" in item["volumeInfo"] else None
            search_results.append(res)

    return flask.render_template("index.html", titles=titles, images=images, search_results=search_results)

app.run(debug=True)