import asyncio
from crawl4ai import AsyncWebCrawler
from bs4 import BeautifulSoup

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://liftingcast.com/")
        html = result.html

    soup = BeautifulSoup(html, 'html.parser')

    # 1) Locate the anchor inside the target table
    anchor = soup.find('a', id='upcoming-meets')
    if not anchor:
        print("Couldn't find the Upcoming Meets anchor.")
        return

    # 2) Climb up to the table that contains it
    table = anchor.find_parent('table')
    if not table:
        print("Couldn't find a parent <table> for Upcoming Meets.")
        return

    # 3) Pull only its <tbody> rows
    tbody = table.find('tbody')
    if not tbody:
        print("No <tbody> in that table.")
        return

    rows = tbody.find_all('tr')  # assuming <thead> is separate
    events = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) < 2:
            continue
        name = cells[0].get_text(strip=True)
        date = cells[1].get_text(strip=True)
        events.append({'name': name, 'date': date})

    # 4) Filter to only those on the first date
    if events:
        first_date = events[0]['date']
        events = [e for e in events if e['date'] == first_date]

    # 5) Print
    for e in events:
        print(f"{e['name']} — {e['date']}")

if __name__ == '__main__':
    asyncio.run(main())
