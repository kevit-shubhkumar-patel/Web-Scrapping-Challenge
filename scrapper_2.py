import requests
import csv
from bs4 import BeautifulSoup


def scrape_web():
    url = "https://www.scrapethissite.com/pages/forms/?page_num={}"

    total_teams = 0

    with open(
        "scrapper_2_result.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Team Name",
            "Year",
            "Wins",
            "Losses",
            "Win Percentage",
            "Goals For",
            "Goals Against",
            "Difference"
        ])

        # Scrape pages 1 through 25
        for page in range(1, 26):
            response = requests.get(
                url.format(page),
                timeout=5
            )
            response.raise_for_status()

            soup = BeautifulSoup(
                response.content,
                "html.parser"
            )

            result = soup.find_all("tr", class_="team")

            if not result:
                print(f"No teams found on page {page}. Stopping.")
                break

            print(f"Scraping page {page}...")

            for r in result:
                team_name = r.find("td", class_="name").get_text(strip=True)
                year = r.find("td", class_="year").get_text(strip=True)
                wins = r.find("td", class_="wins").get_text(strip=True)
                losses = r.find("td", class_="losses").get_text(strip=True)
                win_pct = r.find("td", class_="pct").get_text(strip=True)
                goals = r.find("td", class_="gf").get_text(strip=True)
                goals_against = r.find("td", class_="ga").get_text(strip=True)
                diff = r.find("td", class_="diff").get_text(strip=True)

                writer.writerow([
                    team_name,
                    year,
                    wins,
                    losses,
                    win_pct,
                    goals,
                    goals_against,
                    diff
                ])

                total_teams += 1

    print(f"\nTotal team records scraped: {total_teams}")
    print("Data saved to scrapper_2_result.csv")


scrape_web()