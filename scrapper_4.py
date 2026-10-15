import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_iframe():
    url = "https://www.scrapethissite.com/pages/frames/?frame=i"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    families = soup.find_all("div", class_="turtle-family-card")

    total_families = 0

    with open(
        "scrapper_4_result.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Write CSV headers
        writer.writerow(["Family Name", "Detail URL"])

        for family in families:
            name = family.find("h3", class_="family-name")
            link = family.find(
                "a",
                string=lambda text: text and "Learn more" in text
            )

            if name and link:
                family_name = name.get_text(strip=True)
                detail_url = urljoin(url, link["href"])

                # Write data to CSV
                writer.writerow([family_name, detail_url])

                total_families += 1

                print(f"Family: {family_name}")
                print(f"URL: {detail_url}")
                print("-" * 40)

    print(f"\nTotal families scraped: {total_families}")
    print("Data saved to scrapper_4_result.csv")


scrape_iframe()