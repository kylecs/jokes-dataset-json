import requests
import time
import json

link = "http://reddit.com/r/jokes/top.json?raw_json=1&t=all"

# Custom user agent to avoid low rate limits on default one
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
     (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.\
     9 Safari/537.36"
}

pagenumber = 0

# Loop over pages
while link:
    pagenumber += 1
    code = 0
    response = None
    print("Getting: " + link)

    # Retry on errors
    while code is not 200:
        response = requests.get(link, headers=headers)
        code = response.status_code
        if code is not 200:
            print("Got response code " + str(code) + ", retrying...")
            time.sleep(2)

    print("Got page, interpreting...")
    jokes = []
    nextlink = None
    data = response.json()
    for post in data["data"]["children"]:
        postdata = post["data"]

        # Ignore some bad posts
        if postdata["domain"] != "self.Jokes":
            continue

        if postdata["stickied"]:
            continue

        # Joke Info
        jokedata = {
            "part1": postdata["title"],
            "part2": postdata["selftext"],
            "mature": postdata["over_18"],
            "score": postdata["score"],
            "author": postdata["author"],
            "link": postdata["url"],
        }
        jokes.append(jokedata)

    # Write page to file as json array
    pagefile = open("data/" + str(pagenumber) + ".json", "w")
    pagefile.writelines(json.dumps(jokes, indent=2))
    pagefile.close()

    after = data["data"]["after"]
    if after:
        link = "http://reddit.com/r/Jokes/top.json?raw_json=1&t=all&after=" \
                + after
    else:
        link = None

# Done
print("No more pages to get!")
