from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError, InvalidAuthorError

try:
    chrome = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    authors = page.get_available_authors()
    print("Select one of these authors: [{}]".format(" | ".join(authors)))

    author = input("Enter the author you'd like quotes from: ")
    page.select_author(author)

    tags = page.get_available_tags()
    print("Select one of these tags: [{}]".format(" | ".join(tags)))
    selected_tag = input("Enter your tag: ")

    page.select_tag(selected_tag)
    page.search_button.click()

    print(page.quotes)
except InvalidTagForAuthorError as e:
    print(e)
except InvalidAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")

