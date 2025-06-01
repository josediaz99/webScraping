from website import create_app
from liftCastCompScrape import fetchEvents,getEvent
from scrapeAthletes import getAthletes

app = create_app()

def main():
    events = fetchEvents()                  # get the events from lifticast
    comp = getEvent(events)                 # get specific comp link from user
    boardUrl,athletes = getAthletes(comp)   # get athlete information from url

if __name__ == "__main__":
    app.run(debug=True)