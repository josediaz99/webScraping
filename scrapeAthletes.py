"""
    this program takes in a url and scrapes the elements for athlete information
    returning a list of athletes as the main function
    
    we also use the link to traverse into the side menu where we can return a link to board
    
    using the url we also seach for the board link 
    

"""

from athlete import athlete 
from playwright.sync_api import sync_playwright

def getAthletes(comp):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto(comp)
        page.wait_for_selector("div.table-wrapper")
        
        isMale = True
        categoryKeywords = ["Raw", "Open", "Junior", "Teen", "Bench", "Master", "kg", "Sub-Junior", "Guest"]
        
        seen = set()
        athletes = []
        step = 300
        max_empty_scrolls = 5
        empty_scrolls = 0
        scrollY = 0

        while empty_scrolls < max_empty_scrolls:
            # Scroll grids
            page.evaluate("""
                (y) => {
                    document.querySelector('.grid-bottom-left')?.scrollTo(0, y);
                    document.querySelector('.grid-bottom-right')?.scrollTo(0, y);
                }
            """, scrollY)
            page.wait_for_timeout(500)

            # Get visible content
            left_cells = page.locator(".grid-bottom-left .table-cell-inner").all()
            right_cells = page.locator(".grid-bottom-right .table-cell-inner").all()
            left_data = [cell.inner_text().strip() for cell in left_cells]
            right_data = [cell.inner_text().strip() for cell in right_cells]

            new_found = 0

            for i in range(0, len(left_data), 3):
                if i + 1 >= len(left_data): continue
                
                name = left_data[i].strip()
                team = left_data[i + 1].strip()
                key = (name, team)
                
                #checks repeats
                if key in seen:
                    continue
                seen.add(key)
 
                body_index = (i // 3) * 11
                if body_index >= len(right_data): continue
                body_str = right_data[body_index]

                try:
                    weight = float(body_str)
                except ValueError:
                    weight = 0

                #checks for a category contained in a name / non athlete
                loweredName = name.lower()
                if weight == 0 and ("women's" in loweredName or "men's" in loweredName):
                    isMale = "women's" not in loweredName
                    continue

                
                #create an athlete
                a = athlete(name,team,isMale)
                try:
                    a.setWeight(weight)
                except ValueError:
                    pass
                
                athletes.append(a)
                new_found += 1

            if new_found == 0:
                empty_scrolls += 1
            else:
                empty_scrolls = 0

            scrollY += step
        browser.close()
        
        return athletes
        

if __name__ == "__main__":
    """
    check if we are getting a list of athletes in the correct format
    """
    comp = "https://liftingcast.com/meets/mxq6zp1pyf06/results"
    athletes = getAthletes(comp)
    for i in athletes:
        print(i)