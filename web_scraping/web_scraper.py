"""
CodeAlpha - Data Analytics Internship
Task 1: Web Scraping
Target site: https://books.toscrape.com (sandbox site, safe for scraping practice)

Scrapes: Title, Price, Rating, Availability, Category
Output: books_data.csv
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Star rating words -> numbers (site uses class names like "star-rating Three")
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def scrape_page(page_num):
    """Scrape a single page and return a list of book dicts."""
    url = BASE_URL.format(page_num)
    response = requests.get(url)

    if response.status_code != 200:
        # No more pages left
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    page_data = []
    for book in books:
        # Title
        title = book.h3.a["title"]

        # Price (comes as "£51.77" -> clean to float)
        price_text = book.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        # Rating (class = "star-rating Three")
        rating_class = book.find("p", class_="star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_MAP.get(rating_word, None)

        # Availability
        availability = book.find("p", class_="instock availability").text.strip()

        page_data.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "availability": availability
        })

    return page_data


def scrape_all_books(max_pages=50):
    """Loop through all pages and collect data."""
    all_books = []
    page = 1

    while page <= max_pages:
        print(f"Scraping page {page}...")
        data = scrape_page(page)

        if data is None:
            print("No more pages found. Stopping.")
            break

        all_books.extend(data)
        page += 1
        time.sleep(1)  # polite delay so we don't hammer the server

    return all_books


if __name__ == "__main__":
    books = scrape_all_books()
    df = pd.DataFrame(books)

    df.to_csv("books_data.csv", index=False)
    print(f"\nDone! Scraped {len(df)} books.")
    print(f"Saved to books_data.csv")
    print("\nPreview:")
    print(df.head())