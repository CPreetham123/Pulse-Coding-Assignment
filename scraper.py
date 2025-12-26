import argparse
import json
from datetime import datetime
from sources.g2 import scrape_g2
from sources.capterra import scrape_capterra
from sources.trustradius import scrape_trustradius


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--start_date", required=True)
    parser.add_argument("--end_date", required=True)
    parser.add_argument("--source", required=True)

    args = parser.parse_args()

    start = datetime.strptime(args.start_date, "%Y-%m-%d")
    end = datetime.strptime(args.end_date, "%Y-%m-%d")

    if args.source.lower() == "g2":
        reviews = scrape_g2(args.company, start, end)
    elif args.source.lower() == "capterra":
        reviews = scrape_capterra(args.company, start, end)
    elif args.source.lower() in ["trustradius", "trustradius"]:
        reviews = scrape_trustradius(args.company, start, end)
    else:
        print("Invalid source")
        return
    with open("output/sample_reviews.json", "w") as f:
        json.dump(reviews, f, indent=2)

    print("Done. Reviews saved.")

if __name__ == "__main__":
    main()
