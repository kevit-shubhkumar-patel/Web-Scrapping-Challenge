import requests
import csv
from bs4 import BeautifulSoup

def scrape_web():

    url = 'https://www.scrapethissite.com/pages/simple'
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("div", class_ = "col-md-4 country")

    with open("scrapper_1_result.csv","w", newline="",encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Country Name",
            "Capital",
            "Population",
            "Area"
        ])

        for r in result:
            country_name = r.find("h3", class_="country-name")
            country_capital = r.find("span", class_="country-capital")
            country_population = r.find("span", class_="country-population")
            country_area = r.find("span", class_="country-area")


            name = country_name.get_text(strip=True)
            capital = country_capital.get_text(strip=True)
            population = country_population.get_text(strip=True)
            area = country_area.get_text(strip=True)

            writer.writerow([
                name,
                capital,
                population,
                area
            ])

scrape_web()