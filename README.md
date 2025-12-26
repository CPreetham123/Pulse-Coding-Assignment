# Pulse-Coding-Assignment

# Pulsegen Review Scraper

## Description
Python script to scrape SaaS product reviews from G2 and Capterra and export them as JSON.

## Sources Supported
- G2
- Capterra

## How to Run
pip install -r requirements.txt
python scraper.py --company Chargebee --start_date 2024-01-01 --end_date 2024-06-30 --source g2

## Output
JSON output is saved in output/sample_reviews.json

## Assumptions
- Review data is mocked to demonstrate structure
- Script is designed for easy extension

## Limitations
- Live scraping may require Selenium for dynamic pages
