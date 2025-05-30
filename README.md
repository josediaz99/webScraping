The project aims to improve the powerlifting competition experience for lifters without an experienced coach using lifting cast.

The goal is to provide a less experienced competitor or coach handling many athletes with the tools to make better decisions in the minutes they are allowed to declare an attempt
The data is readily available on lifting cast, but without the help of a handler or while tracking multiple athletes, this information can be overwhelming 

liftcastCompScrape.py 
- scrapes lift cast home page for competitions theyre date and link to get to the competition pages
- returns a list of competitions to be used to display competitions on the day

athlete.py
-class file used for formating data which is found in the competition chosen from liftcastcompscrape.py
athlete data
- name
- team
- weight
- sex
- weightclass
- bestsquat
- bestbench
- bestdead
- total
- glPoints


scrapeAthlete.py
- scrapes competition home page selected by liftcastcompscrape.py
- itterated through data to build an athlete list with the information available without including duplicates
- returns a list of athletes with the minimum information needed to seporate athletes
  athletes
  - name
  - team
  - sex
  - weight
  - weightclass


 to be implemented
- being allowed to select multiple athletes to manage a team
- Display athlete ranking as the competition progresses (dots, pl points, total)
- displaying team ranking as competition progresses (dops, pl points)
- 
