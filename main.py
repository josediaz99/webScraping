from liftCastCompScrape import fetchEvents,getEvent
from scrapeLiftcastUrl import scrapeResult
import athlete

def main():
    events = fetchEvents()  # get the events from lifticast
    comp = getEvent(events) # get specific comp link from user
    athletes = scrapeResult(comp)      # get athlete information from url