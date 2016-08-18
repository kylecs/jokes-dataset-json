#Jokes Dataset

About 1000 jokes scraped from reddit.com/r/jokes/top. Data is stored in all.json
as a large array of json objects.

Each joke has the following attributes:

part1: The first part of the joke,
part2: The final part of the joke,
mature: True if the joke is not safe for work,
score: The score it got on reddit
author: reddit username of original poster,
link: Link to the reddit thread that the joke came from

The data was initially downloaded in unformatted page segments with scrape.py,
then format.py formats the text to be more readable while removing useless text
and concatenating all data into one large array. 
