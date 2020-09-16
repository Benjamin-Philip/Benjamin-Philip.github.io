from bs4 import BeautifulSoup
from requests import Session

with Session() as s:
    # initial GET request
    site = s.get("http://quotes.toscrape.com/login")
    # parsing content
    html_content = BeautifulSoup(site.content, "html.parser")
    # fetch token value
    token_value = html_content.find("input", {"name": "csrf_token"})["value"]
    # write login details
    login_data = {"username": "ben", "password": "123", "csrf_token": token_value}
    # POST request
    s.post("http://quotes.toscrape.com/login", login_data)
    # GET request
    site = s.get("http://quotes.toscrape.com")
    # Parse home page
    home_page = BeautifulSoup(site.content, "html.parser")
    print(home_page)
