import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
key = os.getenv("API_KEY")

def book_search(title):
    """
    Helper function to fetch the JSON response for a given search term from the 
    Google Books API.

    There's a lot more common code in this project, but it's hard to find the right function
    to split off because we grab different information for the search results vs. the favorite books.
    This is the best I could do off the top of my head, but there's probably a better way to organize
    this code floating around.
    """
    response = requests.get(
        # We technically don't need the API key. Apparently Google doesn't actually
        # require that, even though their documentation claims they do
        "https://www.googleapis.com/books/v1/volumes", params={"q": title, "key": key}
    )

    return response.json()