import asyncio
from crawl4ai import AsyncWebCrawler
from bs4 import BeautifulSoup

'''
performs datascraping on the initial lifting cast page and enters the competition which is selected
+ stores a list of competitions which match the soonest date
+ stores a list of athletes the selected competition
  - allows to add/remove athletes to your team
  - stores athlete static stats (weightClass,weight,team,age)
'''
async def fetchEvents():
    '''
    this function gets the raw html from liftingcast
    we then parse the html using beautifulSoup to find the table with the information we want
    
    returns a list of dictionaries (compName,date,link)
    '''
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://liftingcast.com/")
        html = result.html

    soup = BeautifulSoup(html, 'html.parser')

    # find the element that matches the list table name were looking for
    anchor = soup.find('a', id='upcoming-meets')
    if not anchor:
        print("Couldn't find the Upcoming Meets anchor.")
        return

    # using the anchor find the table that contains the element
    table = anchor.find_parent('table')
    if not table:
        print("Couldn't find a parent <table> for Upcoming Meets.")
        return

    # gets only the body portion of the table
    tbody = table.find('tbody')
    if not tbody:
        print("No <tbody> in that table.")
        return

    rows = tbody.find_all('tr')  #gets every row
    
    events = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) < 2:
            continue

        a = cells[0].find('a', href=True)#gets the link in the href of the a element in the left cell
        name = a.get_text(strip=True)
        link = a['href']
        # transform it into the full link
        full_link = f"https://liftingcast.com{link}"

        date = cells[1].get_text(strip=True)#gets the data stored on the right cell of the element
        events.append({
            'name': name,
            'date': date,
            'link': full_link
        })

    # gets the first date and transforms the list that match the first date
    if events:
        first_date = events[0]['date']
        events = [e for e in events if e['date'] == first_date]

    return events
        
def getEvent(events):
    """displays the events in our list and returns the link of the chosen comp

    Args:
        events (list): list of dictionaries wich contain comp name, date , and link

    Returns:
        str: the string for the link of the specified competition
    """
    for i,event in enumerate(events):
        print(i,event['name'])
    
    comp = input("which competition(using the #): ")
    comp = int(comp)
    print("loading...")
    return events[comp]['link']

async def main():
    events = await fetchEvents()
    compUrl = getEvent(events)
    print(compUrl)
    
if __name__ == '__main__':
    asyncio.run(main())
    
    
    

   
    
