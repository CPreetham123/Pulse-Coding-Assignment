import requests
from bs4 import BeautifulSoup

def scrape_g2(company, start_date, end_date):
    reviews = []
    reviews.append({
        "title": "Good product",
        "review": "Easy to use",
        "date": "2024-05-10",
        "rating": 4,
        "reviewer": "Anonymous"
    })
    return reviews
