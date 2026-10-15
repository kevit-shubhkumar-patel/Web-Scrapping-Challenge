#this is the alternative with playwright 

from playwright.sync_api import sync_playwright

def scrape_iframe():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(
            "https://www.scrapethissite.com/pages/frames/",
            wait_until="domcontentloaded"
        )

        # Access the iframe
        frame = page.frame_locator("iframe")

        # Wait until the turtle family cards appear
        frame.locator(".turtle-family-card").first.wait_for()

        # Find all turtle family cards
        families = frame.locator(".turtle-family-card")

        print("Total families:", families.count())
        print("-" * 40)

        for i in range(families.count()):
            family = families.nth(i)

            name = family.locator(".family-name").inner_text().strip()

            print(f"Family Name: {name}")

        browser.close()


scrape_iframe()