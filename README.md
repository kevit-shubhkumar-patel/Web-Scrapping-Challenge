# Scrapper Challenge

Four scrapers for [Scrape This Site](https://www.scrapethissite.com/pages/), each writing a CSV.

| Script | Page | Approach | Output |
| --- | --- | --- | --- |
| `scrapper_1.py` | Countries | Static HTML with BeautifulSoup | `scrapper_1_result.csv` — country, capital, population, area |
| `scrapper_2.py` | Hockey teams | Paginated HTML, pages 1–25 | `scrapper_2_result.csv` — team stats per season |
| `scrapper_3.py` | Oscar winners | JSON returned by the page’s AJAX endpoint, years 2010–2015 | `scrapper_3_result.csv` — title, nominations, awards, best picture |
| `scrapper_4.py` | Turtle families | Iframe page fetched directly, then parsed | `scrapper_4_result.csv` — family name and detail URL |
| `scrapper_4_pw.py` | Turtle families | Same page via Playwright, walking into the iframe | Prints family names only |

## Run

```bash
pip install requests beautifulsoup4
python scrapper_1.py
```

`scrapper_4_pw.py` also needs Playwright:

```bash
pip install playwright
playwright install chromium
python scrapper_4_pw.py
```
