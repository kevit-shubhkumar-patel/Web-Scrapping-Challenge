import requests
import csv


def scrape_movies():
    url = "https://www.scrapethissite.com/pages/ajax-javascript/"

    total_movies = 0

    with open("scrapper_3_result.csv", "w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "Title",
            "Year",
            "Nominations",
            "Awards",
            "Best Picture"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for year in range(2010, 2016):

            params = {
                "ajax": "true",
                "year": year
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            movies = response.json()

            print(f"Scraping year: {year}")

            for movie in movies:
                writer.writerow({
                    "Title": movie.get("title", ""),
                    "Year": movie.get("year", year),
                    "Nominations": movie.get("nominations", 0),
                    "Awards": movie.get("awards", 0),
                    "Best Picture": movie.get("best_picture", False)
                })

                total_movies += 1

    print(f"\nTotal movie records scraped: {total_movies}")

scrape_movies()