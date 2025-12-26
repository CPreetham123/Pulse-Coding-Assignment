# Pulse-Coding-Assignment

# Pulsegen Review Scraper

## Description
Python script to scrape SaaS product reviews from multiple platforms and export them as JSON.

## Sources Supported
- G2
- Capterra
- TrustRadius (Bonus)

## How to Run
pip install -r requirements.txt
python scraper.py --company Chargebee --start_date 2024-01-01 --end_date 2024-06-30 --source g2

### Run with TrustRadius (Bonus)
python scraper.py --company Chargebee --start_date 2024-01-01 --end_date 2024-06-30 --source trustradius

## Output
JSON output is saved in output/sample_reviews.json

[
  {
    "title": "Reliable SaaS platform",
    "review": "Good features and customer support",
    "date": "2024-05-15",
    "rating": 4,
    "reviewer": "Enterprise User"
  }
]
