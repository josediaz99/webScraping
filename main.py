from liftCastCompScrape import fetchEvents,getEvent
from scrapeAthletes import getAthletes
from athlete import athlete

def main():
    events = fetchEvents()                  # get the events from lifticast
    comp = getEvent(events)                 # get specific comp link from user
    boardUrl,athletes = getAthletes(comp)   # get athlete information from url
    